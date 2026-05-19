from flask import Blueprint, request, jsonify
from app.services.reporte_service import ReporteService
from app.services.comentario_service import ComentarioService

reporte_bp = Blueprint('reportes', __name__)

# --- CRUD REPORTES ---
@reporte_bp.route('/api/reportes', methods=['POST'])
def registrar_reporte():
    try:
        titulo = request.form.get('titulo')
        descripcion = request.form.get('descripcion')
        usuario_id = request.form.get('usuario_id')
        categoria_id = request.form.get('categoria_id')
        archivo = request.files.get('imagen')

        reporte = ReporteService.crear_reporte(titulo, descripcion, archivo, usuario_id, categoria_id)
        return jsonify({"status": "success", "id": reporte.id}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@reporte_bp.route('/api/reportes', methods=['GET'])
def obtener_reportes():
    return jsonify(ReporteService.listar_reportes())

@reporte_bp.route('/api/reportes/<int:id>/estado', methods=['PATCH'])
def cambiar_estado(id):
    try:
        estado = request.json.get('estado')
        ReporteService.actualizar_estado(id, estado)
        return jsonify({"status": "Estado actualizado"})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

# --- CRUD COMENTARIOS ---
@reporte_bp.route('/api/reportes/<int:id>/comentarios', methods=['POST'])
def agregar_comentario(id):
    try:
        datos = request.json
        comentario = ComentarioService.agregar_comentario(datos.get('contenido'), id, datos.get('usuario_id'))
        return jsonify({"status": "success", "id": comentario.id}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@reporte_bp.route('/api/reportes/<int:id>/comentarios', methods=['GET'])
def listar_comentarios(id):
    return jsonify(ComentarioService.listar_por_reporte(id))