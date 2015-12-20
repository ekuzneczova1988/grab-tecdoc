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
    __tablename__ = 'manufacture'

    sqlite_autoincrement = True
    id = Column(Integer, primary_key=True)

    name = Column(String(160))
    link = Column(String(160))
    manid = Column(Integer)

    last_update = Column(DateTime, default=datetime.datetime.now)

