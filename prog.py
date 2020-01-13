# Source: https://docs.python.org/3.7/howto/argparse.html#id1

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--verbosity", help="increase output verbosity")
args = parser.parse_args()
if args.verbosity:
    print("verbosity turned on")