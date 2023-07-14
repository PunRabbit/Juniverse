from dataclasses import dataclass
from dependency_injector.containers import DeclarativeContainer

from src.container.app.appInitializeContainer import AppInitializeContainer


@dataclass(frozen=True)
class ContainerConstructor:
    initial_config_container: DeclarativeContainer = AppInitializeContainer()


