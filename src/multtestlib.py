# -*- coding: utf-8 -*-
"""
    multtestlib 1.2.1
    Python package for running unit tests in parallel processing.
    By Ricardo Ribeiro de Alvarenga
       ricardoalvarenga@ita.br

    ITA - Instituto Tecnológico de Aeronáutica - Brasil
          Aeronautics Institute of Thecnology  - Brazil

    October 2025
"""
import os
import threading
from concurrent.futures import ThreadPoolExecutor
import time
from datetime import datetime

file_lock = threading.Lock()
output_filename = None


def engine1(input_item, expected_item, process_function, operator, test):
    start_time = time.perf_counter()
    if process_function is not None:
        result = process_function(input_item)
    else:
        result = input_item
    execution_time = time.perf_counter() - start_time
    test_passed = operator(result, expected_item)

    file_output(test, process_function.__name__, input_item, "", expected_item, result, test_passed, execution_time)


def engine2(input_item, expected_item, operator, test):
    start_time = time.perf_counter()
    result = input_item
    test_passed = operator(result, expected_item)
    execution_time = time.perf_counter() - start_time
    file_output(test, "No Function", input_item, "", expected_item, result, test_passed, execution_time)


def engine3(input_item, expected_item, input2_item, process_function, operator, test):
    start_time = time.perf_counter()
    if process_function is not None:
        result = process_function(input_item, input2_item)
    else:
        result = input_item
    execution_time = time.perf_counter() - start_time  # Calcula o tempo de execução
    test_passed = operator(result, expected_item)
    file_output(test, process_function.__name__ if process_function else "No Function", input_item, input2_item,
                expected_item, result, test_passed, execution_time)


def dispatcher(cpus, input1, input2, expected, operator, test, process_function=None):
    if input2 == "":
        input2 = None
    if not isinstance(input1, list):
        input1 = [input1]
    if not isinstance(expected, list):
        expected = [expected]
    if process_function is not None and not isinstance(process_function, list):
        process_function = [process_function]

    with ThreadPoolExecutor(max_workers=cpus) as executor:
        if input2 is None and process_function is not None:
            for input_item, expected_item, func in zip(input1, expected, process_function * len(input1)):
                executor.submit(engine1, input_item, expected_item, func, operator, test)
        elif input2 is None and process_function is None:
            for input_item, expected_item in zip(input1, expected):
                executor.submit(engine2, input_item, expected_item, operator, test)
        elif input2 is not None and process_function is not None:
            if not isinstance(input2, list):
                input2 = [input2] * len(input1)
            for input_item, expected_item, input2_item, func in zip(input1, expected, input2,
                                                                    process_function * len(input1)):
                executor.submit(engine3, input_item, expected_item, input2_item, func, operator, test)


def test_equal(cpus, input1, input2, expected, process_function=None):
    operator = lambda x, y: x == y
    test = "test_equal"
    dispatcher(cpus, input1, input2, expected, operator, test, process_function)


def test_not_equal(cpus, input1, input2, expected, process_function=None):
    operator = lambda x, y: x != y
    test = "test_not_equal"
    dispatcher(cpus, input1, input2, expected, operator, test, process_function)


def test_is(cpus, input1, input2, expected, process_function=None):
    operator = lambda x, y: x is y
    test = "test_is"
    dispatcher(cpus, input1, input2, expected, operator, test, process_function)


def test_is_not(cpus, input1, input2, expected, process_function=None):
    operator = lambda x, y: x is not y
    test = "test_is_not"
    dispatcher(cpus, input1, input2, expected, operator, test, process_function)


def test_in(cpus, input1, input2, expected, process_function=None):
    operator = lambda x, y: x in y
    test = "test_in"
    dispatcher(cpus, input1, input2, expected, operator, test, process_function)


def test_not_in(cpus, input1, input2, expected, process_function=None):
    operator = lambda x, y: x not in y
    test = "test_not_in"
    dispatcher(cpus, input1, input2, expected, operator, test, process_function)


def test_instance(cpus, input1, input2, expected, process_function=None):
    operator = lambda x, y: isinstance(x, y)
    test = "test_instance"
    dispatcher(cpus, input1, input2, expected, operator, test, process_function)


def test_not_instance(cpus, input1, input2, expected, process_function=None):
    operator = lambda x, y: not isinstance(x, y)
    test = "test_not_instance"
    dispatcher(cpus, input1, input2, expected, operator, test, process_function)


def test_issubclass(cpus, input1, input2, expected, process_function=None):
    operator = lambda x, y: issubclass(x, y)
    test = "test_issubclass"
    dispatcher(cpus, input1, input2, expected, operator, test, process_function)


def test_not_issubclass(cpus, input1, input2, expected, process_function=None):
    operator = lambda x, y: not issubclass(x, y)
    test = "test_not_issubclass"
    dispatcher(cpus, input1, input2, expected, operator, test, process_function)


def test_greater(cpus, input1, input2, expected, process_function=None):
    operator = lambda x, y: x > y
    test = "test_greater"
    dispatcher(cpus, input1, input2, expected, operator, test, process_function)


def test_greater_equal(cpus, input1, input2, expected, process_function=None):
    operator = lambda x, y: x >= y
    test = "test_greater_equal"
    dispatcher(cpus, input1, input2, expected, operator, test, process_function)


def test_less(cpus, input1, input2, expected, process_function=None):
    operator = lambda x, y: x < y
    test = "test_less"
    dispatcher(cpus, input1, input2, expected, operator, test, process_function)


def test_less_equal(cpus, input1, input2, expected, process_function=None):
    operator = lambda x, y: x <= y
    test = "test_less_equal"
    dispatcher(cpus, input1, input2, expected, operator, test, process_function)


def line_a(test, ff, input, result, expected, execution_time):
    return f"{test}{ff.__name__} - input: {input} - expected: {expected} - received: {result} - Result: "


def line_b(test, ff, input, input2, result, expected, execution_time):
    return f"{test}{ff.__name__} - input1: {input} - input2: {input2} - expected: {expected} - received: {result} - Result: "


def line_c(test, input, received):
    return f"{test}input: {input} received: {received} - Result: "


def file_output(test_name, tested_function, input1, input2, expected, received, test_passed, execution_time):
    # Verifica o status do teste
    status = "Pass" if test_passed else "Fail"
    # Verifica input2 e ajusta se for None
    input2 = input2 if input2 is not None else ""
    # Gera linha final para o arquivo CSV
    final_line_csv = f"{test_name},{tested_function},{input1},{input2},{expected},{received},{status},{execution_time:.15f}\n"
    # Adiciona resultado no arquivo CSV
    with file_lock:
        with open(output_filename, 'a') as ft:
            ft.write(final_line_csv)
    # Exibe no console (sem alterar o formato da saída em tela)
    print(
        f"{test_name} - {tested_function} - Input1: {input1} - Input2: {input2} - Expected: {expected} - Received: {received} - Result: {status} - Execution Time: {execution_time:.9f} sec")


def init():
    global output_filename
    current_datetime = datetime.now().strftime("%Y%m%d-%H%M%S")
    output_filename = f"mtl-{current_datetime}.csv"

    # Remove arquivo anterior, se existir
    if os.path.exists(output_filename):
        os.remove(output_filename)

    # Cria arquivo com cabeçalho
    with open(output_filename, 'w') as ft:
        ft.write("Test Name,Tested,Input1,Input2,Expected,Received,Result,Execution Time (seconds)\n")

    print(f"Initialized output file: {output_filename}")


def end():
    print(f"Test results saved in {output_filename}")


def about():
    print("")
    print("-------------------------------------------------------------")
    print("Multithreaded Test Library - multtestlib 1.2.1")
    print("Developed by Ricardo Ribeiro de Alvarenga, ITA, Brazil")
    print("E-mail: ricardoalvarenga@ita.br")
    print("-------------------------------------------------------------")


def max_cpu():
    return os.cpu_count()


def help():
    print("-------------- Multtestlib 1.2.1 --------------")
    print("Command                 Description")
    print("-----------------------------------------------")
    print("test_equal               x == y")
    print("test_not_equal           x != y")
    print("test_is                  x is y")
    print("test_is_not              x is not y")
    print("test_greater             x > y")
    print("test_greater_equal       x >= y")
    print("test_less                x < y")
    print("test_less_equal          x <= y")
    print("test_in                  x in y")
    print("test_not_in              x not in y")
    print("test_instance            isinstance(x, y)")
    print("test_not_instance        not isinstance(x, y)")
    print("test_issubclass          issubclass(x, y)")
    print("test_not_issubclass      not issubclass(x, y)")
    print("-----------------------------------------------")
    print("Additional Commands:")
    print("max_cpu()      Detects the number of CPU cores.")
    print("about()          Information about multtestlib.")
    print("help()                 Displays the help table.")
    print("-----------------------------------------------")
    print("")
