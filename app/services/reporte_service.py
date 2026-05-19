import os
from werkzeug.utils import secure_filename
from app.repositories.reporte_repository import ReporteRepository
from app.database.models import ReporteAmbiental

class ReporteService:
    UPLOAD_FOLDER = 'app/static/uploads'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

    @classmethod
    def _archivo_permitido(cls, filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in cls.ALLOWED_EXTENSIONS

    @classmethod
    def crear_reporte(cls, titulo, descripcion, archivo, usuario_id, categoria_id):
        if not titulo or not usuario_id or not categoria_id:
            raise ValueError("Faltan campos obligatorios.")
        
        if not archivo or archivo.filename == '':
            raise ValueError("Debes subir una imagen.")

        if not cls._archivo_permitido(archivo.filename):
            raise ValueError("Formato de imagen no permitido.")

        nombre_seguro = secure_filename(archivo.filename)
        ruta_fisica = os.path.join(cls.UPLOAD_FOLDER, nombre_seguro)
        archivo.save(ruta_fisica)

        ruta_bd = f'/static/uploads/{nombre_seguro}'

        nuevo_reporte = ReporteAmbiental(
            titulo=titulo,
            descripcion=descripcion,
            ruta_imagen=ruta_bd,
            usuario_id=usuario_id,
            categoria_id=categoria_id
        )

        return ReporteRepository.guardar(nuevo_reporte)

    @staticmethod
    def listar_reportes():
        reportes = ReporteRepository.obtener_todos()
        return [{
            "id": r.id, 
            "titulo": r.titulo, 
            "estado": r.estado_actual,
            "autor": r.autor.nombre, # Usando la relación definida en el modelo
            "categoria": r.categoria.nombre
        } for r in reportes]
        
    @staticmethod
    def actualizar_estado(reporte_id, nuevo_estado):
        reporte = ReporteRepository.obtener_por_id(reporte_id)
        if not reporte:
            raise ValueError("Reporte no encontrado.")
        reporte.estado_actual = nuevo_estado
        return ReporteRepository.guardar(reporte)