from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/verificar', methods=['POST'])
def verificar():
    datos = request.get_json()
    texto = datos.get("texto", "") if datos else ""

    # Aquí iría la lógica de verificación real
    resultado = {
        "texto": texto,
        "verificado": True,
        "mensaje": "Texto recibido correctamente"
    }

    return jsonify(resultado), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
