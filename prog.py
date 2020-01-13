# Source: https://docs.python.org/3.7/howto/argparse.html#id1

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("echo")
args = parser.parse_args()
print(args.echo)