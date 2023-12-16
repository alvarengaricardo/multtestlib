'''
    multtestlib 2023.4
    Python package for running unit tests in parallel processing.
    Engine II
    By Ricardo Ribeiro de Alvarenga
       alvarenga.r.ricardo@gmail.com

    ITA - Instituto Tecnológico de Aeronáutica - BRAZIL

    December 2023

'''

from datetime import datetime
import os
from concurrent.futures import ThreadPoolExecutor


def engine1(input_item, expected_item, process_function, operator, test):
    result = process_function(input_item)
    line = line_a(test, process_function, input_item, result, expected_item)
    filepass(line) if operator(result, expected_item) else filefail(line)


def engine2(input_item, expected_item, operator, test):
    # received = input_item
    line = line_c(test, input_item, expected_item)
    filepass(line) if operator(input_item, expected_item) else filefail(line)


def engine3(input_item, expected_item, input2_item, process_function, operator, test):
    result = process_function(input_item, input2_item)
    line = line_b(test, process_function, input_item, input2_item, result, expected_item)
    filepass(line) if operator(result, expected_item) else filefail(line)


def dispatcher(cpus, input1, input2, expected, operator, test, process_function=None):
    if input2 == "":
        input2 = None
    if not isinstance(input1, list):
        input1 = [input1]
    if not isinstance(expected, list):
        expected = [expected]

    if (input2 is None) and (process_function is not None):
        # print("motor 1")
        with ThreadPoolExecutor(max_workers=cpus) as executor:
            for input_item, expected_item in zip(input1, expected):
                executor.submit(engine1, input_item, expected_item, process_function, operator, test)

    if (input2 is None) and (process_function is None):
        with ThreadPoolExecutor(max_workers=cpus) as executor:
            for input_item, expected_item in zip(input1, expected):
                executor.submit(engine2, input_item, expected_item, operator, test)

    if (input2 is not None) and (process_function is not None):
        if not isinstance(input2, list):
            input2 = [input2]
        with ThreadPoolExecutor(max_workers=cpus) as executor:
            for input_item, expected_item, input2_item in zip(input1, expected, input2):
                executor.submit(engine3, input_item, expected_item, input2_item, process_function, operator, test)


def test_equal(cpus, input1, input2, expected, process_function=None):
    # a == b compares the content of the variables, checking if the values are equal.
    operator = lambda x, y: x == y
    test = "test_equal - "
    dispatcher(cpus, input1, input2, expected, operator, test, process_function)


def test_not_equal(cpus, input1, input2, expected, process_function=None):
    operator = lambda x, y: x != y
    test = "test_not_equal - "
    dispatcher(cpus, input1, input2, expected, operator, test, process_function)


def test_is(cpus, input1, input2, expected, process_function=None):
    # a is b compares the identity of the objects, checking if both variables refer to the same object in memory.
    operator = lambda x, y: x is y
    test = "test_is - "
    dispatcher(cpus, input1, input2, expected, operator, test, process_function)


def test_is_not(cpus, input1, input2, expected, process_function=None):
    operator = lambda x, y: x is not y
    test = "test_is_not - "
    dispatcher(cpus, input1, input2, expected, operator, test, process_function)


def test_in(cpus, input1, input2, expected, process_function=None):
    # verifica se input1 existe em alguma posição em input2
    operator = lambda x, y: x in y
    test = "test_in - "
    dispatcher(cpus, input1, input2, expected, operator, test, process_function)


def test_not_in(cpus, input1, input2, expected, process_function=None):
    # verifica se input1 NÃO existe em alguma posição em input2
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
    # Verifica se uma classe B é subclasse de A. Fornecer o nome da classe, não o objeto
    operator = lambda x, y: issubclass(x, y)
    test = "test_issubclass - "
    dispatcher(cpus, input1, input2, expected, operator, test, process_function)


def test_not_issubclass(cpus, input1, input2, expected, process_function=None):
    # Verifica se uma classe B não é subclasse de A. Fornecer o nome da classe, não o objeto
    operator = lambda x, y: not issubclass(x, y)
    test = "test_not_issubclass - "
    dispatcher(cpus, input1, input2, expected, operator, test, process_function)


def test_greater(cpus, input1, input2, expected, process_function=None):
    # Verifica se a > b
    operator = lambda x, y: x > y
    test = "test_greater - "
    dispatcher(cpus, input1, input2, expected, operator, test, process_function)


def test_greater_equal(cpus, input1, input2, expected, process_function=None):
    # Verifica se a >= b
    operator = lambda x, y: x >= y
    test = "test_greater_equal - "
    dispatcher(cpus, input1, input2, expected, operator, test, process_function)


def test_less(cpus, input1, input2, expected, process_function=None):
    # Verifica se a < b
    operator = lambda x, y: x < y
    test = "test_less - "
    dispatcher(cpus, input1, input2, expected, operator, test, process_function)


def test_less_equal(cpus, input1, input2, expected, process_function=None):
    # Verifica se a <= b
    operator = lambda x, y: x <= y
    test = "test_less_equal - "
    dispatcher(cpus, input1, input2, expected, operator, test, process_function)


def line_a(test, ff, input, result, expected):
    # line1('test_equal', process_function, input_item, result, expected_item)
    return (str(test) + str(ff.__name__) + ' - ' + 'input: ' + str(input) + ' - ' + 'expected: ' + str(
        expected) + ' - ' + 'received: ' + str(result) + ' - ' + 'Result: ')


def line_b(test, ff, input, input2, result, expected):
    # line1b('test_equal', process_function, input_item, input2[0], result, expected_item)
    return (str(test) + str(ff.__name__) + ' - ' + 'input1: ' + str(input) + ' - ' + 'input2: ' + str(
        input2) + ' - ' + 'expected: ' + str(
        expected) + ' - ' + 'received: ' + str(result) + ' - ' + 'Result: ')


def line_c(test, input, received):
    return (str(test) + 'input: ' + str(input) + ' received: ' + str(received) + ' - ' + 'Result: ')


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
            print('Total: ' + str(tl))
            ft = open('filetot.txt', 'a')
            ft.write('\n')
            ft.write('Total: ' + str(tl))
            ft.write('\n')
            ft.write(current_datetime)
            ft.close()
    if os.path.exists('filepass.txt'):
        with open('filepass.txt') as f:
            tl = len(f.readlines())
            print('Passed: ' + str(tl))
            fp = open('filepass.txt', 'a')
            fp.write('\n')
            fp.write('Passed: ' + str(tl))
            fp.write('\n')
            fp.write(current_datetime)
            fp.close()
    if os.path.exists('filefail.txt'):
        with open('filefail.txt') as f:
            tl = len(f.readlines())
            print('Failed: ' + str(tl))
            ff = open('filefail.txt', 'a')
            ff.write('\n')
            ff.write('Failed: ' + str(tl))
            ff.write('\n')
            ff.write(current_datetime)
            ff.close()
    global vector


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


def about():
    print("")
    print("*** multtestLib *** ")
    print("")
    print(" Python package for running unit tests in parallel processing.")
    print(" Author: Ricardo Ribeiro de Alvarenga")
    print("         ITA - Instituto Tecnologico de Aeronáutica")
    print("         Brazil")
    print(" Version: 2023.4 (Engine II)")
    print("")


def sos():
    print("")
    print("")
    print("-----------------------------------------------")
    print("Multtestlib Command       Test")
    print("-----------------------------------------------")
    print("test_equal                x == y")
    print("test_not_equal            x != y")
    print("test_is                   x is y")
    print("test_is_not               x is not y")
    print("test_in                   x in y")
    print("test_not_in               x not in y")
    print("test_instance             isinstance(x, y)")
    print("test_not_instance         not isinstance(x, y)")
    print("test_issubclass           issubclass(x, y)")
    print("test_test_not_issubclass  not issubclass(x, y)")
    print("test_greater              x > y")
    print("test_greater_equal        x >= y")
    print("test_less                 x < y")
    print("test_less_equal           x <= y")
    print("-----------------------------------------------")
    print("")
    print("")
