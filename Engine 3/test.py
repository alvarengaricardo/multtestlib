import time
import multtestlib3 as mtl3
import functions


def main():
    cpus = 4
# Criar a lista "values" usando um loop "for"
    values = []
    values2 = []
    for i in range(0, 5):
        for x in range(1, 31):
            values.append(x)
            if x == 5:
                values2.append(x-1)
            else:
                values2.append(x)
    functions.now()
    start_time = time.time()
    mtl3.test_is(cpus, values, values2)
    end_time = time.time()
    functions.now()
    elapsed_time = end_time - start_time
    print(f"Tempo gasto: {elapsed_time} segundos.")


if __name__ == "__main__":
    mtl3.init()
    main()
    mtl3.end()

