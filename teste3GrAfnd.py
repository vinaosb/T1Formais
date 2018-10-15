import gramatica_regular

gr = gramatica_regular.GramaticaRegular()

gr.add_regras('S', 'a', 'A')
gr.add_regras('A', 'a', 'B')
gr.add_regras('A', 'a', '&')
gr.add_regras('B', 'b', '&')
gr.set_variavel_inicial('S')

print('Gramatica regular teste3')
print(gr.print())
print('Gramatica regular teste3 convertida para afnd: \n')
print(gr.to_afnd().print())