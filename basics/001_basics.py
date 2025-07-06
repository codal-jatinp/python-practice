import sys
import argparse

parser = argparse.ArgumentParser(
    description='sum the integers at the command line'
)
parser.add_argument(
    'integers', metavar='int', nargs='+', type=int,
    help='an integer to be summed'
)
parser.add_argument(
    '--log', default=sys.stdout, type=argparse.FileType('w'),
    help='the file where the sum should be written'
)
args = parser.parse_args()
args.log.write('%s' % sum(args.integers))
# args.log.close()

# age: str = ''

# while (len(age) < 1):
#     age = input("Enter your age: ").strip()
#     if len(age) > 0 and (not str.isnumeric(age)):
#         print("not a valid age")
#         age = ''
# else:

#     new_age = int(age) + 50
#     print("Your age after 50 years is: ", new_age)
