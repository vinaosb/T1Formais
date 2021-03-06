import automato_finito

af = automato_finito.AutomatoFinito()

af.add_transicao('q0', 'a', 'q1')
af.add_transicao('q1', 'a', 'q1')
af.add_transicao('q1', 'b', 'q2')
af.add_transicao('q2', 'b', 'qf')

af.add_estados_finais('qf')
af.set_estado_inicial('q0')

print('Automato teste2')
print(af.print())
print('Automato teste2 transformado em gr: \n')
print(af.to_gr().print())