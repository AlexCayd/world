from models import City, Country, CountryLanguage, SessionLocal

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