import argparse

parser = argparse.ArgumentParser(
    description="This scrjkfsadkljflj"
)


parser.add_argument(
    "--name",
    type=str,
    help="You name (required input)",
    # required=True
)

parser.add_argument(
    "-m", "--mode",
    choices=["enable", "disable"],
    help="Set enable or disable conservation mode"
)

args = parser.parse_args()

print(f"hello, {args.name} and mode is {args.mode}")