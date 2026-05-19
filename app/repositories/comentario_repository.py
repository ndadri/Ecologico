from app.database.models import db, Comentario

class ComentarioRepository:
    
    @staticmethod
    def guardar(comentario: Comentario) -> Comentario:
        """Inserta un nuevo comentario asociado a un reporte."""
        db.session.add(comentario)
        db.session.commit()
        return comentario

    @staticmethod
    def obtener_por_reporte(reporte_id: int):
        """Recupera todos los comentarios de un reporte específico, ordenados por fecha."""
        return Comentario.query.filter_by(reporte_id=reporte_id).order_by(Comentario.fecha_creacion.asc()).all()