import time

# Cálculo da sequência de Fibonacci de forma recursiva (O(2^n))
def fibonacci_recursivo(n):
    if n <= 1:
        return n
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

# Simulação para medir tempos de execução exponenciais
def simular_exponencial():
    valores = [1,2,5, 10, 20, 30, 40]  # Diferentes valores de 'n' para simulação

    print(f"{'Valor de n':<12} {'Tempo (s)':<10}")
    print("-" * 25)

    for n in valores:
        inicio_tempo = time.time()
        fibonacci_recursivo(n)  # Executa o cálculo exponencial
        fim_tempo = time.time()

        # Calcula o tempo de execução
        tempo_exponencial = fim_tempo - inicio_tempo

        # Resultado formatado
        print(f"{n:<12} {tempo_exponencial:.2e}")

# Executar a simulação
simular_exponencial()
