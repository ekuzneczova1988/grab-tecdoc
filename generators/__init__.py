from generators.bdnormilize import getManufactures, getModels, updateModel,\
    getModelsAll
import re

def dbBodyNameParse():
    for manufacture in getManufactures()
        

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
        