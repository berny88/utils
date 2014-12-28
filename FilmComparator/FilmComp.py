# -*- coding: utf-8 -*-
import logging
import sys
import FilmFile
import json
#
# Syntax : python FilmComp.py File1.csv File2.csv
# build a structure of data for each Product : the structure defines
# the quantity of product
# for a type of film (JT/JL/SYNC)
# Structure of csv : TYPEEXPORT;COMPUTING_DATE;ID_PRODUCT;TYPE_FILM;QTY
# where :
#TYPEEXPORT define the kinf od "Film" FBB or FBPC...
# COMPUTING_DATE : the date of compute
# ID_PRODUCt : product code
# TYPE_FILM = JT/JL/SYNC
# QTY : quantity of parts for a product code


# ****************************
# compare the 2 dictionnaries
def compareDictionnaries(firstDict, secondDict):
    #compare 1st key with the 2nd
    logging.info("compareDictionnaries")
    logging.info("dict %s", firstDict)
    logging.info("dict %s", secondDict)
    for product in firstDict.keys():
        productValuesInFirstFile = firstDict.get(product)
        productValuesInSecondFile = secondDict.get(product)
        if (not productValuesInSecondFile is None):
            for typeFilm in productValuesInFirstFile:
                if (productValuesInFirstFile.get(typeFilm) !=
                    productValuesInSecondFile.get(typeFilm)):
                    logging.info("Difference : Product : %s  : TypeFilm : " +
                    "%s: 1st : %s : 2nd : %s", product, typeFilm,
                    productValuesInFirstFile.get(typeFilm),
                    productValuesInSecondFile.get(typeFilm))
        else:
            logging.info("Product only in First file : %s", product)
    for product in secondDict.keys():
        productValuesInFirstFile = firstDict.get(product)
        productValuesInSecondFile = secondDict.get(product)
        if (productValuesInFirstFile is None):
            logging.info("Product only in Second file : %s : values : %s",
                 product, productValuesInSecondFile)


# ************************
#
def main():
    logging.basicConfig(format='%(asctime)s|%(levelname)s|%(message)s',
        filename='myapp.log', level=logging.DEBUG)
    logging.info('Started')
    # load the 2 files
    # Populate dictionnary
    filmA = FilmFile.FilmFile(sys.argv[1])
    filmB = FilmFile.FilmFile(sys.argv[2])
    #display to console
    filmA.printDictionnary()
    filmB.printDictionnary()
    # compare dictionnaries
    compareDictionnaries(filmA.productList, filmB.productList)
    with open('FilmA.txt', 'w') \
        as fichier:
        #print json.dumps(filmA.productList, indent=4)
        json.dump(filmA, fichier, indent=4, default=FilmFile.FilmFile.jdefault)

    with open('FilmB.txt', 'w') \
        as fichier:
        #print json.dumps(filmB.productList, indent=4)
        json.dump(filmB, fichier, indent=4, default=FilmFile.FilmFile.jdefault)

    logging.info('Finished')

if __name__ == '__main__':
    main()