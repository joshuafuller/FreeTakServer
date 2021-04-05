#######################################################
# 
# Color.py
# Python implementation of the Class Color
# Generated by Enterprise Architect
# Created on:      26-Sep-2020 9:41:35 PM
# Original author: natha
# 
#######################################################
from sqlalchemy import Column, ForeignKey
from FreeTAKServer.model.SQLAlchemy.Root import Base
from sqlalchemy import String


class Color(Base):
# default constructor  def __init__(self):  
    __tablename__ = "Color"
    PrimaryKey = Column(ForeignKey("Detail.PrimaryKey"), primary_key=True)
    argb = Column(String(100))