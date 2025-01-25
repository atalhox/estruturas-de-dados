# Introdução ao Big O Notation

## 1. Introdução

A notação Big O é uma ferramenta matemática essencial utilizada para descrever a eficiência de algoritmos em termos de tempo de execução ou uso de memória, fornecendo uma visão clara de como eles se comportam conforme o tamanho da entrada (*n*) cresce.

!!! info "Nota"
    Big O Notation mede como o desempenho de um algoritmo cresce em relação ao tamanho da entrada, ajudando a prever a escalabilidade e identificar soluções mais eficientes.

## 2. Objetivo

Esta documentação tem como objetivo fornecer um entendimento claro e estruturado sobre Big O Notation, incluindo seus conceitos fundamentais, classificações comuns, exemplos de uso e práticas recomendadas.

Ela busca auxiliar programadores e estudantes a identificar e otimizar a complexidade de algoritmos, promovendo escolhas informadas no desenvolvimento de soluções.

## 3. Público-alvo

Esta documentação é destinada a:

- **Estudantes** de computação e áreas correlatas.
- **Desenvolvedores iniciantes e intermediários**.
- **Profissionais** interessados em revisitar conceitos de eficiência algorítmica.
- Qualquer pessoa interessada em entender a análise de desempenho de algoritmos.

## 4. Conteúdo

### 4.1. O que é Big O Notation?

Big O Notation é uma maneira de expressar a complexidade de um algoritmo, representando o comportamento do seu tempo de execução ou uso de memória em função do tamanho da entrada (*n*).

!!! tip "Dica"
    Big O ajuda a entender a escalabilidade dos algoritmos, descrevendo como eles se comportam com entradas muito grandes, independentemente de fatores como hardware ou implementações específicas.

### 4.2. Casos de Complexidade

- **Melhor caso:** Cenário em que o algoritmo tem o menor tempo de execução possível.
- **Pior caso:** Cenário em que o algoritmo apresenta o maior tempo de execução.
- **Caso médio:** Uma estimativa do tempo de execução para entradas aleatórias.

!!! warning "Atenção"
    O pior caso é geralmente usado em análises porque garante que o algoritmo funcionará eficientemente em qualquer situação.

### 4.3. Como calcular a Big O Notation

Calcular a Big O Notation envolve identificar o número de operações realizadas pelo algoritmo em função do tamanho da entrada. Os passos incluem:

1. **Contar o número de operações** realizadas em cada instrução relevante.
2. **Eliminar termos menos significativos**.
3. **Focar no termo de maior crescimento**.
4. **Ignorar constantes**.

!!! example "Exemplo prático"
    Considere um algoritmo que percorre uma lista de tamanho *n* duas vezes. Sua complexidade é O(2n), mas as constantes são ignoradas, resultando em O(n).

### 4.4. Classificações Comuns

As principais classificações da Big O incluem:

- **O(1)**: Tempo constante.
- **O(log n)**: Tempo logarítmico.
- **O(n)**: Tempo linear.
- **O(n log n)**: Tempo linear-logarítmico.
- **O(n²)**: Tempo quadrático.
- **O(2ⁿ)**: Tempo exponencial.

!!! note "Nota"
    Cada classificação representa um padrão de crescimento distinto, adequado para diferentes tipos de problemas.

### 4.5. Escalabilidade vs Performance

A diferença entre escalabilidade e performance está em como cada conceito avalia o comportamento de um algoritmo:

| Aspecto            | **Escalabilidade**                   | **Performance**                    |
|---------------------|---------------------------------------|-------------------------------------|
| **O que avalia?**   | Crescimento com o tamanho da entrada. | Eficiência em cenários reais.      |
| **Medida usada?**   | Notação Big-O.                       | Tempo real, memória, latência etc. |
| **Ignora...**       | Constantes e otimizações práticas.    | Crescimento assintótico.           |
| **Pergunta-chave**  | Como o algoritmo reage a entradas maiores? | Quão rápido é o algoritmo na prática? |

!!! tip "Dica"
    Para grandes volumes de dados, priorize algoritmos com melhor escalabilidade, mesmo que a performance inicial seja inferior.

## 5. Guia de Uso

1. **Entenda o problema**: Analise as necessidades de desempenho e escalabilidade.
2. **Escolha o algoritmo certo**: Identifique soluções compatíveis com o cenário.
3. **Calcule a complexidade**: Avalie o comportamento assintótico para prever a eficiência.
4. **Teste em cenários reais**: Execute com entradas grandes para validar a performance.
5. **Otimize quando necessário**: Refatore algoritmos ou use estruturas de dados mais eficientes.

!!! success "Boas práticas"
    - Perfis de desempenho ajudam a identificar gargalos.
    - Escolha estruturas de dados que se alinhem ao problema.
    - Priorize soluções escaláveis para aplicações de grande escala.

## 6. Referências

- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms*. MIT Press.
- Sedgewick, R., & Wayne, K. (2011). *Algorithms*. Addison-Wesley.
- Khan Academy. "Algoritmos e Eficiência". Disponível em: [https://www.khanacademy.org/](https://www.khanacademy.org/)
- Stack Overflow. "What is Big O notation?". Disponível em: [https://stackoverflow.com/](https://stackoverflow.com/)

## 7. Anexos

### 7.1. Glossário

- **Complexidade computacional**: Medida do custo computacional de um algoritmo em termos de tempo ou espaço.
- **Análise assintótica**: Estudo do comportamento de algoritmos em função de entradas muito grandes.
- **Escalabilidade**: Capacidade de um sistema ou algoritmo lidar com o aumento do tamanho da entrada.

### 7.2. Exemplo adicional

Identificação da complexidade de um algoritmo:

```python
def exemplo_algoritmo(array):
    for i in array:  # O(n)
        for j in array:  # O(n)
            print(i, j)  # Operação constante O(1)

# Complexidade final: O(n * n) = O(n²)
```

!!! tip "Dica sobre análise"
    Sempre foque no termo de maior crescimento para determinar a complexidade final.
