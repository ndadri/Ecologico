from app.repositories.usuario_repository import UsuarioRepository
from app.database.models import Usuario

class UsuarioService:
    @staticmethod
    def crear_usuario(nombre, email, rol='ciudadano'):
        if not nombre or not email:
            raise ValueError("Nombre y email son obligatorios.")
        
        if UsuarioRepository.obtener_por_email(email):
            raise ValueError("El correo electrónico ya está registrado.")
            
        nuevo_usuario = Usuario(nombre=nombre, email=email, rol=rol)
        return UsuarioRepository.guardar(nuevo_usuario)

    @staticmethod
    def obtener_todos():
        usuarios = UsuarioRepository.obtener_todos()
        return [{"id": u.id, "nombre": u.nombre, "email": u.email, "rol": u.rol} for u in usuarios]