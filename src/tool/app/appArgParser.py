import argparse


def create_parser() -> argparse.Namespace:
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument("--runtime", "-rt", action="store", help="Set Runtime Env")
    parse_args: argparse.Namespace = parser.parse_args()

    return parse_args


parse_args: argparse.Namespace = create_parser()

if parse_args.runtime not in ["dev", "live"]:
    raise Exception("Please write down runtime dev envs.")