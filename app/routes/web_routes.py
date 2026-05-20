from flask import Blueprint, render_template, request, redirect, url_for

web_bp = Blueprint('web', __name__)

# --- 1. PÁGINA PRINCIPAL ---
@web_bp.route('/')
def inicio():
    return render_template('inicio.html')

# --- 2. PÁGINA DE REPORTES ---
@web_bp.route('/muro')
def muro_reportes():
    # Aquí puedes hacer la consulta a tu base de datos y enviarla al HTML
    return render_template('muro_reportes.html')

# --- 3. PÁGINA PARA CREAR USUARIOS/CATEGORÍAS ---
@web_bp.route('/administracion')
def administracion():
    return render_template('administracion.html')