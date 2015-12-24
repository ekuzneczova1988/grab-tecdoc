# -*- coding: utf-8 -*-
from generators.bdnormilize import getManufactures, getModels, updateModel,\
    getModelsAll
import re


def dbBodyNameParse():
    for manufacture in getManufactures():
        for model in getModels(manufacture.manid):
            p = re.compile('.*\((.*)\).*')
            try:
                parsedbodyid = p.match(model.name).group(1)
                tempid = model.modelid
                model.bodyid = parsedbodyid
                updateModel(tempid, model)
                print (model.name, model.bodyid)
            except:
                print (model.name)
        

def dbModelmanidParse():
    #for manufacter in getManufactures():
    modelslist = getModelsAll()
    countall = len(modelslist)
    i = 0
    for model in modelslist:
        p = re.compile('modification\.php\?manufacture=(\d*)&model=(\d*)')
        tempmanid = p.match(model.link).group(1)
        tempid = model.modelid
        model.modelmanid = tempmanid
        updateModel(tempid, model)
        i = i + 1
        print "{0}/{1}".format(countall,i)

dbBodyNameParse()