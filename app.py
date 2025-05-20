from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)

# Configuração do banco de dados PostgreSQL
conn = psycopg2.connect(
    host="dpg-d0m9iv0gjchc739mea2g-a",
    database="bd_codigos_alunos",
    user="bd_codigos_alunos_user",
    password="OOVhRqH8vZFM5rl3QAyiAyLI7nqnSKWl"
)
cur = conn.cursor()

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    nome = data.get("nome")
    email = data.get("email")
    senha = data.get("senha")
    try:
        cur.execute("INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)", (nome, email, senha))
        conn.commit()
        return jsonify({"mensagem": "Usuário registrado com sucesso"}), 200
    except Exception as e:
        conn.rollback()
        return jsonify({"detail": str(e)}), 400

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    senha = data.get("senha")
    cur.execute("SELECT * FROM usuarios WHERE email = %s AND senha = %s", (email, senha))
    user = cur.fetchone()
    if user:
        return jsonify({"mensagem": "Login bem-sucedido"}), 200
    else:
        return jsonify({"detail": "Credenciais inválidas"}), 401

@app.route("/enviar_codigo", methods=["POST"])
def enviar_codigo():
    data = request.get_json()
    codigo = data.get("codigo")
    resultado = "Código recebido com sucesso!" if codigo else "Nenhum código enviado."
    return jsonify({"resultado": resultado})

if __name__ == "__main__":
    app.run(debug=True)