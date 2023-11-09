#IMPORTS NATIVOS DE PYTHON.
import os
from datetime import datetime, timedelta

#IMPORTS NATIVOS DEL FRAMEWORK
from flask import (
    render_template, 
    redirect, 
    request, 
    url_for, 
    jsonify
)
from flask_jwt_extended import ( 
    jwt_required, 
    create_access_token, 
    get_jwt_identity, 
    get_jwt)
from werkzeug.security import( 
    generate_password_hash, 
    check_password_hash
)
#IMPORTS PROPIOS
from app import app, db, jwt
from app.models.models import *
from app.schemas.shema import (
    EmpleadoSchema,
    PaisSchema,
    ProvinciaSchema,
    LocalidadSchema
)

@app.route("/empleados")
@jwt_required()
def get_all_empleados():
    # Obtener información adicional del token
    additional_info = get_jwt()
    
    # Obtener todos los empleados paginados
    page = request.args.get('page', 1, type=int)
    can = request.args.get('can', 1000, type=int)
    empleados = db.session.query(Empleado).paginate(
        page=page, per_page=can
    )
    
    if additional_info['is_admin']:
        return jsonify(
            {
                "results": EmpleadoSchema().dump(
                    empleados.items, many=True
                ),
                "next": url_for(
                    'get_all_empleados', page=empleados.next_num
                ) if empleados.has_next else None,
                "prev": url_for(
                    'get_all_empleados', page=empleados.prev_num
                ) if empleados.has_prev else None
            }
        )
        
    return jsonify(
        {
            "results": EmpleadoSchema().dump(empleados.items, many=True)
        }
    )

@app.route("/paises")
def get_all_paises():
    paises = Pais.query.all()
    paises_schema = PaisSchema().dump(paises, many=True)
    return jsonify(paises_schema)

@app.route("/provincias")
def get_all_provincias():
    provincias = Provincia.query.all()
    provincias_schema = ProvinciaSchema().dump(provincias, many=True)
    return jsonify(provincias_schema)

@app.route("/localidades")
def get_all_localidades():
    localidades = Localidad.query.all()
    localidades_schema = LocalidadSchema().dump(localidades, many=True)
    return jsonify(localidades_schema)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agregar_empleado', methods=['POST'])
def nuevo_empleado():
    if request.method == 'POST':
        # Obtener datos del formulario o JSON
        data = request.form if request.form else request.get_json()

        # Crear objeto Empleado
        nuevo_empleado = EmpleadoSchema().load(data)

        # Guardar en la base de datos
        db.session.add(nuevo_empleado)
        db.session.commit()

        return redirect(url_for('index'))

@app.route('/borrar_empleado/<id>')
def borrar_empleado(id):
    empleado = Empleado.query.get(id)
    db.session.delete(empleado)
    db.session.commit()
    return redirect(url_for('index'))
