import time
from typing import List

import multtestlib3 as mtl3
import functions


class Veiculo:
    pass


class Carro(Veiculo):
    def __init__(self, cor, portas):
        self.cor = cor
        self.portas = portas


class Aviao:
    def __init__(self, motor, tipo):
        self.motor = motor
        self.tipo = tipo


def main():
    cpus = 4

    carro1 = Carro("Preto", 4)
    carro2 = Carro("Preto", 4)
    carro3 = Carro("Vermelho", 2)
    aviao1 = Aviao("Jato", "Caça")
    aviao2 = Aviao("Turbo Hélice", "Cargueiro")
    aviao3 = Aviao("Turbo Hélice", "Treinamento")

    # Criar a lista "values" usando um loop "for"
    values: List[int] = []
    values2 = []
    values3 = []
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [1, 2]

    for i in range(0, 1):
        for x in range(1, 11):

            if x == 5:
                values.append(Aviao)
                values2.append(Veiculo)
                # values2.append(10)

            else:
                values.append(Carro)
                values2.append(Veiculo)

            # values.append(x)
            # values2.append(x)
            # values3.append(x + x)

    functions.now()
    start_time = time.time()

    #mtl3.test_not_instance(4, values, "", values2)
    mtl3.test_issubclass(4, values, "", values2)

    end_time = time.time()
    functions.now()
    elapsed_time = end_time - start_time
    print(f"Tempo gasto: {elapsed_time} segundos.")


# print(values)
# print(values2)


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
