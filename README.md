
# mongolab
Atividades para experimentação do MongoDB com python.

## Pré-requisitos

1. Instalar python (gerenciador de pacotes): https://python.org. Caso esteja utilizando Windows, instalar como Administrador e marcar as duas opções conforme a imagem: https://djangobook.com/wp-content/uploads/figure1_1a.png. 
2. Instale o `pymongo` (driver de mongo para o python). Execute no prompt de comando: `python -m pip install pymongo`
3. Criar conta, instancia de base de dados e usuário em https://mlab.com.
4. Criar coleção `questions` e importar nesta coleção o arquivo -> https://goo.gl/AafJqP.
5. Vamos agora testar a conexão com a conta no mlab com o pymongo: 
```python
connection = pymongo.MongoClient(ab123456.mlab.com, 123456)
db = connection[nome_instancia]
db.authenticate(database_user, database_pass)


```

