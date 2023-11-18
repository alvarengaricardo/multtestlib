import os
from concurrent.futures import ThreadPoolExecutor


def run_test1(input_item, expected_item, process_function, operator, test):
    result = process_function(input_item)
    line = line1a(test, process_function, input_item, result, expected_item)
    # filepass(line) if result == expected_item else filefail(line)
    filepass(line) if operator(result, expected_item) else filefail(line)


def run_test2(input_item, expected_item, operator, test):
    result = input_item
    line = line1c(test, input_item, result, expected_item)
    # filepass(line) if result == expected_item else filefail(line)
    filepass(line) if operator(result, expected_item) else filefail(line)


def run_test3(input_item, expected_item, input2_item, process_function, operator, test):
    result = process_function(input_item, input2_item)
    line = line1b(test, process_function, input_item, input2_item, result, expected_item)
    # filepass(line) if result == expected_item else filefail(line)
    filepass(line) if operator(result, expected_item) else filefail(line)


# (test, input, expected)
def run_test4(input_item, expected_item, operator, test):
    line = line1d(test, input_item, expected_item)
    filepass(line) if operator(input_item, expected_item) else filefail(line)


def test_equal(cpus, input1, input2, expected, process_function=None):
    # a == b compares the content of the variables, checking if the values are equal.
    operator = lambda x, y: x == y
    test = "test_equal - "

    if input2 == "":
        input2 = None
    if not isinstance(input1, list):
        input1 = [input1]
    if not isinstance(expected, list):
        expected = [expected]

    if (input2 is None) and (process_function is not None):
        with ThreadPoolExecutor(max_workers=cpus) as executor:
            for input_item, expected_item in zip(input1, expected):
                executor.submit(run_test1, input_item, expected_item, process_function, operator, test)

    if (input2 is None) and (process_function is None):
        with ThreadPoolExecutor(max_workers=cpus) as executor:
            for input_item, expected_item in zip(input1, expected):
                executor.submit(run_test2, input_item, expected_item, operator, test)

    if (input2 is not None) and (process_function is not None):
        if not isinstance(input2, list):
            input2 = [input2]
        with ThreadPoolExecutor(max_workers=cpus) as executor:
            for input_item, expected_item, input2_item in zip(input1, expected, input2):
                executor.submit(run_test3, input_item, expected_item, input2_item, process_function, operator, test)


def test_not_equal(cpus, input1, input2, expected, process_function=None):
    operator = lambda x, y: x != y
    test = "test_not_equal - "

    if input2 == "":
        input2 = None
    if not isinstance(input1, list):
        input1 = [input1]
    if not isinstance(expected, list):
        expected = [expected]

    if (input2 is None) and (process_function is not None):
        with ThreadPoolExecutor(max_workers=cpus) as executor:
            for input_item, expected_item in zip(input1, expected):
                executor.submit(run_test1, input_item, expected_item, process_function, operator, test)

    if (input2 is None) and (process_function is None):
        with ThreadPoolExecutor(max_workers=cpus) as executor:
            for input_item, expected_item in zip(input1, expected):
                executor.submit(run_test2, input_item, expected_item, operator, test)

    if (input2 is not None) and (process_function is not None):
        if not isinstance(input2, list):
            input2 = [input2]
        with ThreadPoolExecutor(max_workers=cpus) as executor:
            for input_item, expected_item, input2_item in zip(input1, expected, input2):
                executor.submit(run_test3, input_item, expected_item, input2_item, process_function, operator, test)


# def test_is(a, b):
#    line = line1('teste_is', a, b)
#    filepass(line) if a is b else filefail(line)
def test_is(cpus, input1, input2, expected, process_function=None):
    # a is b compares the identity of the objects, checking if both variables refer to the same object in memory.
    operator = lambda x, y: x is y
    test = "test_is - "

    if input2 == "":
        input2 = None
    if not isinstance(input1, list):
        input1 = [input1]
    if not isinstance(expected, list):
        expected = [expected]

    if (input2 is None) and (process_function is not None):
        with ThreadPoolExecutor(max_workers=cpus) as executor:
            for input_item, expected_item in zip(input1, expected):
                executor.submit(run_test1, input_item, expected_item, process_function, operator, test)

    if (input2 is None) and (process_function is None):
        with ThreadPoolExecutor(max_workers=cpus) as executor:
            for input_item, expected_item in zip(input1, expected):
                executor.submit(run_test2, input_item, expected_item, operator, test)

    if (input2 is not None) and (process_function is not None):
        if not isinstance(input2, list):
            input2 = [input2]
        with ThreadPoolExecutor(max_workers=cpus) as executor:
            for input_item, expected_item, input2_item in zip(input1, expected, input2):
                executor.submit(run_test3, input_item, expected_item, input2_item, process_function, operator, test)

def test_is_not(cpus, input1, input2, expected, process_function=None):
    operator = lambda x, y: x is not y
    test = "test_is_not - "

    if input2 == "":
        input2 = None
    if not isinstance(input1, list):
        input1 = [input1]
    if not isinstance(expected, list):
        expected = [expected]

    if (input2 is None) and (process_function is not None):
        with ThreadPoolExecutor(max_workers=cpus) as executor:
            for input_item, expected_item in zip(input1, expected):
                executor.submit(run_test1, input_item, expected_item, process_function, operator, test)

    if (input2 is None) and (process_function is None):
        with ThreadPoolExecutor(max_workers=cpus) as executor:
            for input_item, expected_item in zip(input1, expected):
                executor.submit(run_test2, input_item, expected_item, operator, test)

    if (input2 is not None) and (process_function is not None):
        if not isinstance(input2, list):
            input2 = [input2]
        with ThreadPoolExecutor(max_workers=cpus) as executor:
            for input_item, expected_item, input2_item in zip(input1, expected, input2):
                executor.submit(run_test3, input_item, expected_item, input2_item, process_function, operator, test)

#def test_is_none():

def test_in(input1, expected):
    # não realiza paralelo
    # verificar viabilidade no arquivo sugestão
    operator = lambda x, y: x in y
    test = "test_in -"
    run_test4(input1, expected, operator, test)




def test_not_in(input1, expected):
    # não realiza paralelo
    # verificar viabilidade
    operator = lambda x, y: x not in y
    test = "test_not_in -"
    run_test4(input1, expected, operator, test)


def test_instance(a, b):
    line = line1('test_instance', a, b)
    filepass(line) if isinstance(a, b) else filefail(line)


def test_not_instance(a, b):
    line = line1('test_not_instance', a, b)
    filepass(line) if isinstance(a, b) is False else filefail(line)


def test_almost_equal(a, b, c):
    # testa se o arredondamendo de a-b com c casas decimais é zero
    line = line1('test_almost_equal', a, b)
    filepass(line) if round(a - b, c) == 0 else filefail(line)


def test_not_almost_equal(a, b, c):
    line = line1('test_not_almost_equal', a, b)
    filepass(line) if round(a - b, c) != 0 else filefail(line)


def test_greater(a, b):
    line = line1('test_greater', a, b)
    filepass(line) if a > b else filefail(line)


def test_greater_equal(a, b):
    line = line1('test_greater_equal', a, b)
    filepass(line) if a >= b else filefail(line)


def test_less(a, b):
    line = line1('test_less', a, b)
    filepass(line) if a < b else filefail(line)


def test_less_equal(a, b):
    line = line1('test_less_equal', a, b)
    filepass(line) if a <= b else filefail(line)


def line1a(test, ff, input, result, expected):
    # line1('test_equal', process_function, input_item, result, expected_item)
    return (str(test) + str(ff.__name__) + ' - ' + 'input: ' + str(input) + ' - ' + 'expected: ' + str(
        expected) + ' - ' + 'received: ' + str(result) + ' - ' + 'Result: ')


def line1b(test, ff, input, input2, result, expected):
    # line1b('test_equal', process_function, input_item, input2[0], result, expected_item)
    return (str(test) + str(ff.__name__) + ' - ' + 'input1: ' + str(input) + ' - ' + 'input2: ' + str(
        input2) + ' - ' + 'expected: ' + str(
        expected) + ' - ' + 'received: ' + str(result) + ' - ' + 'Result: ')


def line1c(test, input, result, expected):
    return (str(test) + 'input: ' + str(input) + ' expected: ' + str(
        expected) + ' received: ' + str(result) + ' Result: ')


def line1d(test, input, expected):
    return (str(test) + 'input: ' + str(input) + ' reference: ' + str(
        expected) + ' Result: ')


'''

def line1(t, a, b=""):
    return str(t) + ' - ' + 'a: ' + str(a) + ' b: ' + str(b) + ' Result: '
'''


def line2(ff, a, b, expected, received):
    return ('Function: ' + str(ff.__name__) + ' a: ' + str(a) + ' b: ' + str(b) + ' expected: ' + str(
        expected) + ' received: ' + str(received) + ' Result: ')


def init():
    if os.path.exists('filetot.txt'):
        os.remove('filetot.txt')

    if os.path.exists('filepass.txt'):
        os.remove('filepass.txt')

    if os.path.exists('filefail.txt'):
        os.remove('filefail.txt')


def end():
    if os.path.exists('filetot.txt'):
        with open('filetot.txt') as f:
            tl = len(f.readlines())
            print('Total: ' + str(tl))
            ft = open('filetot.txt', 'a')
            ft.write('\n')
            ft.write('Total: ' + str(tl))
            ft.close()
    if os.path.exists('filepass.txt'):
        with open('filepass.txt') as f:
            tl = len(f.readlines())
            print('Passed: ' + str(tl))
            fp = open('filepass.txt', 'a')
            fp.write('\n')
            fp.write('Passed: ' + str(tl))
            fp.close()
    if os.path.exists('filefail.txt'):
        with open('filefail.txt') as f:
            tl = len(f.readlines())
            print('Failed: ' + str(tl))
            ff = open('filefail.txt', 'a')
            ff.write('\n')
            ff.write('Failed: ' + str(tl))
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
    print(" Version: 2023.4")
    print("")


def sos():
    print("")
    print("")
    print("-----------------------------------------------")
    print("Multtestlib Command       Test")
    print("-----------------------------------------------")
    print("test_equal                a == b")
    print("test_not_equal            a != b")
    print("test_is                   is a b")
    print("test_is_not               is a not b")
    print("test_in                   is a in b")
    print("test_not_in               is a not in b")
    print("test_instance             is instance(a, b)")
    print("test_not_instance         is not instance(a, b)")
    print("test_almost_equal         round(a - b, 7) == 0")
    print("test_not_almost_equal     round(a - b, 7) != 0")
    print("test_greater              a > b")
    print("test_greater_equal        a >= b")
    print("test_less                 a < b")
    print("test_less_equal           a <= b")
    print("-----------------------------------------------")
    print("")
    print("")
