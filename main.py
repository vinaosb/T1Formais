#   Trabalho 1   Formais
# Alunos: Bruno George de Moraes
#         Wagner Santos
#
from automato_finito import *
from gramatica_regular import *

at = AutomatoFinito()
at.add_estado('q0')
at.add_estado('qf')
at.add_estado('q1')
at.set_estado_inicial('q0')
at.add_estados_finais('qf')
at.add_transicao('q0', 'a', 'qf')
at.add_transicao('qf', 'b', 'q0')
at.add_transicao('q1', 'b', 'q1')
at.add_transicao('q1', 'a', 'q1')
print(at.print())
at.remover_estados_equivalentes()
print(at.print())

gr = GramaticaRegular()
gr.add_variavel('S')
gr.add_variavel('A')
gr.set_variavel_inicial('S')
gr.add_regras('S', 'a', 'A')
gr.add_regras('A', 'b', 'A')
gr.add_regras('A', 'c', '&')

print(gr.print())
print(gr.alfabeto())
print(gr.to_afnd().print())
