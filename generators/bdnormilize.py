from models import Manufacture, Model
from config import Session

def getManufactures():
    session = Session()
    return session.query(Manufacture).all()

def getManufacture(uid):
    session = Session()
    return session.query(Manufacture).filter_by(manid=uid).first()

def getModels(uid):
    session = Session()
    return session.query(Model).filter_by(modelmanid=uid).all()

def getModelsAll():
    session = Session()
    return session.query(Model).all()

def getModel(uid):
    session = Session()
    return session.query(Model).filter_by(modelid=uid).first()

def updateModel(model, update):
        session = Session()
        try:
            tempmodel = session.query(Model).filter_by(modelid=model).first()
            tempmodel.modelmanid = update.modelmanid
            tempmodel.bodyid = update.bodyid
            session.commit()
            print "Commit ok {0}".format(model)
        except:
            session.rollback()
            print "Rollback"
            raise
    