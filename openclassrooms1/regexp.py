from tkinter import *
import re
import argparse

"""
Exemple de gestion de paramètres en ligne de commande
"""

parser = argparse.ArgumentParser()
parser.add_argument("-f", help="filename")
parser.add_argument("-se", help="string which excludes")
parser.add_argument("-ui", help="to display a simple windows", \
    action="store_true")


args = parser.parse_args()
print("{} - {}".format(parser.prog, args))

print("{} ".format(vars(args)))

params = vars(args)
for arg in params:
    print("option {}={}".format(arg, params[arg]))

# *******
print("**************************")


#expression = input("chaine à chercher : ")
#chaine = "ponpon toto tititi"
#if re.search(expression, chaine):
    #print("found ::{} in [{}]".format(expression, chaine))


#print("**************************")
# pour changer une chaine par une autre
#texte = """nom='Task1'|ThreadID=8|thread-xxx-xxx-Z
#"""
#print(re.sub(r"(?P<id>ThreadID=)", r"t[\g<id>]", texte))
#

# sipplement remplacement d'une chaine'
print("ponpon toto titi".replace("toto", "T"))

texte = "12/02/2015 12:54:44.0000"
print(texte)
# supprime une chaine décrite par une regexp
print(re.sub(r"(\.[0-9]{4})", r"", texte))


class Interface(Frame):

    """Notre fenêtre principale.
    Tous les widgets sont stockés comme attributs de cette fenêtre."""


    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        self.pack(fill=BOTH)
        self.nb_clic = 0

        # Création de nos widgets
        self.message = Label(self, text="Vous n'avez pas cliqué sur le bouton.")
        self.message.pack()
        self.bouton_quitter = Button(self, text="Quitter", command=self.quit)
        self.bouton_quitter.pack(side="left")

        self.bouton_cliquer = Button(self, text="Cliquez ici", fg="red",
                command=self.cliquer)
        self.bouton_cliquer.pack(side="right")
        self.pack()

    def cliquer(self):
        """Il y a eu un clic sur le bouton.
        On change la valeur du label message."""
        self.nb_clic += 1
        self.message["text"] = "Vous avez cliqué {} fois.".format(self.nb_clic)

if (args.ui):
    fenetre = Tk()
    interface = Interface(fenetre)
    interface.mainloop()
    interface.destroy()
else:
    from getpass import getpass
    mot_de_passe = getpass()
    print(mot_de_passe)