# Source: https://docs.python.org/3.7/howto/argparse.html#id1

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number",
                    type=int)
args = parser.parse_args()
print(args.square**2)