from flask import Flask, jsonify, request
from flask_cors import CORS

from database import Database
from eventNow_database import EventDatabase
import awsgi

import json

db = Database("bolt://44.203.246.65:7687", "neo4j", "rattle-primitives-admirals")
eventDB = EventDatabase(db)

app = Flask(__name__)

CORS(app)


@app.route('/')
def index():
    return jsonify(status=200, message='ok')


@app.route('/login', methods=['POST'])
def login():
    try:
        # Obtenha os dados enviados na solicitação POST
        dados = request.get_json()

        # Verifique se todos os campos necessários estão presentes
        if 'email' not in dados or 'senha' not in dados:
            return jsonify({'mensagem': 'Campos incompletos'}), 400

        # Obtenha as credenciais do usuário
        email = dados['email']
        senha = dados['senha']

        # Autentique o usuário
        user_id = eventDB.authenticate_user(email, senha)

        if (user_id != None):
            # Usuário autenticado com sucesso
            return jsonify({'mensagem': 'Login bem-sucedido', 'user_id': user_id})
        else:
            # Credenciais inválidas
            return jsonify({'mensagem': 'Credenciais inválidas', 'user_id': user_id}), 401

    except Exception as e:
        return jsonify({'mensagem': 'Erro ao processar solicitação', 'error': str(e)}), 500


@app.route('/add-user-event', methods=['POST'])
def add_user_event():
    try:
        # Obtenha os dados enviados na solicitação POST
        dados = request.get_json()

        if isinstance(dados, list):
            # Itere sobre a lista de usuários e crie cada um no Neo4j
            for usuario in dados:
                eventDB.insert_usuario_evento(usuario['usuario'], usuario['evento'])
        elif isinstance(dados, dict):
            # Se for um dicionário, crie um único usuário
            eventDB.insert_usuario_evento(dados['usuario'], dados['evento'])
        else:
            # Se não for uma lista ou dicionário, retorne um erro
            return jsonify({'mensagem': 'Formato de dados inválido'}), 400

        return jsonify({'mensagem': 'Usuário inserido com sucesso no evento'})

    except Exception as e:
        return jsonify({'mensagem': 'Erro ao processar solicitação', 'error': str(e)}), 500


# Exemplo de rota GET para obter usuários
@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    try:
        # Use o método get_usuarios da classe UserDB para obter usuários
        usuarios = eventDB.get_usuario

        # Converte a lista de objetos User em um formato JSON
        usuarios_json = [{'nome': usuario.nome, 'email': usuario.email} for usuario in usuarios]

        return jsonify({'usuarios': usuarios_json})

    except Exception as e:
        return jsonify({'mensagem': 'Erro ao obter usuários', 'error': str(e)}), 500


# Exemplo de rota GET para obter eventos
@app.route('/eventos', methods=['GET'])
def get_eventos():
    try:
        # Use o método get_eventos da classe EventDB para obter eventos
        eventos = eventDB.get_evento()

        # Converte a lista de objetos Event em um formato JSON
        eventos_json = [{'nome': evento.nome, 'local': evento.local, 'administrador': evento.administrador} for evento
                        in eventos]

        return jsonify({'eventos': eventos_json})

    except Exception as e:
        return jsonify({'mensagem': 'Erro ao obter eventos', 'error': str(e)}), 500


# Exemplo de função para o endpoint /delete_usuario
@app.route('/delete_usuario/<string:nome>', methods=['DELETE'])
def delete_user_endpoint(nome):
    try:

        # Chame a função para deletar o usuário no Neo4j
        eventDB.delete_usuario(nome)

        return jsonify({'mensagem': 'Usuário removido com sucesso'})

    except Exception as e:
        return jsonify({'mensagem': 'Erro ao processar solicitação', 'error': str(e)}), 500


@app.route('/delete_usuario/<string:nome>', methods=['DELETE'])
def delete_evento_endpoint(nome):
    try:

        # Chame a função para deletar o usuário no Neo4j
        eventDB.delete_evento(nome)

        return jsonify({'mensagem': 'Usuário removido com sucesso'})

    except Exception as e:
        return jsonify({'mensagem': 'Erro ao processar solicitação', 'error': str(e)}), 500


@app.route('/cadastroevento', methods=['POST'])
def cadastroevento():
    try:
        # Obtenha os dados enviados na solicitação POST
        dados = request.get_json()

        if isinstance(dados, list):
            # Itere sobre a lista de usuários e crie cada um no Neo4j
            for usuario in dados:
                eventDB.create_evento(usuario['nome'], usuario['local'], usuario['administrador'])
        elif isinstance(dados, dict):
            # Se for um dicionário, crie um único usuário
            eventDB.create_evento(dados['nome'], dados['local'], dados['administrador'])
        else:
            # Se não for uma lista ou dicionário, retorne um erro
            return jsonify({'mensagem': 'Formato de dados inválido'}), 400

        return jsonify({'mensagem': 'sucesso'})

    except Exception as e:
        return jsonify({'mensagem': 'Erro ao receber dados', 'error': str(e)}), 500


@app.route('/cadastro', methods=['POST'])
def post_data():
    try:
        # Obtenha os dados enviados na solicitação POST
        dados = request.get_json()

        if isinstance(dados, list):
            # Itere sobre a lista de usuários e crie cada um no Neo4j
            for usuario in dados:
                eventDB.create_usuario(usuario['nome'], usuario['email'], usuario['senha'])
        elif isinstance(dados, dict):
            # Se for um dicionário, crie um único usuário
            eventDB.create_usuario(dados['nome'], dados['email'], dados['senha'])
        else:
            # Se não for uma lista ou dicionário, retorne um erro
            return jsonify({'mensagem': 'Formato de dados inválido'}), 400

        return jsonify({'mensagem': 'sucesso'})

    except Exception as e:
        return jsonify({'mensagem': 'Erro ao receber dados', 'error': str(e)}), 500


#Lambda Function para Subir para o AWS
def lambda_handler(event, context):
    return awsgi.response(app, event, context, base64_content_types={"image/png"})


#Para Rodar localmente
app.run(port=5000, host='localhost', debug=True)