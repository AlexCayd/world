from models import City, Country, CountryLanguage, SessionLocal
from sqlalchemy.sql import func, over

# Aqui definimos funciones para interactuar con la base de datos

# Cada vez que se haga una consulta 
# Debe hacerse abriendo y cerrando la sesión
# En un sistema pequeño no afectaría pero es buena práctica

def consulta_1():
     session = SessionLocal()
     try:
         resultados = session.query(Country.name, Country.gnp, Country.governmentForm).order_by(Country.gnp.asc()).filter(Country.gnp != None).filter(Country.gnp > 0 ).limit(10).all()  #Query con ORM
         return [
             {
                 "name": resultado[0],
                 "gnp": resultado[1],
                 "government_form": resultado[2]
             }
             for resultado in resultados
         ]# Devuelve una lista como diccionarios
     finally:
         session.close()

def consulta_2():
    session = SessionLocal()
    try:
        rankedCities = session.query(
            City.name,
            City.population,
            Country.name.label('country'),
            Country.continent,
            func.row_number().over(
                order_by=City.population.desc(),
                partition_by=Country.continent
            ).label('rank')
        ).join(Country, City.countryCode == Country.code).subquery()

        topCities = session.query(
            rankedCities.c.continent,
            rankedCities.c.name,
            rankedCities.c.population,
            rankedCities.c.country
        ).filter(
            rankedCities.c.rank <= 5
        ).order_by(
            rankedCities.c.continent,
            rankedCities.c.rank
        ).all()

        return [
            {
                "continent": topCity[0],
                "city": topCity[1],
                "population": topCity[2],
                "country": topCity[3]
            }
            for topCity in topCities
        ]
    finally:
        session.close()


def consulta_3():
    session = SessionLocal()
    try:
        resultados = (
            session.query(
                Country.name,
                Country.population, 
                func.sum(City.population)
            )
            .join(City, Country.code == City.countryCode)
            .group_by(Country.name)
            .order_by(func.sum(City.population).desc())
            .all()
        )

        return [
            {
                "country_name": resultado[0],
                "country_population": resultado[1],
                "total_city_population": resultado[2],
            }
            for resultado in resultados
        ]  
    finally:
        session.close()

def consulta_5() :
    session = SessionLocal()
    try:
        # Parámetro para altas poblaciones
        umbral_poblacion = 1000000  

        resultados = (
            session.query(
                Country.name.label("country_name"),
                func.count(CountryLanguage.language).label("language_count")
            )
            .join(City, Country.code == City.countryCode)  
            .join(CountryLanguage, Country.code == CountryLanguage.countryCode)  
            .filter(City.population > umbral_poblacion)  
            .group_by(Country.name)
            .order_by(func.count(CountryLanguage.language).desc())  
            .limit(15).all()
        )

        return [
            {
                "country_name": resultado.country_name,
                "language_count": resultado.language_count
            }
            for resultado in resultados
        ]
    finally:
        session.close()