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
		else:
			print('estado ', estado , ' nao existe')

	def add_estados_finais(self, estado):
		if (estado in self.estados):
			self.finais = self.finais.union((estado,))
		else:
			print('estado ', estado , ' nao existe'))

	def add_transicao(self, ei, ch, ef):
		if (ei in self.estados and ef in self.estados):
			if ((ei, ch) in self.transicoes.keys()):
				self.transicoes[(ei, ch)].append(ef)
			else:
				self.transicoes[(ei, ch)] = [ef]
		else:
			print('estado nao existe')

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
		lista = lista - set('&')
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

	def to_afd(self):
		afd = AutomatoFinito()
		for e in self.estados:
			estados_extras = set()
			if (e, '&') in self.transacoes.keys():
				for t in self.transicoes[(e, a)]
					estados_extras = estados_extras.union((t,))
			for a in self.alfabeto():
				if ((e, a) in self.transicoes.keys()):
					afd.add_estado(e)
					if e == inicial:
						afd.set_estado_inicial(e)
					if (self.transicoes[(e, a)] > 1):
						novo_estado = estados_extras
						final = False
						for t in self.transicoes[(e, a)]
							novo_estado = novo_estado.union((t,))
							if t in finais:
								final = True
						afd.add_estado(novo_estado)
						afd.add_transicao(e, a, novo_estado)
						if final:
							afd.add_estados_finais(novo_estado)
					else:
						afd.add_transicao(e, a, self.transicoes[(e, a)][0])
						if self.transicoes[(e, a)][0] in finais:
							afd.add_estados_finais(self.transicoes[(e, a)][0])
		return afd
