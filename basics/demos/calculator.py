from argparse import ArgumentParser
from typing import Iterable

parser = ArgumentParser(description="sum the integers at the command line")
parser.add_argument('integers', metavar='int', nargs='+',
                    type=int, help='an integer to be computed')
parser.add_argument('operation', metavar='str', nargs=1,
                    type=str, help='operation')

args = parser.parse_args()


def multiply(items: Iterable[int]):
    res = 1
    for i in items:
        res *= i
    return res


if args.operation[0] == '+':
    print("%s" % sum(args.integers))
elif args.operation[0] == '-':
    print("%s" % sum([-i for i in args.integers]))
elif args.operation[0] == '*':
    print("%s" % multiply(args.integers))
