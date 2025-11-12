
from db import db

class Mascota(db.Model):

    # Nombre de tabla

    __tablename__="mascota"
    # Conjunto de atributos que van a ser los campos de la tabla
    # Llave primaria 
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(50))
    raza=db.Column(db.String(20))
    edad=db.Column(db.String(10))
    género=db.Column(db.String(20))
    cuidador=db.Column(db.String(50))
    telefono=db.Column(db.String(30))
    comentarios=db.Column(db.String(100))

    # Método constructor para mapear datos a los campos definidos
    def __init__ (self, nombre, raza, edad, género, cuidador, telefono, comentarios):

        self.nombre=nombre
        self.raza=raza
        self.edad=edad
        self.género=género
        self.cuidador=cuidador
        self.telefono=telefono
        self.comentarios=comentarios