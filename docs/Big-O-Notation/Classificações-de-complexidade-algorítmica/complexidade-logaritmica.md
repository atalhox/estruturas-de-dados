# Complexidade Logarítmica - O(log n)

## 1. Introdução

A notação Big O é uma ferramenta essencial na análise de algoritmos, usada para descrever o comportamento de funções computacionais em termos de desempenho e escalabilidade.

O termo O(log n), ou complexidade logarítmica, caracteriza algoritmos cuja quantidade de operações cresce proporcionalmente ao logaritmo do tamanho da entrada, ao invés de crescer linearmente. Essa classificação é comumente associada a processos de divisão e conquista ou pesquisas eficientes.

## 2. Objetivo

Este documento tem como objetivo apresentar uma descrição detalhada da complexidade O(log n), explorando sua definição, aplicações práticas, vantagens e limitações no contexto de análise de algoritmos.

## 3. Público-alvo

Este material destina-se a estudantes, desenvolvedores e profissionais da área de tecnologia da informação, com conhecimento básico em estrutura de dados e algoritmos, que desejam compreender ou aprofundar o estudo sobre análise de complexidade computacional, especialmente em cenários onde se busca eficiência em operações de pesquisa e ordenação.

## 4. Conteúdo

### 4.1. Definição de O(log n)

Complexidade logarítmica descreve algoritmos cuja quantidade de operações necessárias para resolver um problema aumenta proporcionalmente ao logaritmo do tamanho da entrada. Geralmente, a base do logaritmo é 2, refletindo a divisão do problema em partes menores.

Isso significa que, se a entrada dobra de tamanho, o número de operações adicionais requeridas cresce em uma proporção menor.

### 4.2. Características

- **Eficiência em dados grandes**: Algoritmos O(log n) são ideais para operações em conjuntos de dados volumosos.
- **Divisão e conquista**: Geralmente aplicável em problemas que podem ser divididos repetidamente em subproblemas menores.
- **Escalabilidade controlada**: O impacto do aumento no tamanho da entrada é reduzido em comparação a complexidades lineares ou quadráticas.

### 4.3. Exemplos de O(log n)

#### 4.3.1. Pesquisa binária

A pesquisa binária é um exemplo clássico de algoritmo O(log n). Ele funciona dividindo um array ordenado em metades até encontrar o elemento desejado.

```python
def pesquisa_binaria(array, elemento):
    inicio = 0
    fim = len(array) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if array[meio] == elemento:
            return meio
        elif array[meio] < elemento:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1  # Elemento não encontrado

array = [10, 20, 30, 40, 50, 60, 70]
print(pesquisa_binaria(array, 40))  # Saída: 3
```

#### 4.3.2. Armazenamento e busca em árvores balanceadas

Em estruturas como AVL ou árvores binárias de busca balanceadas, as operações de inserção, remoção e busca possuem complexidade O(log n), devido à redução progressiva do número de nós analisados.

```python
from sortedcontainers import SortedDict

arvore = SortedDict()
arvore[10] = "dez"
arvore[20] = "vinte"
arvore[30] = "trinta"

print(arvore[20])  # Saída: vinte
```

#### 4.3.3. Divisão em algoritmos de ordenação

Algoritmos como Merge Sort e Quick Sort utilizam divisão logarítmica para ordenar elementos, embora sua complexidade geral seja O(n log n).

### 4.4. Benefícios do O(log n)

- **Alta eficiência**: Ideal para resolver problemas em conjuntos de dados grandes.
- **Confiabilidade**: Comportamento previsível em termos de desempenho.
- **Boa integração com estruturas de dados eficientes**: Árvores e heaps são exemplos de aplicações práticas.

### 4.5. Limitações do O(log n)

- **Necessidade de ordenação**: Em muitos casos, como na pesquisa binária, a entrada deve estar previamente ordenada.
- **Sobrecarga em entradas pequenas**: Para dados reduzidos, os benefícios do O(log n) podem não ser tão evidentes.

## 5. Guia de uso

1. **Avalie o problema**: Identifique se a entrada pode ser dividida repetidamente em subproblemas menores.
2. **Escolha estruturas adequadas**: Árvores balanceadas e heaps são bons exemplos de estruturas que suportam operações logarítmicas.
3. **Garanta a ordenação**: Verifique se os dados de entrada estão em um formato compatível para aplicação de algoritmos O(log n).

## 6. Referências

- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms*. MIT Press.
- Goodrich, M. T., & Tamassia, R. (2014). *Data Structures and Algorithms in Python*. Wiley.
- Sedgewick, R., & Wayne, K. (2011). *Algorithms*. Addison-Wesley.

## 7. Anexos

### 7.1. Glossário

- **Logaritmo**: Operador matemático que indica o expoente ao qual uma base fixa deve ser elevada para atingir um dado número.
- **Árvore balanceada**: Estrutura de dados em que a diferença de altura entre os ramos é controlada para manter eficiência em operações.
- **Divisão e conquista**: Estratégia algorítmica que divide um problema em subproblemas menores e resolve cada um separadamente.

### 7.2. Exemplo adicional

Busca em uma Heap Binária (estrutura priorizada):

```python
import heapq

heap = []
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)
heapq.heappush(heap, 5)

print(heapq.heappop(heap))  # Saída: 5
```
