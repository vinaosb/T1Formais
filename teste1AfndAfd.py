import automato_finito

af = automato_finito.AutomatoFinito()

af.add_transicao('q0', 'a', 'q0')
af.add_transicao('q0', 'a', 'q1')
af.add_transicao('q1', 'b', 'qf')

af.add_estados_finais('qf')
af.set_estado_inicial('q0')

print('Automato teste1')
print(af.print())
print('Automato teste1 após determinização')
print(af.to_afd(0,{}).print())