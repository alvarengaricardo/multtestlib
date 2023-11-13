import time
import multtestlib3 as mtl3
import functions


class Carro:
    def __init__(self, cor, portas):
        self.cor = cor
        self.portas = portas


def main():
    cpus = 4

    carro1 = Carro("Preto", 4)
    carro2 = Carro("Preto", 4)
    carro3 = Carro("Vermelho", 2)

    # Criar a lista "values" usando um loop "for"
    values = []
    values2 = []
    for i in range(0, 3):
        for x in range(1, 11):
            if x == 5:
                values.append(x-1)
                values2.append({1, 2, 3})
            else:
                values.append(x)
                values2.append(x)
    functions.now()
    start_time = time.time()

    mtl3.test_not_in(5, {1, 2, 3, 4, 5})
    mtl3.test_not_in(5, {1, 2, 3, 4})
    mtl3.test_not_in({1, 2, 3}, values2)
    mtl3.test_not_in(7, values)
    mtl3.test_not_in(747, values)
    '''
    mtl3.test_in(cpus, carro1, carro2)
    mtl3.test_in(cpus, carro1, carro3)
    mtl3.test_in(cpus, carro2, carro2)
    mtl3.test_in(cpus, carro2, carro3)
    mtl3.test_in(cpus, carro3, carro3)
    '''
    #mtl3.test_equal(cpus, values, values2)
    end_time = time.time()
    functions.now()
    elapsed_time = end_time - start_time
    print(f"Tempo gasto: {elapsed_time} segundos.")


if __name__ == "__main__":
    mtl3.init()
    main()
    mtl3.end()
