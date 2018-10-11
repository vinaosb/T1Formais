#   Trabalho 1   Formais
# Alunos: Bruno George de Moraes
#         Wagner Santos
#
from collections import deque 
import automato_finito
class ExpressaoRegular:
	syntaxTree = {}
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
                print(ot.translate(bytes.maketrans(b"()", b"[]")) )
                
                print( "\n")
                st = deque(ot)
                s = deque('')
                for c in st:
                        s.appendleft('[')
                        s.append(c)
                        s.append(']')
                        
                 #TODO nao tah gerando corretamenta a notacao.
                #labelled bracket notation [X value]
                # [S[NP[N Alice]][VP[V is][NP[N'[N a student][PP^ of physics
                
                        
                print("------------------\n")
                print(s)      
                                               
                return s

        # AHO 3.9.3
        # '&' null element
        def nullable(st):
                nullable = false 
                if st.find('&'):
                        nullable = true
                return nullable
        
	#def rst_opN

	#def lastpos(N) 
	#def followpos(P)

	# AHO 3.9.5
	def to_afd(self):
		af = automato_finito.AutomatoFinito()
		#TODO
		return af
