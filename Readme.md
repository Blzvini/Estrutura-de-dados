# Pilhas - Operações

Empilhar
- Colocar um item de dados no topo da pilha

Desempilhar
- Remover um item do topo da pilha

Ver o topo
- Mostrar o elemento que está no topo da pilha

Último a entrar, primeiro a sair
- (LIFO - LAST IN FIRST OUT)


# Filas - Operações

Enfileirar
- Colocar um item no final da fila

Desenfileirar
- Remover um item do início da fila

Ver início da fila
- Mostra o elemento que está no início da fila

Primeiro a entrar, primeiro a sair
- (FIFO - FIRST IN FIRST OUT)

# Filas de prioridade
- Os itens são ordenados por valor-chave, de modo que o item com a chave mais baixa/alta esteja sempre na frente.
- Elementos de alta prioridade são colocados no início da fila, de média prioridade no meio da fila e elementos de baixa prioridade no final da fila.

# Deques (Double ended queue)
- Suporta operações de pilhas e filas
- Agendamento de tarefas de vários processos
- Adicionar no início, remover do início
- Adicionar no final, remover do final
- Implementações estáticas e circulares

# Desvantagem de vetores
- Em um vetor não ordenado, a busca é lenta
- Em um vetor ordenado, a inserção é lenta
- Em ambos, a remoção é lenta
- O tamanho do vetor "Não pode" ser alterado depois de ter sido criado
- Mesmo vazios, ocupam espaço na memória

# Lista encadeada - NÓS
- Cada item de dados é incorporado em um nó
- Cada nó possui uma referência para o próximo nó da lista
- Um campo da própria lista contém uma referência para o primeiro nó

# Listas encadeadas - Posição - Relacionamento
Vetor (Posição)
- Cada item ocupa uma certa posição
- Cada posição pode ser acessada usando um número de índice

Lista (Relacionamento)
- A única maneira de encontrar um elemento é seguir a sequência de elementos
- Um item de dados não pode ser acessado diretamente, ou seja, o relacionamento entre eles deve ser utilizado
- Inicia com o primeiro item, vai para o segundo, então o terceiro, até encontrar o item pesquisado. (Pesquisa linear)

# Listas encadeadas
- Cada elemento da lista é armazenado em um objeto
- Cada elemento da lista referencia o próximo e só é alocado dinamicamente quando necessário
- Para referenciar o primeiro elemento é utilizado um elemento chamado cabeça da lista

# Listas encadeadas operações
Insere no início
- Insere um novo nó no início da lista
- É o local mais fácil para inserir um nó
- O próximo deste novo elemento deve ser o primeiro da lista
- A cabeça da lista aponta para o novo elemento

Excluir do início
- É o inverso de inserir no início
- Desconecta o primeiro nó roteando de novo o primeiro para apontar para o segundo nó
- O segundo nó é encontrado por meio do campo proximo no primeiro nó

Mostrar a lista e Pesquisar
- Para exibir a lista, deverá ser iniciado no primeiro elemento, seguindo a sequência de referências de nó em nó
- O final da lista é indicado pelo campo próximo no último nó apontando para null/none ao invés de outro nó
- Os nós são percorridos e é verificado se o valor do elemento é aquele que está sendo procurado
- Se atingir o final da lista sem encontrar o nó desejado, finaliza sem encontrar o elemento.

Excluir da posição
- O nó a ser eliminado deve ser localizado (pesquisado)
- Quando elimina o nó atual, terá que conectar o nó anterior ao nó seguinte

# Listas encadeadas com extremidades duplas

- Possui referência para o primeiro e para o último nó
- Para inserir um nó no final de uma lista com extemidade simples, é necessário percorrer todos os elementos
- A referência para o último nó permite inserir um novo nó diretamente no final da lista, assim como no início

# Operações

- Inserir no início
- Inserir no final (Adicional)
- Excluir do início

