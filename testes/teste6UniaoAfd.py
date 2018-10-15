import automato_finito

af1 = automato_finito.AutomatoFinito()
af2 = automato_finito.AutomatoFinito()

af1.add_transicao('q0', 'a', 'q0')
af1.add_transicao('q0', 'b', 'qf')

af1.add_estados_finais('qf')
af1.set_estado_inicial('q0')

af2.add_transicao('q0', 'b', 'q0')
af2.add_transicao('q0', 'a', 'qf')

af2.add_estados_finais('qf')
af2.set_estado_inicial('q0')


print('Automato 1 teste6 (a*b)')
print(af1.print())
print('Automato 2 teste6 (b*a)')
print(af2.print())
print('Automato 1 U Automato 2 (a*b|b*a): \n')
print(af1.uniao(af2).print())