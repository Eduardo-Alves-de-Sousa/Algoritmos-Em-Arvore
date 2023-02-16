class No:
	def __init__(self, valor):
		self.valor = valor
		self.esquerda = None
		self.direita = None

	def obtervalor(self):
		return self.valor

	def setesquerda(self, esquerda):
		self.esquerda = esquerda

	def setdireita(self, direita):
		self.direita = direita

	def obteresquerda(self):
		return self.esquerda

	def obterdireita(self):
		return self.direita

#Criação da Árvore Binaria de Busca
class ArvoreBinariaBusca:

	def __init__(self):
		self.raiz = None

	def obterraiz(self):
		return self.raiz
    #Inserir elementos na árvore binaria de busca
	def insere(self, valor):
		no = No(valor)
		if self.raiz == None:
			self.raiz = no
		else:
			no_pai = None
			no_atual = self.raiz
			while True:
				if no_atual != None:
					no_pai = no_atual
					if no.obtervalor() < no_atual.obtervalor():
						no_atual = no_atual.obteresquerda()
					else:
						no_atual = no_atual.obterdireita()
				else:
					if no.obtervalor() < no_pai.obtervalor():
						no_pai.setesquerda(no)
					else:
						no_pai.setdireita(no)
					break
    #Mostrar árvore em percursso de ordem simétrica 
    #Ou seja percorer nossa árvore em ordem simétrica               
	def mostraarvore(self, no_atual): 
		if no_atual != None:
			self.mostraarvore(no_atual.obteresquerda())
			print(f'{no_atual.obtervalor()}', end=' ')
			self.mostraarvore(no_atual.obterdireita())


t = ArvoreBinariaBusca()
#{8,3,6,10,14,1,7,13,4}
t.insere(8)
t.insere(3)
t.insere(6)
t.insere(10)
t.insere(14)
t.insere(1)
t.insere(7)
t.insere(13)
t.insere(4)

t.mostraarvore(t.obterraiz())

"""         8
          /   \
         3     10
       /  \       \
      1    6       14
          /  \    /
         4    7  13 """