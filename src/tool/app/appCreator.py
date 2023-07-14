import uvicorn
from dataclasses import dataclass, is_dataclass
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from dependency_injector.wiring import inject, Provide
from typing import List, Dict
from pprint import pprint

from src.api.constructor import ApiConstructor
from src.tool.app.app import RunConfig, MiddlewareConfig
from src.container.app.appInitializeContainer import AppInitializeContainer


class AppCreator:
    @inject
    def __init__(
            self,
            run_config: RunConfig = Provide[AppInitializeContainer.run_config],
            middleware_config: MiddlewareConfig = Provide[AppInitializeContainer.middleware_config],
            app_routers: ApiConstructor = Provide[AppInitializeContainer.api_routers]
    ):
        self._run_config: RunConfig = run_config
        self._middleware_config: MiddlewareConfig = middleware_config
        self._app_routers: ApiConstructor = app_routers

    def create_app(self) -> FastAPI:
        app: FastAPI = FastAPI()

        app.add_middleware(
            CORSMiddleware,
            allow_origins=self._middleware_config.allow_origins,
            allow_credentials=self._middleware_config.allow_credentials,
            allow_methods=self._middleware_config.allow_methods,
            allow_headers=self._middleware_config.allow_headers,
        )

        injection_map: Dict[str, List[APIRouter]] = self._gen_injection_map(router_class=self._app_routers)

        self._route_injection(
            [injection_map],
            [app]
        )

        pprint(app.routes)

        return app

    def run_app(self, app: FastAPI) -> None:
        uvicorn.run(
            app=app,
            host=self._run_config.host,
            port=self._run_config.port,
            reload=self._run_config.reload,
            workers=self._run_config.workers
        )

    @classmethod
    def _gen_injection_map(cls, router_class: dataclass) -> Dict[str, List[APIRouter]]:
        injection_map: Dict[str, List[APIRouter]] = {}

        def _split_router(routes_class: dataclass, parent_prefix: str = ""):
            current_prefix: str = parent_prefix + routes_class.prefix
            target_routers = injection_map.get(current_prefix, [])

            for k, v in vars(routes_class).items():
                if is_dataclass(v):
                    _split_router(routes_class=v, parent_prefix=current_prefix)

                elif isinstance(v, APIRouter):
                    target_routers.append(v)

            injection_map[current_prefix] = target_routers

        _split_router(routes_class=router_class)

        return injection_map

    @classmethod
    # 추후 여러개의 app를 생성해서 app끼리 app.mount를 통해 빌드할 수도 있다는 판단에 List[] 형태로 요구!!!
    def _route_injection(cls, injection_maps: List[Dict[str, List[APIRouter]]], apps: List[FastAPI]):
        if len(injection_maps) != len(apps):
            raise Exception("Args Length must be Same")
        [
            target_app.include_router(router, prefix=prefix) for
            injection_map, target_app in zip(injection_maps, apps) for
            prefix, routers in injection_map.items() for
            router in routers
        ]
