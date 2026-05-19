from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    rol = db.Column(db.String(50), default='ciudadano') # ciudadano, voluntario, administrador
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relaciones (para acceder a los datos desde el objeto en Python)
    reportes = db.relationship('ReporteAmbiental', backref='autor', lazy=True)
    comentarios = db.relationship('Comentario', backref='usuario', lazy=True)
    acciones = db.relationship('AccionSeguimiento', backref='responsable', lazy=True)


class Categoria(db.Model):
    __tablename__ = 'categorias'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), unique=True, nullable=False) # Ej: "Reciclaje", "Fuga de Agua"
    descripcion = db.Column(db.String(255), nullable=True)
    
    reportes = db.relationship('ReporteAmbiental', backref='categoria', lazy=True)


class ReporteAmbiental(db.Model):
    __tablename__ = 'reportes'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(150), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    ruta_imagen = db.Column(db.String(255), nullable=False)
    estado_actual = db.Column(db.String(50), default='Pendiente') # Pendiente, En Proceso, Solucionado
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Llaves Foráneas (Claves externas)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)
    
    # Relaciones
    comentarios = db.relationship('Comentario', backref='reporte', lazy=True)
    acciones = db.relationship('AccionSeguimiento', backref='reporte', lazy=True)


class Comentario(db.Model):
    __tablename__ = 'comentarios'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    contenido = db.Column(db.Text, nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Llaves Foráneas
    reporte_id = db.Column(db.Integer, db.ForeignKey('reportes.id'), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)


class AccionSeguimiento(db.Model):
    __tablename__ = 'acciones_seguimiento'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    detalle_accion = db.Column(db.Text, nullable=False) # Ej: "Se recolectaron 20kg de plástico"
    fecha_accion = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Llaves Foráneas
    reporte_id = db.Column(db.Integer, db.ForeignKey('reportes.id'), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False) # Quién ejecutó la acción