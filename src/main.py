import sys
import os

current_path: str = os.getcwd()
sys.path.append(current_path[:current_path.rfind("/")])

from src.tool.app.appCreator import AppCreator


if __name__ == "__main__":
    from src.container.containerconstructor import ContainerConstructor

    ContainerConstructor()

    app_creator: AppCreator = AppCreator()
    app_creator.run_app(
        app=app_creator.create_app()
    )
