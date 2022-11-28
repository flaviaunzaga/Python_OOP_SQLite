from model.Pessoa import Pessoa
from database.Database import Database
from dao.PessoaDAO import PessoaDAO

unzaga = Pessoa(1,"Flavia Unzaga")
print(unzaga)

print(unzaga.nome)

db = Database()

pessoaDAO = PessoaDAO(db.conexao, db.cursor)

pessoas = pessoaDAO.getAll(orderBy=True)
for pessoa in pessoas:
  print(pessoa)

novo = Pessoa(0, "Nicole Tobias")

novo = pessoaDAO.save(novo)

pessoas = pessoaDAO.getAll(orderBy=True)
for pessoa in pessoas:
  print(pessoa)