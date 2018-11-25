import sys
import reader
class Analisador:
	gram = {}
	follow = {}
	first = {}
	ta = {}
	pilha = []
	acc = []

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
		self.sync_set()
		w = len(self.gram.keys()) #numero de terminais
		h = len(self.calc_num_terminais()) #numero de nao terminais
		self.tab_ll1()
		self.pilha = ['program', '$']

	def ler_token(self,token):
		error = ''
		print(self.pilha)
		if self.pilha[0] in self.gram.keys():
			if (self.pilha[0], token) in self.ta.keys():
				p = self.pilha[0]
				if self.ta[(p, token)][0] == 'sync': #encontrou sync tira da pilha
					self.pilha.pop(0)
					error = error + 'Expected ' + str(self.calc_first(self.pilha[0])) + ', found: ' + token + '. Action: Popping terminal. \n'
					error = error + self.ler_token(token)
				else:
					self.pilha.pop(0)
					l = self.ta[(p,token)].copy()
					l.reverse()
					for t in l:
						if not t == '&':
							self.pilha.insert(0, t)
					error = error + self.ler_token(token)
			else:
				#skip
				if token == '$': #fim de arquivo
					error = error + 'Unexpected end of file \n'
				else: #nao encontrou sync, pula o token
					error = error + 'Expected ' + str(self.calc_first(self.pilha[0])) + ', found: ' + token + '. Action: Skipping token. \n'
				return error
		elif (self.pilha[0] == token): # encontrou terminal correto
			self.acc.append(self.pilha[0])
			self.pilha.pop(0)
		else: #encontrou terminal errado
			if (self.pilha[0] == '$'): #encontrou tokens depois do ultimo '}'
				error = error + 'Unexpected token after end of program: ' + token + '. \n'
			else: # igonra o input e aceita o terminal da pilha
				error = error + 'Expected ' + self.pilha[0] + ', found: ' + token + '. Action: Using ' + self.pilha[0] + '.\n'
				self.acc.append(self.pilha[0])
				self.pilha.pop(0)
			return error
		return error

	def sync_set(self):
		for nt in self.follow.keys():
			for t in self.follow[nt]:
				self.ta[nt,t] = ['sync']


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


if len(sys.argv) > 1:
	input_name = sys.argv[1]
else:
	input_name = "input"
an = Analisador()
lex = reader.Lexical()
res = lex.run(input_name)
erros = res[1]
tabela = res[0]
t = lex.next_token()
while t != True:
	print(tabela[t[0]][1])
	erro = an.ler_token(tabela[t[0]][1])
	if erro != '':
		erros = erros + 'Error found on line: ' + str(t[1]) + ' word: ' + str(t[2]) + '\n ' +  erro + '\n'
	t = lex.next_token()

print('')

if erros != '':
	print('ERROS: ')
	print()
	print(erros)
	
else:
	print('COMPILADO COM SUCESSO')

acc = ''
for token in an.acc:
	acc = acc + token + ' '
	if token == 'endl':
		acc = acc + '\n'
print('')
print('TEXTO ACEITO:')
print('')
print(acc)

#for key in an.ta.keys():
#	if an.ta[key][0] == '&':
#		print(key,an.ta[key])

#print(an.ta)








