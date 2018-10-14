#   Trabalho 1   Formais
# Alunos: Bruno George de Moraes
#         Wagner Santos
#
from collections import deque 
import automato_finito
class ExpressaoRegular:
	syntaxTree = ''
	expr = ''
	nome = ''

	def __init__(self, expr = '', nome = ''):
		self.expr = expr
		self.nome = nome
		
	def add_expressao(self, expressao):                
		self.expr.append(expressao)

	def print(self):
		saida = '' + self.expr
		saida += '\n'
		return saida

	def gen_tree(self):
				ot = self.expr	
				ot = ot.translate(bytes.maketrans(b"()", b"[]")) 
				print(ot) 
				
				print( "\n")
				st = deque(ot)
				s = deque('')
				for c in st:
						print(c)
						if c == '|':
							s.append('*')
						s.appendleft('[')
						s.append(c)
						s.append(']')
						
				#TODO arrumar notacao 
				#labelled bracket notation [X value]

				for i in s: i.rsplit('[')
				print("------------------\n")
				print(s)
				print("#-----------------#\n")
				x ='[S[NP[N Alice]][VP[V is][NP[N+[N* a student][PP? of physics'
				y = x.rsplit('[')
				print(y)

				syntaxTree = s
				return s

		#'&' or '?' or '*' nullable 
		#AHO 3.9.3
	def nullable(st):
				nullable = false
				if st.find('&') or st.find('?') or st.find('*'):
						nullable = true
				return nullable
		
	def rst_opN(c1, c2):
				rst = set()
				for i in range(1, 10): 
						rst.append(i, syntaxTree[c1] )
				
				return rst
	def lastpos(c1 , c2):
				return rst_opN(c2 , c1)

	def followpos( ):
		#TODO

				return st
		
	# AHO 3.9.5
	def to_afd(self):
		af = automato_finito.AutomatoFinito()
		final = '_F_'
		af.estados = rst_opN(syntaxTree)  
		af.inicial = set()
		af.finais.add(final)
		#TODO
		e = 10
		#there is a non-marked stateS inDstates
		#while ()
		for e in syntaxTree:
		 	if not nullable(s):
		 		if s[0] == s[1]:
		 				e = 1



		
		return af