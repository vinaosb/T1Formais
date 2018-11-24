import sys
import reader
class Analisador:
	gram = {}
	follow = {}
	first = {}
	ta = {}
	pilha = []

	def __init__(self):
		self.follow['program'] = set()
		self.follow['program'].add('$')
		self.ler_gramatica()
		self.calc_follow()
		self.calc_follow()
		self.calc_follow()
		self.calc_follow()
		self.calc_follow()
		self.calc_follow()
		self.calc_follow()
		w = len(self.gram.keys()) #numero de terminais
		h = len(self.calc_num_terminais()) #numero de nao terminais
		self.tab_ll1()
		self.pilha = ['program', '$']

	def ler_token(self,token):
		print(self.pilha)
		if self.pilha[0] in self.gram.keys():
			if (self.pilha[0], token) in self.ta.keys():
				p = self.pilha[0]
				self.pilha.pop(0)
				l = self.ta[(p,token)].copy()
				l.reverse()
				for t in l:
					if not t == '&':
						self.pilha.insert(0, t)
				self.ler_token(token)
			else:
				print('erro', self.pilha[0], token)
				return 0
		elif (self.pilha[0] == token):
			self.pilha.pop(0)
		else:
			if (self.pilha[0] == '$'):
				print('foi ')
			else:
				print('segundo erro')
			return 0
		return 1



	def ler_gramatica(self):
		input_name = 'gramatica.py'
		input_file = open(input_name)
		for line in input_file:
			line = line.replace('\t','')
			line = line.replace('\n','')
			lr = line.split ('->')
			left = lr[0].replace(' ', '')
			right = []
			for prod in lr[1].split('|'):
				prodx = []
				for token in prod.split(' '):
					if token != '':
						prodx.append(token)
				right.append(prodx)
			self.gram[left] = right
		#print (self.gram)
		return 0
	def tab_ll1(self):
		for key in self.gram.keys():
			prods = self.gram[key]
			for prod in prods:
				first = set()
				for i in range(0, len(prod)):
					first.update(self.calc_first(prod[i]))
					if not '&' in first:
						first.discard('&')
						break
				if '&' in first:
					for b in self.follow[key]:
						self.ta[(key,b)] = prod
					if '$' in self.follow[key]:
						self.ta[(key, '$')] = prod
				first.discard('&')
				for token in first:
					self.ta[(key,token)] = prod

		#for key in self.ta.keys():
			#print(key, self.ta[key])



	def calc_first(self, t):
		if not t in self.first.keys():
			self.first[t] = set()
			if not t in self.gram.keys():
				self.first[t].add(t)
			else:
				prods = self.gram[t]
				for prod in prods:
					epson = True;
					first = set()
					for token in prod:
						first.update(self.calc_first(token))
						if '&' in first:
							first.discard('&')
						else:
							epson = False
							break
					if epson:
						first.add('&')
					else:
						first.discard('&')
					self.first[t].update(first)
		return self.first[t]

	def calc_follow(self):
		after = {}
		for key in self.gram.keys():
			prods = self.gram[key]
			for prod in prods:
				count = 0
				for token in prod:
					if not token in self.gram.keys():
						x = 0
					else:
						if not token in self.follow.keys():
							self.follow[token] = set()
						if count == len(prod)-1:
							if not token in after.keys():
								after[token] = set()
							after[token].add(key)
						else:
							first = self.calc_first(prod[count + 1])
							i = 2
							while '&' in first:
								if count + i == len(prod):
									break
								first.discard('&')
								first.update(self.calc_first(prod[count + i]))
							self.follow[token].update(first)
							self.follow[token].discard('&')
							if '&' in first:
								#print(first, prod[count+1], token, key)
								if not token in after.keys():
									after[token] = set()
								after[token].add(key)
								
					count = count + 1
		#print(after)
		for token in after.keys():
			for tokens in after[token]:
				self.follow[token].update(self.follow[tokens])
		#print(after['decls'])
		return 0

	def calc_num_terminais(self):
		nt = set()
		input_name = 'gramatica.py'
		input_file = open(input_name)
		for line in input_file:
			line = line.replace('\t','')
			line = line.replace('\n','')
			lr = line.split ('->')
			for prod in lr[1].split('|'):
				for token in prod.split(' '):
					if token != '':
						if not token in self.gram.keys():
							nt.add(token)
		nt.discard('&')
		nt.add('$')
		return nt



an = Analisador()
lex = reader.Lexical()
res = lex.run()
tokens = res[0]
tabela = res[1]
print(an.ta[('decls', 'basic')])
for t in tokens:
	print(tabela[t][1])
	if an.ler_token(tabela[t][1]) == 0:
		break
		i = 0
#for key in an.ta.keys():
#	if an.ta[key][0] == '&':
#		print(key,an.ta[key])

#print(an.ta)








