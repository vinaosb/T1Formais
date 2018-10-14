#   Trabalho 1   Formais
# Alunos: Bruno George de Moraes
#         Wagner Santos
#
from collections import deque 
import automato_finito
import tree
class ExpressaoRegular:
        syntaxTree:tree.Tree
        expr = '#'
        nome = ''
        operators = set('*|')

        def __init__(self, expr = '#', nome = ''):
                self.expr = expr
                self.nome = nome
                self.syntaxTree = tree.Tree()
                
        def concatenar(self, expressao):                
                self.expr = self.expr[:-1] + expressao + '#'

        def print(self):
                saida = '' + self.expr[:-1]
                saida += '\n'
                return saida

        def gen_tree(self):
                ot = self.expr
                print(ot.translate(bytes.maketrans(b"()", b"[]")))
                
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
        def nullable(self, st):
                nullable = False 
                if st.find('&'):
                        nullable = True
                return nullable

        #def rst_opN

        #def lastpos(N) 
        #def followpos(P)

        # AHO 3.9.5
        def to_afd(self):
                af = automato_finito.AutomatoFinito()
                #TODO
                return af

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
                return tr               
                                
tr = ExpressaoRegular()
expr = 'bb|aa(af)*a'
print(expr)
print(tr.create_tree(expr).to_string())
print(tr.create_tree(expr).firstpos())