import argparse
import tomlkit
from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import Singleton

from src.tool.app.app import MiddlewareConfig, RunConfig
from src.tool.app.appArgParser import parse_args
from src.api.constructor import ApiConstructor


class AppInitializeContainer(DeclarativeContainer):
    with open("core/app/appConfig.toml", "r") as config_file:
        toml_config: dict = tomlkit.load(config_file)

    middleware_config: MiddlewareConfig = Singleton(
        MiddlewareConfig,
        **toml_config[parse_args.runtime]["middleware"]
    )

    run_config: RunConfig = Singleton(
        RunConfig,
        **toml_config[parse_args.runtime]["run"]
    )

    api_routers: ApiConstructor = Singleton(
        ApiConstructor
    )

    wiring_config: WiringConfiguration = WiringConfiguration(
        modules=[
            "src.tool.app.appCreator",
        ]
    )
