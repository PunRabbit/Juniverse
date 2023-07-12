import argparse


def create_parser() -> argparse.Namespace:
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument("--runtime", "-rt", action="store", help="Set Runtime Env")
    parse_args: argparse.Namespace = parser.parse_args()

    return parse_args
