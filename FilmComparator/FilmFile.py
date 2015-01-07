# -*- coding: utf-8 -*-
import logging
import csv
import structcsv


class FilmFile:
    """     load and parse a FilmFile"""

    def __init__(self, fileName):
        """
        open and load a film file
        """
        self.fileName = fileName
        self.productList = dict()
        logging.debug("constructor: %s ", self.fileName)
        logging.debug("productList: %s ", self.productList)
        with open(self.fileName, "r") as src:
            reader = csv.reader(src, structcsv.MyCsvDialect())
            # Puis les données
            for row in reader:
                self.populateOneKey(row)

    def populateOneKey(self, row):
        """
        parse one row and populate the dictionnary
        exclude header
        """
        if (not row[0] == "TYPEEXPORT"):
            if (not row[2] in self.productList):
                #print "pas trouve " + row[1]
                productDict = dict()
                self.productList[row[2]] = productDict
            productDict = self.productList[row[2]]
            if row[3] == "JL":
                productDict["JL"] = row[4]
            if row[3] == "JT":
                productDict["JT"] = row[4]
            if row[3] == "SYNC":
                productDict["SYNC"] = row[4]
        logging.debug("populateOneKey: %s ", self.productList)

    # *****************************
    def printDictionnary(self):
        """ display the content of a dictionnary """
        logging.debug("printDictionnary : %s ************", self.fileName)
        for key, value in self.productList.iteritems():
            logging.debug("key : %s : value : %s", key, value)

    def jdefault(o):
        return o.__dict__