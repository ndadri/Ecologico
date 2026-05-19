from app.database.models import db, Usuario

class UsuarioRepository:
    
    @staticmethod
    def guardar(usuario: Usuario) -> Usuario:
        """Guarda o actualiza un usuario en la base de datos."""
        db.session.add(usuario)
        db.session.commit()
        return usuario

    @staticmethod
    def obtener_por_id(usuario_id: int) -> Usuario:
        """Busca un usuario por su llave primaria."""
        return Usuario.query.get(usuario_id)

    @staticmethod
    def obtener_por_email(email: str) -> Usuario:
        """Busca un usuario por su correo electrónico (útil para validaciones)."""
        return Usuario.query.filter_by(email=email).first()

    @staticmethod
    def obtener_todos():
        """Lista todos los usuarios registrados."""
        return Usuario.query.all()