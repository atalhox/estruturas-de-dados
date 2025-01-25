# Entendendo as classificações

## 1. Introdução

A classificação da complexidade de algoritmos é uma ferramenta essencial na análise de desempenho computacional.

Ela mede como o tempo de execução e o uso de memória de um algoritmo variam em relação ao tamanho de sua entrada.

Este documento aborda classificações comuns de complexidade, destacando suas aplicações práticas e implicações.

## 2. Objetivo

Fornecer uma visão clara e organizada sobre as classificações de complexidade de algoritmos, detalhando os principais conceitos de complexidade temporal e espacial, bem como exemplos de aplicações práticas.

## 3. Público-alvo

Este material destina-se a estudantes, desenvolvedores e profissionais de tecnologia interessados em compreender como analisar e otimizar o desempenho de algoritmos.

## 4. Guia de Uso

1. Determine o tamanho e a natureza da entrada para avaliar o impacto da complexidade.
2. Escolha algoritmos que ofereçam equilíbrio entre tempo de execução e uso de memória, considerando os recursos disponíveis.
3. Para entradas pequenas, algoritmos com complexidade elevada (como O(n²)) podem ser aceitáveis, mas para grandes entradas, prefira soluções com complexidade reduzida (como O(log n) ou O(n)).

## 5. Referências

- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. **Introduction to Algorithms.** MIT Press.
- Sedgewick, R., & Wayne, K. **Algorithms.** Addison-Wesley.
- Knuth, D. E. **The Art of Computer Programming.** Addison-Wesley.

## 6. Anexos

### 6.1. Tabela de Resumo

| Notation  | Nome                | Exemplo de Algoritmo          |
|-----------|---------------------|-------------------------------|
| O(1)      | Constante          | Acesso direto em arrays        |
| O(log n)  | Logarítmica        | Pesquisa binária               |
| O(n)      | Linear             | Laço simples                   |
| O(n log n)| Linearitmica       | Merge Sort, Quick Sort         |
| O(n²)     | Quadrática         | Bubble Sort, Selection Sort    |
| O(2^n)    | Exponencial        | Problema da mochila (bruto)    |
| O(n!)     | Fatorial           | Permutações                    |
