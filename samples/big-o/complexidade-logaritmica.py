import time

# Pesquisa binária (O(log n))
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

# Simulação dos tempos de execução para O(log n)
def simular_logaritmica():
    tamanhos = [10, 100, 1000, 10000, 100000, 1000000]  # Diferentes tamanhos de array
    elemento_procurado = -1  # Elemento que não está no array (pior caso)

    print(f"{'Tamanho':<10} {'Logarítmica (s)':<15}")
    print("-" * 30)

    for tamanho in tamanhos:
        array = list(range(tamanho))  # Gera um array ordenado

        # Mede o tempo da pesquisa binária
        inicio_tempo = time.time()
        for _ in range(100000):  # Executa 100.000 vezes para média mais estável
            pesquisa_binaria(array, elemento_procurado)
        fim_tempo = time.time()
        tempo_logaritmico = (fim_tempo - inicio_tempo) / 100000

        # Resultado formatado
        print(f"{tamanho:<10} {tempo_logaritmico:.2e}")

# Executar a simulação
simular_logaritmica()
