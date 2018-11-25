import sys
class Lexical:

	letter = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
	digit = set("0123456789")
	special = set("<>=*/;()[]}{&|!-+")
	tokens = [] # id - tipo
	tabela_simbolos = [ ('if', 'if', 'if'),
						('then', 'then', 'then'),
						('else', 'else', 'else'),
						('while', 'while', 'while'),
						('do', 'do', 'do'),
						('break', 'break', 'break'),
						('true', 'true', 'true'),
						('false', 'false', 'false'),
						('int', 'basic', 'int'),
						('float', 'basic', 'float'),
						('$', '$', '$'),
						('bool', 'basic', 'bool')] # <lexema> <terminal> <tipo>
	token_type = [  'lop', 'lop', 'attr', 'lop', 'delim', 'delim', 'delim', 'delim', 'delim', 'delim',
					'mop', 'mop', ':P'  , ':P' , 'mop'  , 'mop'  , 'num'  , 'id'   , ':P'   , 'lop'  ,
					'lop', ':P', 'lop' , 'lop', 'lop', 'lop', 'real', 'endl']
	invalid = set((-1, 0, 13, 14, 19))
	pointer = 0

	def run(self, input_name):
		input_file = open(input_name + '.prog', 'r')
		errors = []
		line_n = 0
		for line in input_file:
			line_n = line_n + 1
			line = line.replace('\t','')
			line = line.replace('\n','')
			word_n = 0
			for word in line.split(' '):
				word_n = word_n + 1
				result = self.find_token(word)
				if (result[1] == 0): #ignora linha vazia
					continue
				if result[0]: #não é um estado invalido
					token = (result[4], result[2], self.token_type[result[1]-1]) #(<lexema>, <terminal>, <tipo>)
					self.tokens.append((self.atualiza_tabela(token),line_n, word_n))
				if result[3] != '': #se existir erro
					errors.append('Error found on line '+ str(line_n) + ', word ' + str(word_n) + ': \'' + word + '\'' +  '\n'
						+ result[3] + '\n')
		out = ''
		self.tokens.append((10, line_n, 0))
		for erro in errors:
			out = out + erro + '\n'
		#print(out)
		return( self.tabela_simbolos, out)

	def atualiza_tabela(self, token):
		l = len(self.tabela_simbolos)
		for i in range(l):
			if token[0] == self.tabela_simbolos[i][0]:
				return i
		self.tabela_simbolos.append(token)
		return l

	def next_token(self):
		if self.pointer < len(self.tokens):
			token = self.tokens[self.pointer]
			self.pointer = self.pointer + 1
			return token
		else:
			return True



	def find_token(self, word):
		state = 0
		error = ''
		tipo = '' 
		acc = ''
		best_state = 0
		for char in word:
			if (state == 0):
				if (char == '>'):
					tipo = 'gt'
					state = 1
				elif (char == '<'):
					tipo = 'lt'
					state = 2
				elif (char == '='):
					tipo = 'attr'
					state = 3
				elif (char == '!'):
					tipo = 'not'
					state = 4
				elif (char == '('): #final
					tipo = 'lp'
					state = 5
				elif (char == ')'): #final
					tipo = 'rp'
					state = 6
				elif (char == '['): #final
					tipo = 'lb'
					state = 7
				elif (char == ']'): #final
					tipo = 'rb'
					state = 8
				elif (char == '{'): #final
					tipo = 'lc'
					state = 9
				elif (char == '}'): #final
					tipo = 'rc'
					state = 10
				elif (char == '/'): #final
					tipo = 'div'
					state = 11
				elif (char == '*'):
					tipo = 'mult'
					state = 12
				elif (char == '|'):
					state = 13
					tipo = 'or'
					error = 'Expected \"|\"'
				elif (char == '&'):
					state = 14
					tipo = 'and'
					error = 'Expected \"&\"'
				elif (char == '-'):  #final
					tipo = 'minus'
					state = 15
				elif (char == '+'):  #final
					tipo = 'plus'
					state = 16
				elif (char in self.digit):
					state = 17
					tipo = 'num'
				elif (char in self.letter):
					state = 18
					tipo = 'id'
				elif (char == ';'):
					state = 28
					tipo = 'endl'
				else:
					state = -1
					error = 'Expected something'
			elif(state == 1): # >
				if (char == '='):
					state = 26
					tipo = 'get'
				else:
					state = -1
				error = ''
			elif(state == 2): # <
				if (char == '='):
					state = 25
					tipo = 'let'
				else:
					state = -1
				error = ''
			elif(state == 3): # = 
				if (char == '='):
					state = 24
					tipo = 'eq'
				else:
					state = -1
				error = ''
			elif(state == 4): # !
				if (char == '='):
					state = 23
					tipo = 'dif'
				else:
					state = -1
				error = ''
			elif(state == 5): # (
				state = -1
				error = ''
			elif(state == 6): # )
				state = -1
				error = ''
			elif(state == 7): # [
				state = -1
				error = ''
			elif(state == 8): # ]
				state = -1
				error = ''
			elif(state == 9): # {
				state = -1
				error = ''
			elif(state == 10): # }
				state = -1
				error = ''
			elif(state == 11): # /
				state = -1
				error = ''
			elif(state == 12): # *
				state = -1
				error = ''
			elif(state == 13): # |
				if (char == '|'):
					state = 21
					error = ''
				else:
					state = -1
			elif(state == 14): # &
				if (char == '&'):
					state = 20
					error = ''
				else:
					state = -1
			elif(state == 15): # -
				state = -1
				error = ''
			elif(state == 16): # + 
				state = -1
				error = ''
			elif(state == 17): # num
				if (char in self.digit):
					state = 17
					error = ''
				elif (char == '.'):
					state = 19
					error = 'Expected more digits'
				else:
					state = -1
			elif(state == 18): #id
				if ((char in self.letter) or (char in self.digit)):
					state = 18
				else:
					state = -1
				error = ''
			elif(state == 19): # num.
				if (char in self.digit):
					state = 27
					error = ''
					tipo = 'real'
				else:
					state =-1
			elif(state == 20): # &&
				state = -1
				error = ''
			elif(state == 21): # ||
				state = -1
				error = ''
			elif(state == 22): # ????????????????
				state = -1
				error = ''
			elif(state == 23): # !=
				state = -1
				error = ''
			elif(state == 24): # ==
				state = -1
				error = ''
			elif(state == 25): # <=
				state = -1
				error = ''
			elif(state == 26): # >=
				state = -1
				error = ''
			elif(state == 27): # num.num
				error = ''
				if (char in self.digit):
					state = 27
				else:
					state = -1
			elif(state == 28): # ;
				state = -1
				error = ''
			if(state == -1):
				break;
			best_state = state
			acc = acc + char
		if (state == -1):
			error = 'Found invalid \"'+ char + '\"'
		return ((not (best_state in self.invalid)), best_state, tipo, error, acc)
# 