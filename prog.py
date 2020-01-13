# Source: https://docs.python.org/3.7/howto/argparse.html#id1
# bookmark: https://docs.python.org/3.7/howto/argparse.html#combining-positional-and-optional-arguments

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()
if args.verbose:
    print("verbosity turned on")