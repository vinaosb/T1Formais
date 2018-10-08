class GramaticaRegular:
	variaveis = set()
	transicoes = {}
	inicial: ''

	def __init__(self):
		self.variaveis = set()
		self.transicoes = {}
		self.inicial = ''

	def add_variavel(self, variavel):
		self.variaveis = self.variaveis.union((variavel,))

	def set_variavel_inicial(self, variavel):
		if variavel in self.variaveis:
			self.inicial = variavel

	def add_regras(self, v1, t, v2):
		if (v1 in self.variaveis):
			if (v1 not in self.transicoes.keys()):
				self.transicoes[v1] = [(t, v2)]
			else:
				if((t, v2) not in self.transicoes[v1]):
					self.transicoes[v1].append((t, v2))	

	def print(self):
		saida = ''
		for v in self.variaveis:
			if v == self.inicial:
				saida = saida + '->'
			saida = saida + '(' + v + ') -> '
			for prod in self.transicoes[v]:
				if prod[1] != '&':
					saida = saida + prod[0] + '(' +prod[1] + ') | '
				else:
					saida = saida + prod[0] + ' | '
			saida = saida[:-2] + '\n'
		return saida

	def alfabeto(self):
		lista = set()
		for v in self.variaveis:
			for prod in self.transicoes[v]:
				lista = lista.union(prod[0])
		return lista