from app.database.models import db, Categoria

class CategoriaRepository:
    
    @staticmethod
    def guardar(categoria: Categoria) -> Categoria:
        """Añade una nueva categoría ambiental (ej. Deforestación)."""
        db.session.add(categoria)
        db.session.commit()
        return categoria

    @staticmethod
    def obtener_por_id(categoria_id: int) -> Categoria:
        return Categoria.query.get(categoria_id)

    @staticmethod
    def obtener_todas():
        """Retorna la lista de todas las categorías disponibles."""
        return Categoria.query.order_by(Categoria.nombre.asc()).all()