class AutomatoFinito:
	estados = set()
	transicoes = {}
	inicial: ''
	finais = set()

	def add_estado(self, estado):
		self.estados = self.estados.union((estado,))

	def set_estado_inicial(self, estado):
		if (estado in self.estados):
			self.inicial = estado

	def add_estados_finais(self, estado):
		if (estado in self.estados):
			self.finais = self.finais.union((estado,))

	def add_transicao(self, ei, ch, ef):
		if (ei in self.estados and ef in self.estados):
			if ((ei, ch) in self.transicoes.keys()):
				self.transicoes[(ei, ch)].append(ef)
			else:
				self.transicoes[(ei, ch)] = [ef]

	def check(self, palavra) -> bool:
		atual = self.inicial
		for ch in palavra:
			if ((atual, ch) in self.transicoes.keys()):
				atual = self.transicoes[(atual, ch)][0]
			else:
				return False
		if atual in self.finais:
			return True
		else:
			return False

	def alfabeto(self):
		lista = set()
		count = 0
		for x in self.transicoes.keys():
			lista = lista.union(set(x[1]))
			count = count + 1
		return lista

	def print(self):
		saida = ''
		nome = 'estado'
		alfabeto = self.alfabeto()
		temp = "-----------------"
		saida = saida + f'|{nome:15}|'
		for a in alfabeto:
			saida = saida + f'{a:15}|'
			temp = temp + "-----------------"
		saida = saida + '\n'
		saida = temp + "\n" + saida + temp + "\n"
		for e in self.estados:
			saida = saida + f'|{e:15}|'
			for a in alfabeto:
				est = ''
				if (e,a) in self.transicoes.keys():
					for t in self.transicoes[(e,a)]:
						est = est + t + ','
				else:
					est = '&'
				saida = saida + f'{est:15}|'
			saida = saida + '\n'
		return saida
