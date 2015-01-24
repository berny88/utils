import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", help="filename")
parser.add_argument("-se", help="string which excludes")


args = parser.parse_args()
print("{} - {}".format(parser.prog, args))

print("{} ".format(vars(args)))

params = vars(args)
for arg in params:
    print("option {}={}".format(arg, params[arg]))