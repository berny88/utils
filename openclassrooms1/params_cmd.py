from tkinter import *
import re
import argparse

"""
Exemple de gestion de paramètres en ligne de commande
"""

parser = argparse.ArgumentParser()
parser.add_argument("-f", help="filename")
parser.add_argument("-se", help="string which excludes")

args = parser.parse_args()
print(("Script Name = {} - ParamStructure = {}".format(parser.prog, args)))

#transform into dict
params = vars(args)
for arg in params:
    print("\toption param {}={}".format(arg, params[arg]))

#test option ui : boolean
if (not args.f is None):
    print(("Traitement Fichier ={}".format(args.f)))
elif (not args.se is None):
    print(("string replacement ={}".format(args.se)))
else:
    from getpass import getpass
    mot_de_passe = getpass()
    print(("Mot de passe saisi={}".format(mot_de_passe)))


