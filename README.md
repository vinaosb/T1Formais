Universidade Federal de Santa Catarina 
Departamento de Informática e Estatística				11/10/2018

Bruno George de Moraes 	
Wagner Braga dos Santos

Linguagem usada python.  
Estruturas de dados usadas: arvore binaria, deque, dicionarios 	   


Modelagem AFD , GR, ER  arrays string....


Como usar:

interface por terminal aceita comandos. 

help -> mostra os comandos acessiveis em cada momento

o programa permite criar, editar ou deletar automatos, expressoes regulares ou gramaticas regulares
após iniciar a criação ou edição de automato, a interface passa a aceitar comandos que irão alterar o automato aberto, para sair basta utilizar o comando exit

exemplo de fluxo:

new af novo_automato (cria um novo automato finito e inicia a edição do mesmo)
add q0 a qf (adicina a transição que vai de q0 a qf por 'a' e cria ambos os estados caso não existam)
inicial q0 (indica que q0 é estado inicial)
final add qf (indica que qf é estado final)
print (imprime o automato aberto na tela)
to_afnd (determiniza o automato, criando um novo e iniciando a edição do mesmo)
exit (volta ao inicio)
list (imprime a lista de automatos, gramaticas e expressoes existentes)




