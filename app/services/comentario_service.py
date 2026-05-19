from app.repositories.comentario_repository import ComentarioRepository
from app.database.models import Comentario

class ComentarioService:
    @staticmethod
    def agregar_comentario(contenido, reporte_id, usuario_id):
        if not contenido:
            raise ValueError("El comentario no puede estar vacío.")
            
        nuevo_comentario = Comentario(contenido=contenido, reporte_id=reporte_id, usuario_id=usuario_id)
        return ComentarioRepository.guardar(nuevo_comentario)

    @staticmethod
    def listar_por_reporte(reporte_id):
        comentarios = ComentarioRepository.obtener_por_reporte(reporte_id)
        return [{"id": c.id, "contenido": c.contenido, "autor": c.usuario.nombre, "fecha": c.fecha_creacion} for c in comentarios]