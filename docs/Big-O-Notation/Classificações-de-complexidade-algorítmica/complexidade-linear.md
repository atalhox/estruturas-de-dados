# Complexidade Linear - O(n)

## 1. Introdução

A notação Big O é amplamente utilizada em análise de algoritmos para descrever o comportamento de funções computacionais em termos de eficiência e escalabilidade.

!!! info "Nota"
    O termo O(n), ou complexidade linear, descreve algoritmos ou operações cuja quantidade de operações necessárias cresce proporcionalmente ao tamanho da entrada.

## 2. Objetivo

Este documento tem como objetivo apresentar uma descrição detalhada da notação O(n), explorando sua definição, características, exemplos de aplicação e boas práticas para utilização em análise de algoritmos.

## 3. Público-alvo

Este material é destinado a estudantes, desenvolvedores e profissionais da área de tecnologia da informação, com conhecimento básico em estrutura de dados e algoritmos, que desejam aprofundar seu entendimento sobre análise de complexidade computacional.

## 4. Conteúdo

### 4.1. Definição de O(n)

O(n), ou complexidade linear, descreve situações em que a quantidade de operações necessárias para executar uma tarefa é proporcional ao tamanho da entrada.

!!! tip "Dica"
    Isso significa que, para cada novo elemento na entrada, uma operação adicional é realizada.

### 4.2. Características

- **Proporcionalidade direta**: O tempo de execução aumenta linearmente com o tamanho da entrada.
- **Previsibilidade**: O desempenho é fácil de estimar com base no tamanho da entrada.
- **Operações completas**: Algoritmos O(n) geralmente processam todos os elementos da entrada pelo menos uma vez.

!!! success "Benefício Importante"
    Algoritmos O(n) são eficientes em muitos cenários onde é necessário processar todos os dados.

### 4.3. Exemplos de O(n)

#### 4.3.1. Percorrer um array

Ao iterar por todos os elementos de um array, a complexidade é O(n), pois cada elemento é acessado exatamente uma vez.

```python
array = [10, 20, 30, 40, 50]
for elemento in array:
    print(elemento)
```

#### 4.3.2. Busca linear

Na busca linear, todos os elementos são comparados até que o elemento desejado seja encontrado ou que o final da lista seja alcançado.

```python
def busca_linear(array, elemento):
    for i in range(len(array)):
        if array[i] == elemento:
            return i  # Elemento encontrado
    return -1  # Elemento não encontrado

array = [10, 20, 30, 40, 50]
print(busca_linear(array, 40))  # Saída: 3
```

#### 4.3.3. Soma de elementos de uma lista

Somar todos os elementos de uma lista exige que cada elemento seja acessado uma vez, resultando em complexidade O(n).

```python
def soma_lista(array):
    soma = 0
    for elemento in array:
        soma += elemento
    return soma

array = [10, 20, 30, 40, 50]
print(soma_lista(array))  # Saída: 150
```

!!! note "Nota"
    Algoritmos que percorrem toda a entrada geralmente possuem complexidade O(n).

### 4.4. Benefícios do O(n)

- **Simplicidade**: Algoritmos lineares são mais fáceis de implementar e entender.
- **Escalabilidade razoável**: Embora não tão eficientes quanto O(1) ou O(log n), algoritmos O(n) são adequados para uma ampla gama de aplicações.

### 4.5. Limitações do O(n)

!!! warning "Atenção"
    Para entradas extremamente grandes, o tempo de execução pode se tornar um gargalo, especialmente em aplicações que requerem alta performance.

## 5. Guia de uso

1. **Analise a necessidade**: Determine se é necessário processar todos os elementos da entrada.
2. **Evite redundâncias**: Reduza operações desnecessárias para otimizar o desempenho.
3. **Considere estruturas adequadas**: Algumas estruturas de dados podem melhorar o desempenho em cenários específicos.

!!! example "Exemplo prático"
    Use a busca linear para localizar elementos em listas pequenas ou desordenadas.

## 6. Referências

- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms*. MIT Press.
- Goodrich, M. T., & Tamassia, R. (2014). *Data Structures and Algorithms in Python*. Wiley.
- Sedgewick, R., & Wayne, K. (2011). *Algorithms*. Addison-Wesley.

## 7. Anexos

### 7.1. Glossário

- **Complexidade computacional**: Medida do custo computacional de um algoritmo em termos de tempo ou espaço.
- **Busca linear**: Estratégia de busca que verifica cada elemento da entrada sequencialmente.
- **Array**: Estrutura de dados linear onde os elementos são armazenados em endereços contíguos.

### 7.2. Exemplo adicional

Multiplicação de todos os elementos de uma lista:

```python
def multiplica_lista(array):
    produto = 1
    for elemento in array:
        produto *= elemento
    return produto

array = [1, 2, 3, 4, 5]
print(multiplica_lista(array))  # Saída: 120
```

!!! tip "Dica sobre Listas"
    Listas são ideais para armazenar sequências de elementos onde a ordem importa e é necessário iterar frequentemente.
