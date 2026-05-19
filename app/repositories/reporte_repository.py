from app.database.models import db, ReporteAmbiental

class ReporteRepository:
    
    @staticmethod
    def guardar(reporte: ReporteAmbiental) -> ReporteAmbiental:
        db.session.add(reporte)
        db.session.commit()
        return reporte

    @staticmethod
    def obtener_todos():
        return ReporteAmbiental.query.order_by(ReporteAmbiental.fecha_creacion.desc()).all()

    @staticmethod
    def obtener_por_id(reporte_id: int) -> ReporteAmbiental:
        return ReporteAmbiental.query.get(reporte_id)

    @staticmethod
    def obtener_por_estado(estado: str):
        """Filtra incidentes según su avance (ej. 'En Proceso')."""
        return ReporteAmbiental.query.filter_by(estado_actual=estado).order_by(ReporteAmbiental.fecha_creacion.desc()).all()