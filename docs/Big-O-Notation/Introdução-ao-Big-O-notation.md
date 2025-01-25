# Introdução ao Big-O notation

## 1. Introdução

Big O Notation é uma ferramenta matemática essencial utilizada para descrever a eficiência de algoritmos em termos de tempo de execução ou uso de memória, fornecendo uma visão clara de como eles se comportam conforme o tamanho da entrada (n) cresce.

## 2. Objetivo

O objetivo desta documentação é fornecer um entendimento claro e estruturado sobre Big O Notation, incluindo seus conceitos fundamentais, classificações comuns, exemplos de uso e práticas recomendadas.

O documento também busca auxiliar programadores e estudantes a identificar e otimizar a complexidade de algoritmos.

## 3. Público-alvo

Esta documentação é destinada a:

- Estudantes de computação e áreas correlatas.
- Desenvolvedores iniciantes e intermediários.
- Profissionais que desejam revisar conceitos de eficiência algorítmica.
- Qualquer pessoa interessada em aprender mais sobre avaliação de desempenho de algoritmos.

## 4. Conteúdo

### 4.1. O que é Big O Notation?

Big O Notation é uma maneira de expressar a complexidade de um algoritmo, representando o comportamento de seu tempo de execução ou uso de memória no pior caso, melhor caso ou caso médio.

Ela descreve como o desempenho do algoritmo cresce à medida que o tamanho da entrada (*n*) aumenta.

Essa notação é fundamental na ciência da computação e disciplinas relacionadas, pois permite avaliar a escalabilidade e eficácia de soluções algorítmicas, ajudando no desenvolvimento e na escolha de métodos mais apropriados para problemas específicos.

A principal utilidade do Big O está em sua capacidade de expressar o comportamento assintótico dos algoritmos, ou seja, como eles respondem a entradas muito grandes, independentemente de fatores como hardware ou implementações específicas.

Ele classifica algoritmos em categorias, como O(1) (constante), O(log n) (logarítmica), O(n) (linear), O(n log n), O(n²) (quadrática), entre outras, cada uma representando um padrão de crescimento distinto.

No entanto, é importante ressaltar que Big O mede a escalabilidade do algoritmo, ou seja, sua eficiência relativa ao crescimento da entrada, e não diretamente sua performance.

Por exemplo, um algoritmo classificado como O(n) não é necessariamente mais rápido que outro de O(n²) em todos os casos.

Isso porque a notação não considera constantes ou fatores externos como otimizações específicas no código ou hardware. Para determinar qual algoritmo é mais rápido na prática, é necessária uma análise mais detalhada, frequentemente chamada de análise assintótica, que considera as constantes ocultas e as condições reais de execução.

Além disso, o Big O é usado para identificar gargalos em sistemas e prever a viabilidade de um algoritmo em aplicações de grande escala.

Ele serve como uma linguagem universal para desenvolvedores e cientistas de dados discutirem e compararem abordagens, promovendo um entendimento claro e objetivo das implicações algorítmicas.

### 4.2. Casos de Complexidade

- **Melhor caso:** Cenário em que o algoritmo tem o menor tempo de execução possível.
- **Pior caso:** Cenário em que o algoritmo apresenta o maior tempo de execução.
- **Caso médio:** Uma estimativa do tempo de execução para entradas aleatórias.

### 4.3. Como calcular a Big O Notation

Calcular a Big O Notation envolve identificar o número de operações realizadas pelo algoritmo em função do tamanho da entrada.

Os principais passos incluem:

1. Contar o número de operações realizadas em cada instrução relevante.
2. Eliminar termos menos significativos.
3. Focar no termo de maior crescimento.
4. Ignorar constantes.

### 4.4. Práticas recomendadas

- Priorize algoritmos com menor complexidade para entradas grandes.
- Utilize perfis de desempenho para identificar gargalos.
- Considere a estrutura de dados utilizada, pois ela pode impactar significativamente a performance.

### 4.5. Escalabilidade vs performance

A diferença entre escalabilidade e performance em relação à notação Big-O está no que cada conceito busca descrever e como ele se relaciona ao comportamento de um sistema ou algoritmo.

#### 4.5.1. Escalabilidade (Scalability)

Escalabilidade é a **capacidade de um algoritmo ou sistema lidar com o aumento do tamanho da entrada (input)** sem degradação significativa. A notação Big-O é amplamente usada para descrever a escalabilidade, porque ela indica como o tempo de execução ou o uso de recursos (como memória) cresce em relação ao tamanho da entrada `n`.

**Exemplo**

Um algoritmo com complexidade O(n) é mais escalável do que um com O(n²), porque seu crescimento em tempo de execução é linear, enquanto o outro cresce quadraticamente.

**Escalabilidade foca no crescimento**: queremos saber como o algoritmo se comporta quando a entrada cresce para tamanhos maiores, ignorando constantes e fatores de escala.

#### 4.5.2. Performance

Performance refere-se à **eficiência prática de um algoritmo ou sistema em um contexto específico**, incluindo fatores como o tempo de execução real, o uso de memória ou a latência para entradas de tamanhos específicos.

A notação Big-O não mede performance diretamente, porque ela ignora constantes e fatores de implementação que influenciam a eficiência prática.

**Exemplo**

Um algoritmo com `O(n)` pode ser mais lento em prática do que um com `O(n²)` para entradas pequenas, dependendo de fatores como:

- Constantes escondidas em O, por exemplo, `O(100n)` pode ser pior do que `O(n²)` para `n < 100`.
- Otimizações do código ou da infraestrutura.

**Performance foca no comportamento prático.** Queremos saber o quão rápido é o algoritmo na realidade, considerando a entrada e o ambiente em que ele é executado.

##### 4.5.3. Resumo

| Aspecto            | **Escalabilidade**                   | **Performance**                    |
|---------------------|---------------------------------------|-------------------------------------|
| **O que avalia?**   | Crescimento com o tamanho da entrada. | Eficiência em cenários reais.      |
| **Medida usada?**   | Notação Big-O.                       | Tempo real, memória, latência etc. |
| **Ignora...**       | Constantes e otimizações práticas.    | Crescimento assintótico.           |
| **Pergunta-chave**  | Como o algoritmo se comporta para entradas maiores? | O quão rápido é o algoritmo na prática? |

## 5. Guia de uso

1. **Identifique o algoritmo**: Analise o problema e escolha um algoritmo adequado.
2. **Calcule a complexidade**: Determine a Big O Notation de diferentes soluções.
3. **Compare alternativas**: Escolha a solução com melhor equilíbrio entre desempenho e simplicidade.
4. **Teste o algoritmo**: Use entradas grandes para avaliar o comportamento real.
5. **Otimize se necessário**: Refatore o código para reduzir a complexidade.

## 6. Referências

- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms*. MIT Press.
- Sedgewick, R., & Wayne, K. (2011). *Algorithms*. Addison-Wesley.
- Khan Academy. "Algoritmos e Eficiência". Disponível em: [https://www.khanacademy.org/](https://www.khanacademy.org/)
- Stack Overflow. "What is Big O notation?". Disponível em: [https://stackoverflow.com/](https://stackoverflow.com/)
