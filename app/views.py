# Aquí definimos todas las rutas a partir de nuestras vistas
from flask import Flask, render_template
import queries

def register_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/about')
    def about():
        return render_template('index.html')

    @app.route('/consulta_1')
    def consulta_1():
        q_1 = queries.consulta_1() # Llamar a la función importada de queries
        return render_template('consulta_1.html', consulta_1 = q_1) # Mandar datos de la consulta a Jinja2 

    @app.route('/consulta_2')
    def consulta_2():
        q_2 = queries.consulta_2()
        return render_template('consulta_2.html', consulta_2 = q_2)

    @app.route('/consulta_3')
    def consulta_3():
        q_3 = queries.consulta_3()
        return render_template('consulta_3.html', consulta_3 = q_3)
        
    @app.route('/consulta_4')
    def consulta_4():
        q_4 = queries.consulta_4()
        return render_template('consulta_4.html', consulta_4 = q_4)

    @app.route('/consulta_5')
    def consulta_5():
        q_5 = queries.consulta_5()
        return render_template('consulta_5.html', consulta_5 = q_5)
      

