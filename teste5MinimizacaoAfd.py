import automato_finito

af = automato_finito.AutomatoFinito()

af.add_transicao('q0', 'a', 'q1')
af.add_transicao('q1', 'a', 'q0')#q1 equivalente a qf
af.add_transicao('qf', 'a', 'q0')#q2 morto
af.add_transicao('q3', 'a', 'qf')#q3 inalcancavel


af.add_estados_finais('qf')
af.add_estados_finais('q1')
af.set_estado_inicial('q0')

print('Automato teste5')
print(af.print())
af.minimizar()
print('Automato teste5 minimizado com q1 equivalente a qf, q2 morto e q3 inalcancavel')
print(af.print())