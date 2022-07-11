from . import app

@app.route('/')
def home():
    return "Homepage"

@app.route('/nuevo', methods=['GET', 'POST'])
def nuevo():
    return "crear movimiento"

@app.route('/modificar')
def actualizar():
    return "actualizar movimiento"

@app.route('/borrar', methods=['GET', 'POST'])
def eliminar():
    return "eliminar movimiento"