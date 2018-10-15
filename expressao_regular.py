#   Trabalho 1   Formais
# Alunos: Bruno George de Moraes
#         Wagner Santos
#
from collections import deque 
import automato_finito
import tree
class ExpressaoRegular:
		arvore:tree.Tree
		expr = '#'
		nome = ''

		def __init__(self, expr = '#', nome = ''):
				self.expr = expr
				self.nome = nome
				self.syntax_tree = tree.Tree()
				
		def concatenar(self, expressao):                
				self.expr = self.expr[:-1] + expressao + '#'

		def print(self):
				saida = '' + self.expr[:-1]
				saida += '\n'
				return saida

		def create_tree(self, expr):
				tr = tree.Tree()
				l = len(expr)-1
				if l == 0:
						tr.value = expr[0]
						return tr
				elif l < 0:
						return tr  
				else:
						count = 0
						if expr[l] ==  ')':
								i = 1
								while i != 0:
										count = count + 1
										if count > len(expr):
												return -1
										if expr[l-count] == ')':
												i = i + 1
										elif expr[l-count] == '(':
												i = i - 1
								tr.setRight(self.create_tree(expr[l-count+1:l]))
						elif expr[l] == '*':
								count = 0
								if expr[l-1] ==  ')':
										i = 1
										while i != 0:
												count = count + 1
												if count > l:
														return -1
												if expr[l-count-1] == ')':
														i = i + 1
												elif expr[l-count-1] == '(':
														i = i - 1
										if l-count-2<0:
												print('terminando o *', expr[l-count:-2])
												tr.value = '*'
												tr.setLeft(self.create_tree(expr[l-count:-2]))
												return tr
										else:
												print('passando pelo *', expr[l-count-1:])
												tr.setRight(self.create_tree(expr[l-count-1:]))
												count = count + 1
								else:
										if l-2 < 0:
												tr.value = '*'
												tr.setLeft(self.create_tree(expr[:-1]))
												return tr
										else:
												tr.setRight(self.create_tree(expr[l-1:]))
						else:
								tr.setRight(self.create_tree(expr[l]))
								
						l = l - 1 - count
						print('fim', expr[:l+1])
						if expr[l] == '|':
								tr.value = expr[l]
								tr.setLeft(self.create_tree(expr[:l]))
						else: #OK
								tr.value = '+'
								tr.setLeft(self.create_tree(expr[:l+1]))
				self.arvore = tr
				return tr               
		
		def followpos(self, tr:tree.Tree):
			   fp = tr.firstpos()
			   lp = tr.lastpos()
			   i=0
			   temp = set()
			   #for p in tr: #TODO  not iterable 
			   #	i += 1
			   #	temp.append(p.value, i)
			   return temp


		def to_afd(self):
			   af = automato_finito.AutomatoFinito()
			   af.inicial = self.arvore.value
			   final = '#'
			   alfabeto = self.expr.lstrip('+|*?()')
			   Dstates = set()
			   #while there is a non-marked state S in Dstates  
			   # mark S
			   for i in alfabeto:
			   	U = union(followpos()) #followpos p for all p in S from alfabeto i







ex = 'bb|aa(af)*a'
tr = ExpressaoRegular(ex)
print(tr.print())
print(tr.create_tree(tr.expr).to_string())
print(tr.create_tree(tr.expr).firstpos())
print('---------------')


print('outra ER')
x ='c?d(a|b)+'
e = ExpressaoRegular(x)
print(e.create_tree(e.expr).lastpos()) 
print(e.followpos(e.arvore)) 
print(e.to_afd())

