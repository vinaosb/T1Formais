class GramaticaRegular:
	variaveis = set()
	transicoes = {}
	inicial: ''
	finais = set()

	def add_variavel(self, variavel):
		self.variaveis = self.variaveis.union((variavel,))

	def set_variavel_inicial(self, variavel):
		if variavel in self.variaveis:
			self.inicial = variavel

	def add_regras(self, v, t):
		self.add_regras(v, t, '&')

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
			for prod in self.transicoes[v]:
				if prod[1] != '&':
					saida = saida + v + ' -> ' + prod[0] + prod[1] + '\n'
				else:
					saida = saida + v + ' -> ' + prod[0] + '\n'
		return saida

	def alfabeto(self):
		lista = set()
		for v in self.variaveis:
			for prod in self.transicoes[v]:
				lista = lista.union(prod[0])
		return lista