import automato_finito

af1 = automato_finito.AutomatoFinito()
af2 = automato_finito.AutomatoFinito()

af1.add_transicao('q0', 'a', 'qf')
af1.add_transicao('qf', 'b', 'qf')
af1.add_transicao('qf', 'a', 'qf')

af1.add_estados_finais('qf')
af1.set_estado_inicial('q0')

af2.add_transicao('q0', 'a', 'q1')
af2.add_transicao('q1', 'b', 'q2')
af2.add_transicao('q2', 'b', 'q3')
af2.add_transicao('q3', 'a', 'qf')
af2.add_transicao('qf', 'a', 'qf')

af2.add_estados_finais('qf')
af2.set_estado_inicial('q0')


print('Automato 1 teste6 (a(a|b)*)')
print(af1.print())
print('Automato 2 teste6 (abba*)')
print(af2.print())
print('Automato 1 Intersecao Automato 2 (abba*): \n')
print(af1.intersecao(af2).print())