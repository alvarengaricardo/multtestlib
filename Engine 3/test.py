import time
import multtestlib3 as mtl3
import functions


class Carro:
    def __init__(self, cor, portas):
        cor = ""
        portas = ""


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
                values2.append(x+1)
            else:
                values.append(x)
                values2.append(x)
    functions.now()
    start_time = time.time()
    mtl3.test_is(cpus, values, values2)
    mtl3.test_is(cpus, carro1, carro1)
    mtl3.test_is(cpus, carro1, carro2)
    mtl3.test_is(cpus, carro1, carro3)
    mtl3.test_is(cpus, carro2, carro2)
    mtl3.test_is(cpus, carro2, carro3)
    mtl3.test_is(cpus, carro3, carro3)
    end_time = time.time()
    functions.now()
    elapsed_time = end_time - start_time
    print(f"Tempo gasto: {elapsed_time} segundos.")


if __name__ == "__main__":
    mtl3.init()
    main()
    mtl3.end()
