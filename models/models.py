
from app import db
from sqlalchemy import ForeignKey

# CREACION TABLA DEPARTAMENTO
class Departamento(db.Model):
    __tablename__ = 'Departamento'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=True, nullable=False)

    def __str__(self):
        return self.nombre

# CREACION TABLA PUESTO
class Puesto(db.Model):
    __tablename__ = 'Puesto'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=True, nullable=False)

    def __str__(self):
        return self.nombre

# CREACION TABLA EMPLEADO
class Empleado(db.Model):
    __tablename__ = 'Empleado'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(15))
    fecha_contratacion = db.Column(db.Date)
    departamento_id = db.Column(db.Integer, ForeignKey('Departamento.id'))
    puesto_id = db.Column(db.Integer, ForeignKey('Puesto.id'))

    departamento = db.relationship('Departamento')
    puesto = db.relationship('Puesto')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

