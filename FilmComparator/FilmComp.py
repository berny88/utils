# -*- coding: utf-8 -*-
import logging
import csv
from datetime import datetime

import structcsv

startDateTime = datetime.today()
print startDateTime


#
#Return a Dictionnary of Product for one file
def ExtractProductList(src):
    #
    #
    reader = csv.reader(src, structcsv.MyCsvDialect())
    productList = dict()
    # Puis les données
    for row in reader:
        populateOneKey(productList, row)
    return productList


# ******************
# parse one row and populate the dictionnary
def populateOneKey(productList, row):
    #exclude header
    if (not row[0] == "Category"):
        if (not row[1] in productList):
            #print "pas trouve " + row[1]
            productDict = dict()
            productList[row[1]] = productDict
        productDict = productList[row[1]]
        if row[2] == "JL":
            productDict["JL"] = row[3]
        if row[2] == "JT":
            productDict["JT"] = row[3]
        if row[2] == "SYNC":
            productDict["SYNC"] = row[3]


# display the content of a dictionnary
def printDictionnary(theDict):
    logging.debug("printDictionnary ************")
    for key, value in theDict.iteritems():
        logging.debug("key : %s : value : %s", key, value)


# compare the 2 dictionnaries
def compareDictionnaries(firstDict, secondDict):
    #compare 1st key with the 2nd
    logging.info("compareDictionnaries ************")
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
            print "Product only in First file : ", product
    for product in secondDict.keys():
        productValuesInFirstFile = firstDict.get(product)
        productValuesInSecondFile = secondDict.get(product)
        if (productValuesInFirstFile is None):
            logging.info("Product only in Second file : %s : values : %s",
                 product, productValuesInSecondFile)


def main():
    logging.basicConfig(format='%(asctime)s %(message)s',
        filename='myapp.log', level=logging.DEBUG)
    logging.info('Started')
    try:
        # Open the 2 files
        firstFile = open("FilmA.csv", "r")
        secondFile = open("FilmB.csv", "r")
        # Populate dictionnaries
        firstProductDict = ExtractProductList(firstFile)
        secondProductDict = ExtractProductList(secondFile)
        #display to console
        printDictionnary(firstProductDict)
        printDictionnary(secondProductDict)
        # compare dictionnaries
        compareDictionnaries(firstProductDict, secondProductDict)
    finally:
        # Close files
        firstFile.close()
        secondFile.close()
    logging.info('Finished')

if __name__ == '__main__':
    main()