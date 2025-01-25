import time

# Funções de pesquisa
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

def pesquisa_linear(array, elemento):
    for i in range(len(array)):
        if array[i] == elemento:
            return i
    return -1

# Função para simular tempos de execução com time
def simular_tempos():
    tamanhos = [10, 100, 1000, 10000, 100000]  # Diferentes tamanhos de array
    elemento_procurado = -1  # Pior caso: elemento não está na lista

    print(f"{'Tamanho':<10} {'Binária (s)':<15} {'Linear (s)':<15} {'Melhor':<10}")
    print("-" * 50)

    for tamanho in tamanhos:
        array = list(range(tamanho))  # Gera um array ordenado de 0 até tamanho-1

        # Mede o tempo da pesquisa binária
        inicio_tempo = time.time()
        for _ in range(1000):  # Executa 1000 vezes para média mais estável
            pesquisa_binaria(array, elemento_procurado)
        fim_tempo = time.time()
        tempo_binario = (fim_tempo - inicio_tempo) / 1000

        # Mede o tempo da pesquisa linear
        inicio_tempo = time.time()
        for _ in range(1000):  # Executa 1000 vezes para média mais estável
            pesquisa_linear(array, elemento_procurado)
        fim_tempo = time.time()
        tempo_linear = (fim_tempo - inicio_tempo) / 1000

        # Determina o melhor resultado
        melhor = "Binária" if tempo_binario < tempo_linear else "Linear"

        # Resultado formatado
        print(f"{tamanho:<10} {tempo_binario:.2e}       {tempo_linear:.2e}       {melhor:<10}")

# Executar a simulação
simular_tempos()
