# Classificações de Complexidade Algorítmica

## 1. Introdução

A classificação da complexidade de algoritmos é uma ferramenta essencial na análise de desempenho computacional.

Ela mede como o tempo de execução e o uso de memória de um algoritmo variam em relação ao tamanho de sua entrada.

Este documento aborda classificações comuns de complexidade, destacando suas aplicações práticas e implicações.

## 2. Objetivo

Fornecer uma visão clara e organizada sobre as classificações de complexidade de algoritmos, detalhando os principais conceitos de complexidade temporal e espacial, bem como exemplos de aplicações práticas.

## 3. Público-alvo

Este material destina-se a estudantes, desenvolvedores e profissionais de tecnologia interessados em compreender como analisar e otimizar o desempenho de algoritmos.

## 4. Conteúdo

### 4.1. Classificações de Complexidade

#### 4.1.1. O(1): Complexidade Constante

A complexidade constante é caracterizada pela execução de uma operação em tempo fixo, independentemente do tamanho da entrada. Um exemplo simples é o acesso direto a um elemento em um array por meio de índice.

#### 4.1.2. O(n): Complexidade Linear

Imagine uma lista com **N elementos**. Encontrar o maior número nesta lista requer examinar cada elemento, garantindo que nenhum seja ignorado.

##### 4.1.2.1. Complexidade Temporal

A complexidade temporal desse algoritmo é **O(n)**, porque cada elemento é visitado uma única vez.

À medida que a lista cresce, o tempo de execução aumenta linearmente.

##### 4.1.2.2. Complexidade Espacial

A complexidade espacial é **O(1)**, pois utiliza apenas uma quantidade constante de memória para variáveis auxiliares.

##### 4.1.2.3. Ilustração Prática

Suponha que a lista seja `[4, 7, 1, 9, 3]`. O algoritmo segue os passos:

1. Inicializa uma variável, `maior`, com o valor do primeiro elemento da lista (4).
2. Percorre os demais elementos:
   - Compara 7 com `maior`. Atualiza `maior` para 7.
   - Compara 1 com `maior`. Nenhuma atualização é feita.
   - Compara 9 com `maior`. Atualiza `maior` para 9.
   - Compara 3 com `maior`. Nenhuma atualização é feita.
3. Retorna o valor armazenado em `maior`, que é 9.

##### 4.1.2.4. Observações Importantes

Este é um exemplo clássico de complexidade linear, eficiente para situações onde cada elemento deve ser avaliado individualmente.

- A eficiência espacial é garantida pela ausência de estruturas adicionais.
- Escalabilidade é um ponto forte, tornando o algoritmo adequado para listas grandes.
- Este tipo de algoritmo serve de base para soluções mais complexas, como ordenação e análise de grandes volumes de dados.

#### 4.1.3. O(log n): Complexidade Logarítmica

Algoritmos com complexidade logarítmica são caracterizados por uma redução progressiva no tamanho do problema a cada iteração, resultando em um tempo de execução que cresce muito mais lentamente do que o tamanho da entrada.

##### Exemplo Prático: Pesquisa Binária

1. Suponha uma lista ordenada `[1, 3, 5, 7, 9, 11]` e o objetivo de encontrar o elemento `7`.
2. A cada passo, o algoritmo divide a lista ao meio:
   - Compara o elemento central (neste caso, `7`) com o alvo.
   - Se o elemento for igual ao alvo, retorna o índice correspondente.
   - Caso contrário, elimina metade da lista e repete o processo.

Este comportamento é altamente eficiente para listas ordenadas.

#### 4.1.4. O(n log n): Complexidade Linearitmica

A complexidade linearitmica combina o crescimento linear e logarítmico, geralmente observada em algoritmos de ordenação eficientes.

##### Exemplo Prático: Merge Sort

1. Divide a lista em sublistas menores até que cada sublista tenha apenas um elemento.
2. Combina as sublistas de forma ordenada.
3. Repete o processo até que toda a lista esteja ordenada.

Este algoritmo é uma escolha popular para ordenação de grandes conjuntos de dados devido à sua escalabilidade.

#### 4.1.5. O(n²): Complexidade Quadrática

Algoritmos com complexidade quadrática são adequados apenas para pequenas entradas, pois seu desempenho degrada rapidamente conforme o tamanho da entrada aumenta.

##### Exemplo Prático: Ordenação por Seleção

1. Para cada elemento da lista, encontra o menor elemento restante e o coloca na posição correta.
2. Repete o processo até que toda a lista esteja ordenada.

#### 4.1.6. O(2^n): Complexidade Exponencial

Problemas com complexidade exponencial são extremamente difíceis de resolver para entradas maiores, pois o tempo de execução dobra a cada novo elemento.

##### Exemplo Prático: Problema de Subconjuntos

Determinar todos os subconjuntos possíveis de um conjunto envolve um crescimento exponencial no número de soluções conforme o tamanho do conjunto aumenta.

#### 4.1.7. O(n!): Complexidade Fatorial

Algoritmos de complexidade fatorial são frequentemente usados em problemas de combinações e permutações, mas são impraticáveis para entradas grandes.

##### Exemplo Prático: Permutações

Gerar todas as permutações de um conjunto de elementos resulta em um crescimento fatorial no tempo de execução conforme o tamanho do conjunto aumenta.

## 5. Guia de Uso

1. Determine o tamanho e a natureza da entrada para avaliar o impacto da complexidade.
2. Escolha algoritmos que ofereçam equilíbrio entre tempo de execução e uso de memória, considerando os recursos disponíveis.
3. Para entradas pequenas, algoritmos com complexidade elevada (como O(n²)) podem ser aceitáveis, mas para grandes entradas, prefira soluções com complexidade reduzida (como O(log n) ou O(n)).

## 6. Referências

- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. **Introduction to Algorithms.** MIT Press.
- Sedgewick, R., & Wayne, K. **Algorithms.** Addison-Wesley.
- Knuth, D. E. **The Art of Computer Programming.** Addison-Wesley.

## 7. Anexos

### 7.1. Tabela de Resumo

| Notation  | Nome                | Exemplo de Algoritmo          |
|-----------|---------------------|-------------------------------|
| O(1)      | Constante          | Acesso direto em arrays       |
| O(log n)  | Logarítmica        | Pesquisa binária             |
| O(n)      | Linear             | Laço simples                 |
| O(n log n)| Linearitmica       | Merge Sort, Quick Sort        |
| O(n²)     | Quadrática         | Bubble Sort, Selection Sort   |
| O(2^n)    | Exponencial        | Problema da mochila (bruto)   |
| O(n!)     | Fatorial           | Permutações                  |
