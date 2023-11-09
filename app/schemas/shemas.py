from app import ma
from marshmallow import fields


class DepartamentoSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    nombre = fields.String()


class PuestoSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    nombre = fields.String()


class EmpleadoBasicSchema(ma.Schema):
    nombre = fields.String()
    apellido = fields.String()
    email = fields.String()
    telefono = fields.String()


class EmpleadoSchema(EmpleadoBasicSchema):
    id = fields.Integer(dump_only=True)
    fecha_contratacion = fields.Date()
    departamento = fields.Nested(DepartamentoSchema, only=('id', 'nombre'))
    puesto = fields.Nested(PuestoSchema, only=('id', 'nombre'))
