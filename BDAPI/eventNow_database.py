
class EventDatabase:
    def __init__(self, database):
        self.db = database

    # Autentifica Usuário
    def authenticate_user(self, email, senha):
        # Lógica de autenticação (substitua com sua própria lógica)
        query = "MATCH (u:usuario {mail: $email, senha: $senha}) RETURN u.nome AS nome, ID(u) AS user_id"
        parameters = {"email": email, "senha": senha}
        result = self.db.execute_query(query, parameters)
        # Verifique se a consulta retornou algum resultado
        if result:
            return result[0]  # Retorne as informações do usuário autenticado
        else:
            return None

    #Cria um usuário
    def create_usuario(self, nome, mail, senha):
        query = "CREATE(:usuario {nome: $nome, mail: $mail, senha: $senha})"
        parameters = {"nome": nome, "mail": mail, "senha": senha}
        self.db.execute_query(query, parameters)

    #Cria um administrador
    def create_administrador(self, nome, mail, senha):
        query = "CREATE(:administrador {nome: $nome, mail: $mail, senha: $senha})"
        parameters = {"nome": nome, "mail": mail, "senha": senha}
        self.db.execute_query(query, parameters)

    #Cria um evento
    def create_evento(self, nome, local, administrador):
        query = "CREATE(:evento {nome: $nome, local: $local, administrador: $administrador})"
        parameters = {"nome": nome, "local": local, "administrador": administrador}
        self.db.execute_query(query, parameters)

    #Coloca um adm no evento
    def insert_adm_event(self, nome_adm, nome_evento):
        query = "MATCH(a:administrador {nome: $nome_adm}), (e:evento {nome: $nome_evento}) CREATE(a)-[:ADMINISTRA]->(e);"
        parameters = {"nome_adm": nome_adm, "nome_evento": nome_evento}
        self.db.execute_query(query, parameters)

    #Cria uma relação de usuário com evento
    def insert_usuario_evento(self, usuario_nome, evento_nome):
        query = "MATCH(a:usuario {nome: $usuario_nome}) MATCH (b:evento {nome: $evento_nome}) CREATE (a)-[:PARTICIPA]->(b);"
        parameters = {"usuario_nome": usuario_nome, "evento_nome": evento_nome}
        self.db.execute_query(query, parameters)

    #Chama todas as relações no Neo4j
    def get_TotalDB(self):
        query = "MATCH (n) RETURN n"
        results = self.db.execute_query(query)
        return results

    #Busca por usuários
    def get_usuario(self):
        query = "MATCH (u:usuario) RETURN u.nome AS nome"
        results = self.db.execute_query(query)
        return [result["nome"] for result in results]

    def get_usuario_espec(self, nome_usuario):
        query = "MATCH (u:usuario {nome: $nome_usuario} RETURN u.nome"
        parameters = {"nome_usuario": nome_usuario}
        results = self.db.execute_query(query, parameters)
        return results

    #Busca por eventos
    def get_evento(self):
        query = "MATCH (e:evento) RETURN e.nome AS nome"
        results = self.db.execute_query(query)
        return [result["nome"] for result in results]

    #Busca usuários em um evento
    def get_users_in_event(self, nome_evento):
        query = "MATCH (u:usuario) -[:PARTICIPA]-> (e:evento {nome: $nome_evento}) RETURN u.nome AS nome"
        parameters = {"nome_evento": nome_evento}
        results = self.db.execute_query(query, parameters)
        return results

    #Busca todos os eventos que um usuário participa
    def get_all_events_by_user(self, nome_usuario):
        query = "MATCH (u:usuario {nome: $nome_usuario}) -[:PARTICIPA]-> (e:evento) RETURN e.nome AS nome"
        parameters = {"nome_usuario": nome_usuario}
        results = self.db.execute_query(query, parameters)
        return results

    #Busca todos os eventos que um ADM administra
    def getAdmEventos(self, nome_adm, nome_evento):
        query = "MATCH (a:administrador {nome: $nome_adm}) -[:ADMINISTRA]-> (e:evento {nome: $nome_evento})"
        parameters = {"nome_adm": nome_adm, "nome_evento": nome_evento}
        results = self.db.execute_query(query, parameters)
        return results

    #Deleta Usuario
    def delete_usuario(self, nome):
        query = "MATCH (u:usuario {nome: $nome}) DETACH DELETE u"
        parameters = {"nome": nome}
        self.db.execute_query(query, parameters)

    #Deleta Evento
    def delete_evento(self, nome):
        query = "MATCH (e:evento {nome: $nome}) DETACH DELETE e"
        parameters = {"nome": nome}
        self.db.execute_query(query, parameters)

    #Deleta Admin
    def delete_adm(self, nome):
        query = "MATCH (adm:administrador {nome: $nome}) DETACH DELETE adm"
        parameters = {"nome": nome}
        self.db.execute_query(query, parameters)