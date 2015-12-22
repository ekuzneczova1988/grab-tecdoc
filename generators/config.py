# -*- coding: utf-8 -*-
"""
Configs for default spider
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from models import Base

def init_engine():
    db_engine = create_engine(
        'sqlite+pysqlite:///../data.sqlite', encoding='utf-8')
    Base.metadata.create_all(db_engine)  # @UndefinedVariable
    return db_engine

    
db_engine = init_engine()
Session = sessionmaker(bind=db_engine)