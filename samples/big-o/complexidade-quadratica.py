import time

# Função para verificar duplicatas (O(n^2))
def verificar_duplicatas(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                return True  # Encontrou duplicata
    return False  # Não há duplicatas

# Simulação para medir tempos de execução
def simular_quadratica():
    tamanhos = [10, 100, 500, 1000, 10000]  # Diferentes tamanhos de lista

    print(f"{'Tamanho':<10} {'Quadrática (s)':<15}")
    print("-" * 30)

    for tamanho in tamanhos:
        array = list(range(tamanho))  # Gera uma lista de números únicos

        # Mede o tempo de execução
        inicio_tempo = time.time()
        for _ in range(3):  # Executa 3 vezes para média mais estável
            verificar_duplicatas(array)
        fim_tempo = time.time()
        tempo_quadratico = (fim_tempo - inicio_tempo) / 3

        # Resultado formatado
        print(f"{tamanho:<10} {tempo_quadratico:.2e}")

# Executar a simulação
simular_quadratica()
