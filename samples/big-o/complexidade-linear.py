import time

# Função de soma linear (O(n))
def soma_linear(array):
    soma = 0
    for elemento in array:
        soma += elemento
    return soma

# Função para simular tempos de execução com operações O(n)
def simular_linear():
    tamanhos = [10, 100, 1000, 10000, 100000, 1000000]  # Diferentes tamanhos de array

    print(f"{'Tamanho':<10} {'Linear (s)':<15}")
    print("-" * 30)

    for tamanho in tamanhos:
        array = list(range(tamanho))  # Gera um array de 0 até tamanho-1

        # Mede o tempo de uma operação O(n)
        inicio_tempo = time.time()
        for _ in range(10):  # Executa 10 vezes para média mais estável
            soma_linear(array)
        fim_tempo = time.time()
        tempo_linear = (fim_tempo - inicio_tempo) / 10

        # Resultado formatado
        print(f"{tamanho:<10} {tempo_linear:.2e}")

# Executar a simulação
simular_linear()
