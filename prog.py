# Source: https://docs.python.org/3.7/howto/argparse.html#id1
# bookmark: https://docs.python.org/3.7/howto/argparse.html#getting-a-little-more-advanced

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display a square of a given number")
parser.add_argument("-v", "--verbosity", action="count", default=0,
                    help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2

# bugfix: replace == with >=
if args.verbosity >= 2:
    print("The square of {} equals {}".format(args.square,answer))
elif args.verbosity >= 1:
    print("{}^2 == {}".format(args.square, answer))
else:
    print(answer)