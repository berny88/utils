import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", help="filename")
parser.add_argument("-se", help="string which excludes")


args = parser.parse_args()
print(args)
#for arg in args:
#    print("option {}={}".format(arg))