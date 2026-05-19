from flask import Blueprint, request, jsonify
from app.services.usuario_service import UsuarioService
from app.services.categoria_service import CategoriaService

base_bp = Blueprint('base', __name__)

# --- CRUD USUARIOS ---
@base_bp.route('/api/usuarios', methods=['POST'])
def registrar_usuario():
    try:
        datos = request.json
        usuario = UsuarioService.crear_usuario(datos.get('nombre'), datos.get('email'), datos.get('rol', 'ciudadano'))
        return jsonify({"status": "success", "id": usuario.id}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@base_bp.route('/api/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify(UsuarioService.obtener_todos())

# --- CRUD CATEGORÍAS ---
@base_bp.route('/api/categorias', methods=['POST'])
def crear_categoria():
    try:
        datos = request.json
        categoria = CategoriaService.crear_categoria(datos.get('nombre'), datos.get('descripcion'))
        return jsonify({"status": "success", "id": categoria.id}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@base_bp.route('/api/categorias', methods=['GET'])
def listar_categorias():
    return jsonify(CategoriaService.listar_categorias())