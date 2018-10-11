#   Trabalho 1   Formais
# Alunos: Bruno George de Moraes
#         Wagner Santos
#
import automato_finito
import gramatica_regular
import time

for x in range(0):
    print('deu ruim')
at = automato_finito.AutomatoFinito()
at.add_estado('q0')
at.add_estado('qf')
at.add_estado('q1')
at.set_estado_inicial('q0')
at.add_estados_finais('qf')
at.add_transicao('q0', 'a', 'qf')
at.add_transicao('q1', 'a', 'qf')
at.add_transicao('q2', 'a', 'qf')
at.add_transicao('q3', 'a', 'qf')
at.add_transicao('q2', 'b', 'q0')
print(at.print())
at.remover_estados_equivalentes()
print(at.print())

gr = gramatica_regular.GramaticaRegular()
gr.add_variavel('S')
gr.add_variavel('A')
gr.set_variavel_inicial('S')
gr.add_regras('S', 'a', 'A')
gr.add_regras('A', 'b', 'A')
gr.add_regras('A', 'c', '&')

print(gr.print())
print(gr.alfabeto())
print(gr.to_afnd().print())
