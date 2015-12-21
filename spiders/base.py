# -*- coding: utf-8 -*-
from grab.spider import Spider

from models import Manufacture, Model, BodyDictionary, Modification
from config import Session, SAVE_TO_DB


class BaseHubSpider(Spider):
    initial_urls = ['http://tecdoc.autodoc.ru']

    items_total = 0

    def saveManufacture(self, data):
        if not SAVE_TO_DB:
            return #parse_manufactures
            
        session = Session()

        if not session.query(Manufacture).filter_by(manid=data['manid']).first():
            obj = Manufacture(**data)
            session.add(obj)
        session.commit()
        
    def saveModel(self, data):
        if not SAVE_TO_DB:
            return
            
        session = Session()

        if not session.query(Model).filter_by(modelid=data['modelid']).first():
            obj = Model(**data)
            session.add(obj)
        session.commit()
        
    def saveBodyDictionary(self, data):
        if not SAVE_TO_DB:
            return
            #parse_manufactures
        session = Session()

        if not (session.query(BodyDictionary).filter_by(name=data['name']).first()&session.query(BodyDictionary).filter_by(modelid=data['modelid']).first()):
            obj = BodyDictionary(**data)
            session.add(obj)
        session.commit()
        
    def saveModification(self, data):
        if not SAVE_TO_DB:
            return
            
        session = Session()

        if not session.query(Modification).filter_by(cardid=data['cardid']).first():
            obj = Modification(**data)
            session.add(obj)
        session.commit()

    def log_progress(self, str):  # @DontTrace @ReservedAssignment
        self.items_total += 1
        print "(%d) Item scraped: %s" % (self.items_total, str)