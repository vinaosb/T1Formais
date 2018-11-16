class Lexical:

	letter = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
	digit = set("0123456789")
	special = set("<>=*/;()[]}{&|!-+")
	tokens = [] # id - tipo
	tabela_simbolos = [ ('if', 'pr', 'if'),
						('then', 'pr', 'then'),
						('else', 'pr', 'else'),
						('while', 'pr', 'while'),
						('do', 'pr', 'do'),
						('break', 'pr', 'break'),
						('true', 'pr', 'true'),
						('false', 'pr', 'false'),
						('int', 'basic', 'int'),
						('real', 'basic', 'real'),
						('bool', 'basic', 'bool')] # <lexema> [<id> <if> <else> <lop> <mop> <begin> <end> ]
	token_type = [  'lop', 'lop', 'attr', 'lop', 'delim', 'delim', 'delim', 'delim', 'delim', 'delim'
					, 'mop', 'mop', ':P', ':P', 'mop', 'mop', 'num', 'id', ':P', 'lop', 'lop', 'mop', 'lop', 'lop'
					, 'lop', 'lop', 'real']
	invalid = set((-1, 0, 13, 14, 19))

	def run(self):
		input_name = "input"
		input_file = open(input_name + '.prog', 'r')
		for line in input_file:
			line = line.replace('\t','')
			line = line.replace('\n','')
			for word in line.split(' '):
				result = self.find_token(word)
				if (result[1] == 0):
					continue
				if result[0]:
					token = (word, self.token_type[result[1]-1], result[2])
					self.tokens.append(self.atualiza_tabela(token))
				else:
					continue
					#aqui deu erro
					#print(word, result)
		for t in self.tokens:
			print(self.tabela_simbolos[t])

	def atualiza_tabela(self, token):
		l = len(self.tabela_simbolos)
		for i in range(l):
			if token[0] == self.tabela_simbolos[i][0]:
				return i
		self.tabela_simbolos.append(token)
		return l


	def find_token(self, word):
		state = 0
		error = ''
		tipo = '' 
		for char in word:
			if (state == 0):
				if (char == '>'):
					tipo = 'GT'
					state = 1
				elif (char == '<'):
					tipo = 'LT'
					state = 2
				elif (char == '='):
					tipo = 'ATTR'
					state = 3
				elif (char == '!'):
					tipo = 'NOT'
					state = 4
				elif (char == '('): #final
					tipo = 'LP'
					state = 5
				elif (char == ')'): #final
					tipo = 'RP'
					state = 6
				elif (char == '['): #final
					tipo = 'LB'
					state = 7
				elif (char == ']'): #final
					tipo = 'RB'
					state = 8
				elif (char == '{'): #final
					tipo = 'LC'
					state = 9
				elif (char == '}'): #final
					tipo = 'RC'
					state = 10
				elif (char == '/'): #final
					tipo = 'DIV'
					state = 11
				elif (char == '*'):
					tipo = 'MULT'
					state = 12
				elif (char == '|'):
					state = 13
					tipo = 'OR'
					error = 'expected \"|\"'
				elif (char == '&'):
					state = 14
					tipo = 'AND'
					error = 'expected \"&\"'
				elif (char == '-'):  #final
					tipo = 'MIN'
					state = 15
				elif (char == '+'):  #final
					tipo = 'PLUS'
					state = 16
				elif (char in self.digit):
					state = 17
				elif (char in self.letter):
					state = 18
				else:
					state = -1
					error = ' expected something'

				continue
			elif(state == 1): # >
				if (char == '='):
					state = 26
					tipo = 'GET'
				else:
					state = -1
				error = ''
				continue
			elif(state == 2): # <
				if (char == '='):
					state = 25
					tipo = 'LET'
				else:
					state = -1
				error = ''
				continue
			elif(state == 3): # = 
				if (char == '='):
					state = 24
					tipo = 'EQ'
				else:
					state = -1
				error = ''
				continue
			elif(state == 4): # !
				if (char == '='):
					state = 23
					tipo = 'DF'
				else:
					state = -1
				error = ''
				continue
			elif(state == 5): # (
				state = -1
				error = ''
				continue
			elif(state == 6): # )
				state = -1
				error = ''
				continue
			elif(state == 7): # [
				state = -1
				error = ''
				continue
			elif(state == 8): # ]
				state = -1
				error = ''
				continue
			elif(state == 9): # {
				state = -1
				error = ''
				continue
			elif(state == 10): # }
				state = -1
				error = ''
				continue
			elif(state == 11): # /
				state = -1
				error = ''
				continue
			elif(state == 12): # *
				if (char == '*'):
					state = 22
					tipo = 'GT'
				else:
					state = -1
				continue
			elif(state == 13): # |
				if (char == '|'):
					state = 21
					error = ''
				else:
					state = -1
				
				continue
			elif(state == 14): # &
				if (char == '&'):
					state = 20
					error = ''
				else:
					state = -1
				
				continue
			elif(state == 15): # -
				state = -1
				error = ''
				continue
			elif(state == 16): # + 
				state = -1
				error = ''
				continue
			elif(state == 17): # num
				if (char in self.digit):
					state = 17
					error = ''
				elif (char == '.'):
					state = 19
					error = 'expected more digits"'
				else:
					state = -1
				continue
			elif(state == 18): #id
				if ((char in self.letter) or (char in self.digit)):
					state = 18
				else:
					state = -1
				error = ''
				continue
			elif(state == 19): # num.
				if (char in self.digit):
					state = 27
					error = ''
				else:
					state =-1
				
				continue
			elif(state == 20): # &&
				state = -1
				error = ''
				continue
			elif(state == 21): # ||
				state = -1
				error = ''
				continue
			elif(state == 22): # **
				state = -1
				error = ''
				continue
			elif(state == 23): # !=
				state = -1
				error = ''
				continue
			elif(state == 24): # ==
				state = -1
				error = ''
				continue
			elif(state == 25): # <=
				state = -1
				error = ''
				continue
			elif(state == 26): # >=
				state = -1
				error = ''
				continue
			elif(state == 27): # num.num
				error = ''
				if (char in self.digit):
					state = 27
				else:
					state = -1
				continue
		if (state == -1):
			error = 'found invalid \"'+ char + '\"'
		return ((not (state in self.invalid)), state, tipo, error)

lex = Lexical()
lex.run()
# 