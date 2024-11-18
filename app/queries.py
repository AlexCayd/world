from models import City, Country, CountryLanguage, SessionLocal
from sqlalchemy import func

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
            .limit(10)
            .all()
        )

        return [
            {
                "country_name": resultado[0],
                "country_population": resultado[1],
                "total_city_population": resultado[2],
            }
            for resultado in resultados
        ]  # Devuelve una lista de diccionarios
    finally:
        session.close()

