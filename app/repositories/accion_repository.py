from app.database.models import db, AccionSeguimiento

class AccionRepository:
    
    @staticmethod
    def guardar(accion: AccionSeguimiento) -> AccionSeguimiento:
        """Registra una acción de mitigación o limpieza."""
        db.session.add(accion)
        db.session.commit()
        return accion

    @staticmethod
    def obtener_por_reporte(reporte_id: int):
        """Lista el historial de acciones tomadas para resolver un reporte."""
        return AccionSeguimiento.query.filter_by(reporte_id=reporte_id).order_by(AccionSeguimiento.fecha_accion.desc()).all()