import time
from typing import List

import multtestlib3 as mtl3
import functions


def main():
    cpus = 4

    # Criar a lista "values" usando um loop "for"
    values: List[int] = []
    values2 = []
    values3 = []
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [1, 2]
    fator = 50
    for i in range(0, 1):
        for x in range(1, 51):
            values.append(x)
            values2.append(x + fator)
            fator -= 2

    functions.now()
    start_time = time.time()
    mtl3.test_greater(1, values, "", values2)
    end_time = time.time()
    functions.now()
    elapsed_time = end_time - start_time
    print(f"Tempo gasto: {elapsed_time} segundos.")
    print(values)
    print(values2)


if __name__ == "__main__":
    mtl3.init()
    main()
    mtl3.end()

'''
    mtl3.test_not_in(5, {1, 2, 3, 4, 5})
    mtl3.test_not_in(5, {1, 2, 3, 4})
    mtl3.test_not_in({1, 2, 3}, values2)
    mtl3.test_not_in(7, values)
    mtl3.test_not_in(747, values)
'''
'''
    mtl3.test_in(cpus, carro1, carro2)
    mtl3.test_in(cpus, carro1, carro3)
    mtl3.test_in(cpus, carro2, carro2)
    mtl3.test_in(cpus, carro2, carro3)
    mtl3.test_in(cpus, carro3, carro3)
'''
