import time
import random

# Merge Sort
def merge_sort(array):
    if len(array) <= 1:
        return array

    meio = len(array) // 2
    esquerda = merge_sort(array[:meio])
    direita = merge_sort(array[meio:])

    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado

# Quick Sort
def quick_sort(array):
    if len(array) <= 1:
        return array
    pivo = array[len(array) // 2]
    menores = [x for x in array if x < pivo]
    iguais = [x for x in array if x == pivo]
    maiores = [x for x in array if x > pivo]
    return quick_sort(menores) + iguais + quick_sort(maiores)

# Simulação dos tempos
def simular_merge_quick_sort():
    tamanhos = [10, 100, 1000, 10000, 100000]  # Diferentes tamanhos de array

    print(f"{'Tamanho':<10} {'Merge Sort (s)':<15} {'Quick Sort (s)':<15} {'Melhor':<10}")
    print("-" * 50)

    for tamanho in tamanhos:
        array = random.sample(range(tamanho), tamanho)  # Array aleatório

        # Mede o tempo do Merge Sort
        inicio_tempo = time.time()
        for _ in range(3):  # Executa 3 vezes para média mais estável
            merge_sort(array)
        fim_tempo = time.time()
        tempo_merge = (fim_tempo - inicio_tempo) / 3

        # Mede o tempo do Quick Sort
        inicio_tempo = time.time()
        for _ in range(3):  # Executa 3 vezes para média mais estável
            quick_sort(array)
        fim_tempo = time.time()
        tempo_quick = (fim_tempo - inicio_tempo) / 3

        # Determina o melhor resultado
        melhor = "Merge" if tempo_merge < tempo_quick else "Quick"

        # Resultado formatado
        print(f"{tamanho:<10} {tempo_merge:.2e}       {tempo_quick:.2e}       {melhor:<10}")

# Executar a simulação
simular_merge_quick_sort()
