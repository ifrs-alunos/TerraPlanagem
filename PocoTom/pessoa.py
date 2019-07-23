#coding: utf-8
class Pessoa():
	nome = ""
	endereco = ""
	cidade = ""
	bairro = ""
	estado = ""
	fone = int
	email = ""
	cpf = ""
	rg = ""

	def __init__(self, nome, endereco, cidade, bairro, estado, fone, email, cpf, rg):
		self.nome = nome
		self.endereco = endereco
		self.cidade = cidade
		self.bairro = bairro
		self.estado = estado
		self.fone = fone
		self.email = email
		self.cpf = cpf
		self.rg = rg
