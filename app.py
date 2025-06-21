from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route('/')
def home():
    return "API de verificación conectada a OpenAI"

@app.route('/verificar', methods=['POST'])
def verificar():
    try:
        data = request.get_json()
        print("🟡 Datos recibidos en /verificar:", data)

        texto = data.get("texto", "") if data else ""

        if not texto:
            return jsonify({"error": "No se proporcionó texto para verificar"}), 400

        prompt = f"Dime si esta afirmación es falsa y explica por qué: {texto}"

        respuesta = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4,
            max_tokens=700
        )

        contenido = respuesta.choices[0].message.content
        tokens_usados = respuesta.usage.total_tokens

        return jsonify({
            "respuesta": contenido,
            "tokensSpent": tokens_usados
        })

    except Exception as e:
        print("❌ Error:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
