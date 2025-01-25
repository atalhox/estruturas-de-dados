# Complexidade Quadrática - O(n²)

## 1. Introdução

A notação Big O é amplamente utilizada em análise de algoritmos para descrever o comportamento de funções computacionais em termos de eficiência e escalabilidade.

!!! info "Nota"
    O termo O(n²), ou complexidade quadrática, caracteriza algoritmos cuja quantidade de operações cresce proporcionalmente ao quadrado do tamanho da entrada.

    Essa complexidade é comum em algoritmos que utilizam laços aninhados para processar cada par de elementos de um conjunto de dados.

## 2. Objetivo

Este documento tem como objetivo apresentar uma descrição detalhada da notação O(n²), explorando sua definição, características, exemplos de aplicação e boas práticas para utilização em análise de algoritmos.

## 3. Público-alvo

Este material é destinado a estudantes, desenvolvedores e profissionais da área de tecnologia da informação, com conhecimento básico em estrutura de dados e algoritmos, que desejam compreender ou aprofundar o estudo sobre análise de complexidade computacional.

## 4. Conteúdo

### 4.1. Definição de O(n²)

A complexidade O(n²) descreve algoritmos cuja quantidade de operações aumenta proporcionalmente ao quadrado do tamanho da entrada. Isso ocorre porque, para cada elemento, o algoritmo realiza operações sobre todos os outros elementos.

#### 4.1.1. Por que um `for` dentro de outro `for` resulta em O(n²)?

Quando usamos um **`for` dentro de outro `for`**, o algoritmo precisa repetir operações múltiplas vezes para cada elemento da lista ou conjunto de dados. Isso significa que:

1. O primeiro `for` percorre cada elemento uma vez.
2. Para cada elemento do primeiro `for`, o  segundo `for` percorre novamente todos os elementos restantes.

O número total de operações acaba sendo proporcional ao número de combinações de elementos, o que equivale a `n` vezes `n`, ou seja, **quadrático**.

#### 4.1.2. Exemplo intuitivo

Imagine que você está em uma sala com `n` pessoas e quer que cada pessoa dê um "aperto de mão" com todas as outras. Para cada pessoa:

- Ela aperta a mão de todas as outras `n-1`.
- No final, o número total de apertos de mão será proporcional a `n²`.

#### 4.1.3. Código de exemplo

```python
for i in range(len(lista)):
    for j in range(i + 1, len(lista)):
        # Aqui cada par (i, j) é comparado
        if lista[i] == lista[j]:
            print(f"Duplicata encontrada: {lista[i]}")
```

!!! tip "Dica"

    Essa abordagem é funcional, mas pode se tornar muito lenta para listas grandes, já que o número de operações cresce rapidamente.

### 4.2. Características

- **Crescimento exponencial com a entrada**: Pequenos aumentos no tamanho da entrada resultam em grandes aumentos no tempo de execução.
- **Simples de implementar**: Muitas soluções iniciais de algoritmos utilizam essa abordagem pela facilidade de codificação.
- **Baixa escalabilidade**: Algoritmos O(n²) tornam-se rapidamente inviáveis para grandes conjuntos de dados.

!!! warning "Atenção"
    Para entradas grandes, algoritmos O(n²) podem ser extremamente ineficientes. Substituí-los por algoritmos mais eficientes é fundamental.

### 4.3. Exemplos de O(n²)

#### 4.3.1. Ordenação por Inserção (Insertion Sort)

O Insertion Sort é um algoritmo de ordenação onde cada elemento é comparado com os anteriores e inserido na posição correta. Sua complexidade no pior caso é O(n²).

```python
def insertion_sort(array):
    for i in range(1, len(array)):
        chave = array[i]
        j = i - 1

        while j >= 0 and chave < array[j]:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = chave

array = [38, 27, 43, 3, 9, 82, 10]
insertion_sort(array)
print(array)  # Saída: [3, 9, 10, 27, 38, 43, 82]
```

#### 4.3.2. Multiplicação de Matrizes (Método Ingênuo)

A multiplicação de duas matrizes utiliza laços aninhados para calcular cada elemento do produto, resultando em complexidade O(n²) para matrizes quadradas.

```python
def multiplica_matrizes(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
resultado = multiplica_matrizes(A, B)
print(resultado)  # Saída: [[19, 22], [43, 50]]
```

#### 4.3.3. Comparação de Todos os Pares

Um algoritmo que compara todos os pares de elementos em um conjunto também possui complexidade O(n²).

```python
def compara_todos_pares(array):
    for i in range(len(array)):
        for j in range(len(array)):
            print(f"Comparando {array[i]} com {array[j]}")

array = [1, 2, 3]
compara_todos_pares(array)
```

!!! note "Nota sobre Comparações"
    A comparação de todos os pares é útil em problemas de similaridade ou distância entre elementos, mas alternativas mais eficientes podem existir.

### 4.4. Benefícios do O(n²)

- **Fácil de implementar**: Algoritmos quadráticos são muitas vezes a solução inicial mais intuitiva.
- **Adequado para entradas pequenas**: Quando os dados são limitados, o impacto de O(n²) é menos perceptível.

### 4.5. Limitações do O(n²)

!!! warning "Atenção"
    Para entradas maiores, algoritmos O(n²) podem ser significativamente mais lentos do que alternativas mais eficientes, como algoritmos O(n log n).

## 5. Guia de uso

1. **Avalie a necessidade**: Use algoritmos O(n²) apenas para entradas pequenas ou onde não existam alternativas mais eficientes.
2. **Substitua quando possível**: Explore algoritmos mais eficientes para reduzir o tempo de execução.
3. **Otimize laços aninhados**: Reduza o número de operações dentro dos laços sempre que possível.

!!! example "Exemplo prático"
    Substitua o Insertion Sort por algoritmos de ordenação mais rápidos, como Merge Sort, em cenários com grandes volumes de dados.

## 6. Referências

- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms*. MIT Press.
- Goodrich, M. T., & Tamassia, R. (2014). *Data Structures and Algorithms in Python*. Wiley.
- Sedgewick, R., & Wayne, K. (2011). *Algorithms*. Addison-Wesley.

## 7. Anexos

### 7.1. Glossário

- **Complexidade computacional**: Medida do custo computacional de um algoritmo em termos de tempo ou espaço.
- **Laço aninhado**: Estrutura onde um laço é executado dentro de outro, frequentemente resultando em complexidade quadrática.
- **Matriz**: Estrutura de dados bidimensional usada para armazenar valores em linhas e colunas.

### 7.2. Exemplo adicional

Verificação de elementos duplicados em uma lista utilizando comparação de todos os pares:

```python
def verifica_duplicados(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                return True
    return False

array = [1, 2, 3, 4, 2]
print(verifica_duplicados(array))  # Saída: True
```

!!! tip "Dica sobre Duplicados"
    Para listas grandes, considere usar estruturas como tabelas hash para verificar duplicados de forma mais eficiente.
