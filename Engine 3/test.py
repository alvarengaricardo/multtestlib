import time
import multtestlib3 as mtl3
import functions


def main():
    cpus = 1
# Criar a lista "values" usando um loop "for"
    values = []
    values2 = []
    for i in range(0, 5):
        for x in range(1, 31):
            values.append(x)
            values2.append(x + 1)
    functions.now()
    start_time = time.time()
    mtl3.test_not_equal(cpus, values, values2, functions.soma, values)
    end_time = time.time()
    functions.now()
    elapsed_time = end_time - start_time
    print(f"Tempo gasto: {elapsed_time} segundos.")


if __name__ == "__main__":
    mtl3.init()
    main()
    mtl3.end()

