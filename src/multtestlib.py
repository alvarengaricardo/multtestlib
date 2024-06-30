# -*- coding: utf-8 -*-
'''
    multtestlib 1.1
    Python package for running unit tests in parallel processing.
    By Ricardo Ribeiro de Alvarenga
       ricardoalvarenga@ita.br

    ITA - Instituto Tecnológico de Aeronáutica - Brasil
          Aeronautics Institute of Thecnology  - Brazil

    June 2024
'''

from datetime import datetime
import threading, os
from concurrent.futures import ThreadPoolExecutor

file_lock = threading.Lock()


def engine1(input_item, expected_item, process_function, operator, test):
    if process_function is not None:
        result = process_function(input_item)
    else:
        result = input_item
    line = line_a(test, process_function, input_item, result, expected_item)
    filepass(line) if operator(result, expected_item) else filefail(line)


def engine2(input_item, expected_item, operator, test):
    line = line_c(test, input_item, expected_item)
    filepass(line) if operator(input_item, expected_item) else filefail(line)


def engine3(input_item, expected_item, input2_item, process_function, operator, test):
    if process_function is not None:
        result = process_function(input_item, input2_item)
    else:
        result = input_item
    line = line_b(test, process_function, input_item, input2_item, result, expected_item)
    filepass(line) if operator(result, expected_item) else filefail(line)


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
    test = "test_equal - "
    dispatcher(cpus, input1, input2, expected, operator, test, process_function)


def test_not_equal(cpus, input1, input2, expected, process_function=None):
    operator = lambda x, y: x != y
    test = "test_not_equal - "
    dispatcher(cpus, input1, input2, expected, operator, test, process_function)


def test_is(cpus, input1, input2, expected, process_function=None):
    operator = lambda x, y: x is y
    test = "test_is - "
    dispatcher(cpus, input1, input2, expected, operator, test, process_function)


def test_is_not(cpus, input1, input2, expected, process_function=None):
    operator = lambda x, y: x is not y
    test = "test_is_not - "
    dispatcher(cpus, input1, input2, expected, operator, test, process_function)


def test_in(cpus, input1, input2, expected, process_function=None):
    operator = lambda x, y: x in y
    test = "test_in - "
    dispatcher(cpus, input1, input2, expected, operator, test, process_function)


def test_not_in(cpus, input1, input2, expected, process_function=None):
    operator = lambda x, y: x not in y
    test = "test_not_in - "
    dispatcher(cpus, input1, input2, expected, operator, test, process_function)


def test_instance(cpus, input1, input2, expected, process_function=None):
    operator = lambda x, y: isinstance(x, y)
    test = "test_instance - "
    dispatcher(cpus, input1, input2, expected, operator, test, process_function)


def test_not_instance(cpus, input1, input2, expected, process_function=None):
    operator = lambda x, y: not isinstance(x, y)
    test = "test_not_instance - "
    dispatcher(cpus, input1, input2, expected, operator, test, process_function)


def test_issubclass(cpus, input1, input2, expected, process_function=None):
    operator = lambda x, y: issubclass(x, y)
    test = "test_issubclass - "
    dispatcher(cpus, input1, input2, expected, operator, test, process_function)


def test_not_issubclass(cpus, input1, input2, expected, process_function=None):
    operator = lambda x, y: not issubclass(x, y)
    test = "test_not_issubclass - "
    dispatcher(cpus, input1, input2, expected, operator, test, process_function)


def test_greater(cpus, input1, input2, expected, process_function=None):
    operator = lambda x, y: x > y
    test = "test_greater - "
    dispatcher(cpus, input1, input2, expected, operator, test, process_function)


def test_greater_equal(cpus, input1, input2, expected, process_function=None):
    operator = lambda x, y: x >= y
    test = "test_greater_equal - "
    dispatcher(cpus, input1, input2, expected, operator, test, process_function)


def test_less(cpus, input1, input2, expected, process_function=None):
    operator = lambda x, y: x < y
    test = "test_less - "
    dispatcher(cpus, input1, input2, expected, operator, test, process_function)


def test_less_equal(cpus, input1, input2, expected, process_function=None):
    operator = lambda x, y: x <= y
    test = "test_less_equal - "
    dispatcher(cpus, input1, input2, expected, operator, test, process_function)


def line_a(test, ff, input, result, expected):
    return f"{test}{ff.__name__} - input: {input} - expected: {expected} - received: {result} - Result: "


def line_b(test, ff, input, input2, result, expected):
    return f"{test}{ff.__name__} - input1: {input} - input2: {input2} - expected: {expected} - received: {result} - Result: "


def line_c(test, input, received):
    return f"{test}input: {input} received: {received} - Result: "


def get_date_time():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


def init():
    if os.path.exists('filetot.txt'):
        os.remove('filetot.txt')

    if os.path.exists('filepass.txt'):
        os.remove('filepass.txt')

    if os.path.exists('filefail.txt'):
        os.remove('filefail.txt')


def end():
    current_datetime = get_date_time()
    if os.path.exists('filetot.txt'):
        with open('filetot.txt') as f:
            tl = len(f.readlines())
            print(f'Total: {tl}')
            with open('filetot.txt', 'a') as ft:
                ft.write(f'\nTotal: {tl}\n{current_datetime}\n')
    if os.path.exists('filepass.txt'):
        with open('filepass.txt') as f:
            tl = len(f.readlines())
            print(f'Passed: {tl}')
            with open('filepass.txt', 'a') as fp:
                fp.write(f'\nPassed: {tl}\n{current_datetime}\n')
    if os.path.exists('filefail.txt'):
        with open('filefail.txt') as f:
            tl = len(f.readlines())
            print(f'Failed: {tl}')
            with open('filefail.txt', 'a') as ff:
                ff.write(f'\nFailed: {tl}\n{current_datetime}\n')


def filepass(line):
    line = line + 'Pass'
    ft = open('filetot.txt', 'a')
    ft.write(line + '\n')
    fp = open('filepass.txt', 'a')
    fp.write(line + '\n')
    print(line)


def filefail(line):
    line = line + 'Fail'
    ft = open('filetot.txt', 'a')
    ft.write(line + '\n')
    ff = open('filefail.txt', 'a')
    ff.write(line + '\n')
    print(line)


def max_cpu():
    try:
        return os.cpu_count()
    except NotImplementedError:
        return 1


def about():
    print("")
    print("")
    print(" Multtestlib,")
    print(" a package developed for performing unit tests in Python using multiprocessing.")
    print("")
    print(" Author:  Ricardo Ribeiro de Alvarenga")
    print("          ricardoalvarenga@ita.br")
    print("          ITA - Instituto Tecnológico de Aeronáutica")
    print("          Brazil")
    print("")
    print(" Version: 1.1 - June 2024")
    print("          https://pypi.org/project/multtestlib/")
    print("")
    print("")


def help():
    print("")
    print("-----------------------------------------------")
    print("Multtestlib Command       Test")
    print("-----------------------------------------------")
    print("test_equal                x == y")
    print("test_not_equal            x != y")
    print("test_is                   x is y")
    print("test_is_not               x is not y")
    print("test_greater              x > y")
    print("test_greater_equal        x >= y")
    print("test_less                 x < y")
    print("test_less_equal           x <= y")
    print("test_in                   x in y")
    print("test_not_in               x not in y")
    print("test_instance             isinstance(x, y)")
    print("test_not_instance         not isinstance(x, y)")
    print("test_issubclass           issubclass(x, y)")
    print("test_not_issubclass       not issubclass(x, y)")
    print("-----------------------------------------------")
    print("Additional Commands:")
    print("max_cpu()      Detects the number of CPU cores.")
    print("about()          Information about multtestlib.")
    print("help()                 Displays the help table.")
    print("-----------------------------------------------")
    print("")
