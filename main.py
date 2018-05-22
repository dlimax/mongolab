from pymongo import MongoClient
import config as cfg

client = MongoClient(cfg.MONGO_ADDR, cfg.MONGO_PORT)
db = client[cfg.MONGO_INSTANCE]
users = db.users  # coleção de usuários
questions = db.questions  # coleção de questões

def get_user(username):
    """
    obtem o usuário conforme o valor de :username
    """
    users.find_one({'username': username})
    return user

def authenticate(username, password):
    """ 
    autenticar um usuario conforme combinacao de parametros :username e :password.
    return True para autenticacao válida.
    """
    # 1. obter o usuario por username com collection.find_one() 
    # 2. caso exista, comparar o password do usuario obtido com bcrypt(password)
    # 3. retornar True ou False conforme resultado da comparação em 2.
    pass
    

def new_user(username, name, password):
    """
    cria um novo usuário, caso :username seja único na base de dados.
    """
    # 1. obter o usuario por username com collection.find_one()
    # 2. caso não exista, cria novo usuário e retorna True, caso contrário, apenas retorna False.
    pass


def get_question(question_id):
    """
    obtém a questao pelo :question_id
    """
    # 1. obter questao com collection.find_one() e retornar
    pass


def search_questions_by_disciplina(disciplinas):
    """
    realiza uma busca por questoes por disciplinas:
    retorna as questoes cuja disciplina esteja dentro da *lista* :disciplinas
    """
    pass


def new_comment(username, question_id, comment):
    """
    registra um comentário em uma questão
    """
    # 1. obter questao com collection.find_one()
    # 2. incluir comentario na questao recuperada. 
    # 3. atualizar questao com collection.set() utilizando operador $push caso não seja o primeiro comentário.
    pass


def answer_question(user_id, question_id, resposta):
    """
    responde uma questão de id :question_id com a resposta :resposta pelo usuario de id :user_id.
    persiste a resposta na colecao de usuarios.
    retorna True se a resposta for correta; False, caso contrário.
    """
    # 1. obter questao com collection.find_one()
    # 2. comparar a resposta da questao com :resposta    
    # 3. atualizar questao com collection.set() utilizando operador $push caso não seja o primeiro comentário.    
    pass


def get_questions_answereds_by_user(username):
    """
    retorna as questoes respondidas por um usuário
    """
    # 1. obter usuario com users.find() (usando colecao de questoes)
    # 2. separar os ids das questoes do usuario obtido em uma variavel do tipo lista.
    # 3. obter questoes com questions.find() utilizando o operador $in e o parametro a variabel criada em #2  (usando colecao de questoes)
    pass
    

def search_questions(temas, bancas, disciplinas, ano_min, ano_max):
    """
    realiza uma busca por questoes baseada nos criterios passados como parametros
    """
    pass
