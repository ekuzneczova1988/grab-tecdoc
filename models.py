# -*- coding: utf-8 -*-
"""
Models for default project
"""
import datetime

from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column, Integer, Text, String, ForeignKey,
                        DateTime, PickleType, Table)

Base = declarative_base()

    
class Manufacture(Base):
    __tablename__ = 'manufactures'

    sqlite_autoincrement = True
    id = Column(Integer, primary_key=True)

    name = Column(String(160))
    link = Column(String(160))
    manid = Column(Integer)

    last_update = Column(DateTime, default=datetime.datetime.now)

class Model(Base):
    __tablename__ = 'models'

    sqlite_autoincrement = True
    id = Column(Integer, primary_key=True)

    name = Column(String(160))
    link = Column(String(160))
    bodyid = Column(Integer)
    startman = Column(String(100))
    stopman = Column(String(100))
    modelid = Column(Integer)
    manid = Column(Integer)

    last_update = Column(DateTime, default=datetime.datetime.now)
    
class BodyDictionary(Base):
    __tablename__ = 'bodydictionaries'

    sqlite_autoincrement = True
    id = Column(Integer, primary_key=True)

    name = Column(String(160))
    modelid = Column(String(160))

    last_update = Column(DateTime, default=datetime.datetime.now) 
    
class Modification(Base):
    __tablename__ = 'modifications'

    sqlite_autoincrement = True
    id = Column(Integer, primary_key=True)

    name = Column(String(160))
    productionyear = Column(String(160))
    kw = Column(Integer)
    hp = Column(Integer)
    volume = Column(Integer)
    type = Column(String(160))
    link = Column(String(160))
    modelid = Column(Integer)
    cardid = Column(Integer)

    last_update = Column(DateTime, default=datetime.datetime.now) 