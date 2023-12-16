from concurrent.futures import ThreadPoolExecutor

def verificar_elementos_em_paralelo(elemento, arrayB):
    return elemento in arrayB

def verificar_elementos_em_array(arrayA, arrayB, num_threads=2):
    resultado = []

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        # Mapeia a função verificar_elementos_em_paralelo para cada elemento em arrayA
        # e coleta os resultados
        resultados = list(executor.map(lambda x: verificar_elementos_em_paralelo(x, arrayB), arrayA))

    # Retorna os elementos de arrayA que estão em arrayB
    return [arrayA[i] for i, resultado in enumerate(resultados) if resultado]

# Exemplo de uso
arrayA = [1, 2, 3, 4, 5]
arrayB = [3, 5, 7, 9]

elementos_em_arrayB = verificar_elementos_em_array(arrayA, arrayB)
print("Elementos de arrayA que estão em arrayB:", elementos_em_arrayB)
