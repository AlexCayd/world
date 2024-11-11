from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class City(Base):
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    country_code = Column(String, ForeignKey('country.code'), nullable=False)
    district = Column(String)
    population = Column(Integer)

class Country(Base):
    __tablename__ = 'country'
    code = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    continent = Column(String)
    region = Column(String)
    surface_area = Column(Float)
    independence_year = Column(Integer)
    population = Column(Integer)
    life_expectancy = Column(Float)
    gnp = Column(Float)
    gnp_old = Column(Float)
    local_name = Column(String)
    government_form = Column(String)
    head_of_state = Column(String)
    capital = Column(Integer, ForeignKey('city.id'))
    code2 = Column(String)

class CountryLanguage(Base):
    __tablename__ = 'countrylanguage'
    language = Column(String, primary_key=True)
    country_code = Column(String, ForeignKey('country.code'), primary_key=True)
    is_official = Column(Boolean)
    percentage = Column(Float)
