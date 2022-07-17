import argparse
import sys
#
# def calc(args):
#     if args.o == 'add':
#         return args.x + args.y
#
#     elif args.o == 'mul':
#         return args.x * args.y
#
#     elif args.o == 'sub':
#         return args.x - args.y
#
#     elif args.o == 'div':
#         return args.x / args.y
#
#     else:
#         return "Something went wrong"
#
#
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--x', type=float, default=1.0,
#                         help="Enter first number. This is a utility for calculation. Please contact harry bhai")
#
#     parser.add_argument('--y', type=float, default=3.0,
#                         help="Enter second number. This is a utility for calculation. Please contact harry bhai")
#
#     parser.add_argument('--o', type=str, default="add",
#                         help="This is a utility for calculation. Please contact harry bhai for more")
#
#     args = parser.parse_args()
#     sys.stdout.write(str(calc(args)))

# ab faulty calculator wale ko ese run karna hai

def calc(args):
    if args.x == 45 and args.y == 3 and args.o == 'mul':
        return "145.0"
    elif args.x == 56 and args.y == 9 and args.o == 'add':
        return "67.0"
    elif args.x == 56 and args.y == 6 and args.o == 'div':
        return "9.7"
    elif args.o == 'add':
        return args.x + args.y

    elif args.o == 'mul':
        return args.x * args.y

    elif args.o == 'sub':
        return args.x - args.y

    elif args.o == 'div':
        return args.x / args.y

    else:
        return "Something went wrong"

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0,
                        help="Enter the First number")
    parser.add_argument('--y', type=float, default=3.0,
                        help="Enter the Second number")
    parser.add_argument('--o', type=str, default="add",
                        help="Enter the operation you want to do")

    argss = parser.parse_args()
    sys.stdout.write(str(calc(argss)))

































