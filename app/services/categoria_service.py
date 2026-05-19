from app.repositories.categoria_repository import CategoriaRepository
from app.database.models import Categoria

class CategoriaService:
    @staticmethod
    def crear_categoria(nombre, descripcion):
        if not nombre:
            raise ValueError("El nombre de la categoría es obligatorio.")
        
        nueva_categoria = Categoria(nombre=nombre, descripcion=descripcion)
        return CategoriaRepository.guardar(nueva_categoria)

    @staticmethod
    def listar_categorias():
        categorias = CategoriaRepository.obtener_todas()
        return [{"id": c.id, "nombre": c.nombre, "descripcion": c.descripcion} for c in categorias]