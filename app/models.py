from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine
import pymysql
from sqlalchemy.orm import sessionmaker
import config

engine = create_engine(config.DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

class City(Base):
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    countryCode = Column(String, ForeignKey('country.code'), nullable=False)
    district = Column(String)
    population = Column(Integer)

class Country(Base):
    __tablename__ = 'country'
    code = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    continent = Column(String)
    region = Column(String)
    surfaceArea = Column(Float)
    indepYear = Column(Integer)
    population = Column(Integer)
    lifeExpectancy = Column(Float)
    gnp = Column(Float)
    gnpOld = Column(Float)
    localName = Column(String)
    governmentForm = Column(String)
    headOfState = Column(String)
    capital = Column(Integer, ForeignKey('city.id'))
    code2 = Column(String)

class CountryLanguage(Base):
    __tablename__ = 'countrylanguage'
    language = Column(String, primary_key=True)
    countryCode = Column(String, ForeignKey('country.code'), primary_key=True)
    isOfficial = Column(Boolean)
    percentage = Column(Float)
