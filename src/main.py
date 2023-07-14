import sys
import os

# Todo: Path 설정을 코드로 말고 다른 방식으로 할 것...
current_path: str = os.getcwd()
sys.path.append(current_path[:current_path.rfind("/")])

from src.tool.app.appCreator import AppCreator


if __name__ == "__main__":
    # 순환참조 방지, 추후 개선 요망
    from src.container.containerconstructor import ContainerConstructor

    ContainerConstructor()

    app_creator: AppCreator = AppCreator()
    app_creator.run_app(
        app=app_creator.create_app()
    )
