from flask import Flask, request, jsonify
import os
import random

app = Flask(__name__)

clases = ['Sano', 'Trips', 'Otro daño']

@app.route('/predecir', methods=['POST'])
def predecir():
    if 'imagen' not in request.files:
        return jsonify({'error': 'No se envió imagen'}), 400

    img_file = request.files['imagen']
    
    # Asegurar carpeta temp/imagenes
    folder = os.path.join("temp", "imagenes")
    os.makedirs(folder, exist_ok=True)
    
    img_path = os.path.join(folder, img_file.filename)
    img_file.save(img_path)

    # Simulación de predicción
    resultado = random.choice(clases)
    return jsonify({'prediccion': resultado})

@app.route('/')
def index():
    return "API de Monitoreo de Brócoli Activa"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
