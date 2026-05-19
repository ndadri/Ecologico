from app import create_app

# Crea la instancia de la aplicación
app = create_app()

if __name__ == '__main__':
    # Arranca el servidor local en el puerto 5000
    # debug=True permite que el servidor se reinicie solo si haces cambios en el código
    app.run(debug=True, port=5000)