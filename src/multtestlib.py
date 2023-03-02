from multiprocessing import freeze_support, Pool, cpu_count
import os
#import src


def test_equal(a, b):
    line = line1('test_equal', a, b)
    filepass(line) if a == b else filefail(line)


def test_not_equal(a, b):
    line = line1('test_not_equal', a, b)
    filepass(line) if a != b else filefail(line)


def test_func(ff, a, b, expected):
    if b != '':
        received = ff(a, b)
    else:
        received = ff(a)
    line = line2(ff, a, b, expected, received)
    filepass(line) if received == expected else filefail(line)


def test_not_func(ff, a, b, expected):
    if b != '':
        received = ff(a, b)
    else:
        received = ff(a)
    line = line2(ff, a, b, expected, received)
    filepass(line) if received != expected else filefail(line)


def test_is(a, b):
    line = line1('teste_is', a, b)
    filepass(line) if a is b else filefail(line)


def test_is_not(a, b):
    line = line1('test_is_not', a, b)
    filepass(line) if a is not b else filefail(line)


def test_in(a, b):
    line = line1('test_in', a, b)
    filepass(line) if a in b else filefail(line)


def test_not_in(a, b):
    line = line1('test_not_in', a, b)
    filepass(line) if a not in b else filefail(line)


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


def line1(t, a, b=""):
    #  s = str(type(a))
    return str(t) + ' - ' + 'a: ' + str(a) + ' b: ' + str(b) + ' Result: '


def line2(ff, a, b, expected, received):
    return ('Function: ' + str(ff.__name__) + ' a: ' + str(a) + ' b: ' + str(b) + ' expected: ' + str(
        expected) + ' received: ' + str(received) + ' Result: ')


def init():
    if os.path.exists('filetot.txt'):
        os.remove('filetot.txt')
        # print("removido filetot.txt")
    # else:
    # print("filetot.txt does not exist")

    if os.path.exists('filepass.txt'):
        os.remove('filepass.txt')
    #    print("removido filefail.txt")
    # else:
    #    print("filepass.txt does not exist")

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
    print("multtestLib")
    print("Biblioteca de Teste de Unidade com Processamento Paralelo em Python.")
    print("Unit Test Library with Parallel Processing in Python.")
    print("Author: Ricardo Ribeiro de Alvarenga")
    print("        ITA - Instituto Tecnologico de Aeronáutica")
    print("Version: 2023.1")


def sos():
    print("")
    print("")
    print("Multtestlib Command             Test")
    print("---------------------------------------------")
    print("test_equal              a == b")
    print("test_not_equal          a != b")
    print("test_func               function(a, b) == c")
    print("test_not_func           function(a, b) != c")
    print("test_is                 is a b")
    print("test_is_not             is a not b")
    print("test_in                 is a in b")
    print("test_not_in             is a not in b")
    print("test_instance           is instance(a, b)")
    print("test_not_instance       is not instance(a, b)")
    print("test_almost_equal       round(a - b, 7) == 0")
    print("test_not_almost_equal   round(a - b, 7) != 0")
    print("test_greater            a > b")
    print("test_greater_equal      a >= b")
    print("test_less               a < b")
    print("test_less_equal         a <= b")
    print("")
    print("")
