# Complexidade Linear-Logarítmica - O(n log n)

## 1. Introdução

A notação Big O é amplamente utilizada em análise de algoritmos para descrever o comportamento de funções computacionais em termos de eficiência e escalabilidade.

!!! info "Nota"
    O termo O(n log n), ou complexidade linear-logarítmica, caracteriza algoritmos cuja quantidade de operações cresce proporcionalmente ao produto do tamanho da entrada (n) e do logaritmo do tamanho da entrada (log n).

    Essa complexidade é comum em algoritmos de ordenação eficientes e em métodos que utilizam estratégias de divisão e conquista.

## 2. Objetivo

Este documento tem como objetivo apresentar uma descrição detalhada da notação O(n log n), explorando sua definição, características, exemplos de aplicação e boas práticas para utilização em análise de algoritmos.

## 3. Público-alvo

Este material é destinado a estudantes, desenvolvedores e profissionais da área de tecnologia da informação, com conhecimento básico em estrutura de dados e algoritmos, que desejam compreender ou aprofundar o estudo sobre análise de complexidade computacional.

## 4. Conteúdo

### 4.1. Definição de O(n log n)

Para explicar de maneira bem simples e clara, vamos pensar na complexidade **linear logarítmica** O(n log(n)) como uma combinação de duas coisas:

#### Parte linear(n)

Significa que você precisa processar **todos os elementos** da sua lista pelo menos uma vez. Por exemplo, imagine que você tenha que olhar cada item de uma lista de compras.

#### Parte logarítmica (log n)

Refere-se ao fato de que, para cada elemento que você processa, você faz **algumas operações extras**, mas essas operações diminuem rapidamente à medida que a lista cresce.

É como dividir a lista pela metade várias vezes, como em uma pesquisa binária

#### Juntando tudo

Agora, vamos juntar as duas ideias:

A complexidade O(n log n) significa que você faz uma operação logarítmica `log n` para cada um dos `n` elementos da sua lista.

Um exemplo prático seria organizar fichas de alunos em ordem alfabética (ordenar uma lista):

- Primeiro, você divide as fichas em grupos menores (isso é o `log n`).
- Depois, combina os grupos de forma organizada, passando por todas as fichas (isso é o `n`).

Então, você tem:

- **Linear** porque você passa por todas as fichas.
- **Logarítmico** porque você divide e organiza as fichas de forma eficiente.

No fim, O(n log n) aparece em situações onde:

1. Você precisa trabalhar com todos os itens de uma lista `n`.
2. E fazer algo eficiente, como dividir e combinar várias vezes `log n`.

Por isso, o tempo de execução é proporcional ao tamanho da lista `n`, multiplicado pelo esforço adicional de dividir e organizar `log n`.

!!! tip "Dica"
    Essa complexidade é geralmente observada em algoritmos que repetem uma operação logarítmica para cada elemento da entrada.

### 4.2. Características

- **Combinação eficiente**: O(n log n) oferece um equilíbrio entre escalabilidade e eficiência.
- **Relevância prática**: Muitos algoritmos de ordenação e métodos baseados em divisão e conquista possuem essa complexidade.
- **Ampla aplicabilidade**: Comum em cenários onde é necessário processar grandes volumes de dados com um custo computacional moderado.

!!! tip "Dica"
    Algoritmos O(n log n) são frequentemente usados para resolver problemas que envolvem grandes quantidades de dados com uma complexidade razoável.

### 4.3. Exemplos de O(n log n)

#### 4.3.1. Merge Sort

O Merge Sort é um algoritmo de ordenação que divide a entrada em partes menores, ordena cada parte e as combina. Sua complexidade é O(n log n).

```python
def merge_sort(array):
    if len(array) > 1:
        meio = len(array) // 2
        esquerda = array[:meio]
        direita = array[meio:]

        merge_sort(esquerda)
        merge_sort(direita)

        i = j = k = 0

        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                array[k] = esquerda[i]
                i += 1
            else:
                array[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            array[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            array[k] = direita[j]
            j += 1
            k += 1

array = [38, 27, 43, 3, 9, 82, 10]
merge_sort(array)
print(array)  # Saída: [3, 9, 10, 27, 38, 43, 82]
```

#### 4.3.2. Quick Sort (melhor caso)

O Quick Sort utiliza uma estratégia de divisão e conquista, onde os elementos são particionados em relação a um pivo. Sua complexidade é O(n log n) no melhor caso.

```python
def quick_sort(array):
    if len(array) <= 1:
        return array

    pivo = array[0]
    menores = [x for x in array[1:] if x <= pivo]
    maiores = [x for x in array[1:] if x > pivo]

    return quick_sort(menores) + [pivo] + quick_sort(maiores)

array = [38, 27, 43, 3, 9, 82, 10]
array = quick_sort(array)
print(array)  # Saída: [3, 9, 10, 27, 38, 43, 82]
```

!!! note "Nota"
    No pior caso, a complexidade do Quick Sort pode ser O(n²), mas isso é mitigado em implementações que escolhem pivos de forma inteligente.

#### 4.3.3. Construção de uma árvore de busca balanceada

Inserir elementos em uma árvore de busca balanceada, como uma AVL ou Red-Black Tree, pode ter complexidade O(n log n) para construir a árvore inteira.

```python
from sortedcontainers import SortedSet

valores = [38, 27, 43, 3, 9, 82, 10]
arvore = SortedSet()

for valor in valores:
    arvore.add(valor)

print(list(arvore))  # Saída: [3, 9, 10, 27, 38, 43, 82]
```

### 4.4. Benefícios do O(n log n)

- **Eficiência em problemas grandes**: Algoritmos com essa complexidade lidam bem com grandes volumes de dados.
- **Ampla aplicação**: Essencial em ordenação eficiente e outras operações fundamentais.

### 4.5. Limitações do O(n log n)

!!! warning "Atenção"
    Algoritmos O(n log n) podem ser sobrecarregados em cenários onde entradas menores podem ser processadas com algoritmos de complexidade linear (O(n)) ou constante (O(1)).

## 5. Guia de uso

1. **Avalie a necessidade**: Identifique se o problema exige a combinação de operações lineares e logarítmicas.
2. **Escolha algoritmos adequados**: Opte por algoritmos como Merge Sort ou Quick Sort quando precisar de alta eficiência em ordenação.
3. **Garanta condições ideais**: Em alguns casos, como no Quick Sort, garanta estratégias de divisão equilibradas para otimizar o desempenho.

!!! example "Exemplo prático"
    Use Merge Sort para ordenar grandes volumes de dados que não podem ser tratados de forma eficiente com algoritmos de complexidade inferior.

## 6. Referências

- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms*. MIT Press.
- Goodrich, M. T., & Tamassia, R. (2014). *Data Structures and Algorithms in Python*. Wiley.
- Sedgewick, R., & Wayne, K. (2011). *Algorithms*. Addison-Wesley.

## 7. Anexos

### 7.1. Glossário

- **Complexidade computacional**: Medida do custo computacional de um algoritmo em termos de tempo ou espaço.
- **Divisão e conquista**: Estratégia algorítmica que divide um problema em subproblemas menores e resolve cada um separadamente.
- **Árvore de busca balanceada**: Estrutura de dados onde a altura da árvore é mantida balanceada para garantir operações eficientes.

### 7.2. Exemplo adicional

Ordenação utilizando Heap Sort, que possui complexidade O(n log n):

```python
import heapq

def heap_sort(array):
    heapq.heapify(array)
    return [heapq.heappop(array) for _ in range(len(array))]

array = [38, 27, 43, 3, 9, 82, 10]
array = heap_sort(array)
print(array)  # Saída: [3, 9, 10, 27, 38, 43, 82]
```

!!! tip "Dica sobre Heap Sort"
    Heap Sort é uma alternativa estável e eficiente para ordenação em cenários onde o uso de estruturas de heap é vantajoso.
