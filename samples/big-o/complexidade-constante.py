import time

# Função de acesso direto (O(1))
def acesso_constante(array, indice):
    return array[indice]  # Acesso direto ao índice

# Função para simular tempos de execução com operações O(1)
def simular_constante():
    tamanhos = [10, 100, 1000, 10000, 100000, 1000000]  # Diferentes tamanhos de array
    indice_procurado = 0  # Acessa sempre o primeiro elemento (constante)

    print(f"{'Tamanho':<10} {'Constante (s)':<15}")
    print("-" * 30)

    for tamanho in tamanhos:
        array = list(range(tamanho))  # Gera um array de 0 até tamanho-1

        # Mede o tempo de uma operação O(1)
        inicio_tempo = time.time()
        for _ in range(1000000):  # Executa 1 milhão de vezes para estabilidade
            acesso_constante(array, indice_procurado)
        fim_tempo = time.time()
        tempo_constante = (fim_tempo - inicio_tempo) / 1000000

        # Resultado formatado
        print(f"{tamanho:<10} {tempo_constante:.2e}")

# Executar a simulação
simular_constante()
