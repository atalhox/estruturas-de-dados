# Complexidade constante - O(1)

## 1. Introdução

A notação Big O é amplamente utilizada em análise de algoritmos para descrever o comportamento de funções computacionais em termos de eficiência e escalabilidade.

O termo O(1), ou tempo constante, é uma das classificações mais simples e importantes nessa notção.

Ele descreve algoritmos ou operações cuja complexidade permanece a mesma independentemente do tamanho da entrada.

## 2. Objetivo

Este documento tem como objetivo apresentar uma descrição detalhada da notção O(1), explorando sua definição, características, exemplos de aplicação e boas práticas para utilização em análise de algoritmos.

## 3. Público-alvo

Este material é destinado a estudantes, desenvolvedores e profissionais da área de tecnologia da informação, com conhecimento básico em estrutura de dados e algoritmos, que desejam aprofundar seu entendimento sobre análise de complexidade computacional.

## 4. Conteúdo

### 4.1. Definição de O(1)

O(1), ou tempo constante, descreve situações em que a quantidade de operações necessárias para executar uma tarefa é independente do tamanho da entrada.

Isso significa que, não importa se a entrada possui 1 ou 1.000 elementos, o tempo para concluir a tarefa permanece constante.

### 4.2. Características

- **Independência da entrada**: O desempenho não varia com o tamanho ou a complexidade da entrada.
- **Execução previsível**: A operação ou algoritmo oferece um desempenho estável.
- **Baixa complexidade computacional**: É frequentemente associado a operações de alto desempenho.

### 4.3. Exemplos de O(1)

#### 4.3.1. Acesso direto a um elemento em um array

Ao acessar um elemento específico de um array por índice, a complexidade é O(1), pois o acesso é direto e não depende do tamanho do array.

```python
array = [10, 20, 30, 40, 50]
print(array[2])  # Saída: 30
```

#### 4.3.2. Verificação de uma condição simples

Uma comparação entre duas variáveis também é um exemplo de O(1), pois ocorre em tempo constante independentemente do tamanho dos dados.

```python
x = 10
y = 20
if x < y:
    print("x é menor que y")
```

#### 4.3.3. Inserção em um hash table

Inserir um elemento em uma tabela hash bem projetada, sem colisões, possui complexidade O(1).

```python
hash_table = {}
hash_table["chave"] = "valor"
print(hash_table)
```

### 4.4. Benefícios do O(1)

- **Escalabilidade**: Algoritmos O(1) são altamente escaláveis devido ao seu tempo de execução constante.
- **Eficiência**: Geralmente, são mais eficientes do que algoritmos de maior complexidade, como O(n) ou O(log n).

### 4.5. Limitações do O(1)

Embora O(1) seja extremamente eficiente, sua aplicação é limitada a casos específicos. Nem todas as operações ou algoritmos podem ser implementados com complexidade constante.

## 5. Guia de uso

1. **Identifique operações candidatas**: Procure pontos no código onde a entrada não influencia diretamente o tempo de execução.
2. **Implemente estruturas de dados apropriadas**: Estruturas como tabelas hash ou arrays são frequentemente usadas para operações O(1).
3. **Evite pressupostos irrealistas**: Certifique-se de que as condições para O(1) sejam satisfeitas, como evitar colisões em tabelas hash.

## 6. Referências

- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms*. MIT Press.
- Goodrich, M. T., & Tamassia, R. (2014). *Data Structures and Algorithms in Python*. Wiley.
- Sedgewick, R., & Wayne, K. (2011). *Algorithms*. Addison-Wesley.

## 7. Anexos

### 7.1. Glossário

- **Complexidade computacional**: Medida do custo computacional de um algoritmo em termos de tempo ou espaço.
- **Tabela hash**: Estrutura de dados que mapeia chaves a valores usando uma função hash.
- **Array**: Estrutura de dados linear onde os elementos são armazenados em endereços contíguos.

### 7.2. Exemplo adicional

Inserção em uma pilha utilizando listas em Python:

```python
pilha = []
pilha.append(10)  # Inserção em O(1)
print(pilha)
```
