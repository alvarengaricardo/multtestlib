import time
import datetime


def fibonacci_rec(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)


def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        next_fib = fib[i - 1] + fib[i - 2]
        fib.append(next_fib)
    return fib[n]


def slow_function(n):
    # cenário 1: n/100
    time.sleep(n / 100)
    # cenário 2: 1/10
    # time.sleep(1 / 10)
    return n


def factorial_rec(n):
    s = n / 10
    time.sleep(s)
    if n == 0:
        return 1
    else:
        return n * factorial_rec(n - 1)


def factorial(n):
    if n < 0:
        return None  # O fatorial de números negativos não está definido
    elif n == 0:
        return 1  # O fatorial de 0 é 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


def now():
    # Obtenha o tempo atual em segundos desde a época (time.time())
    timestamp = time.time()

    # Converta o timestamp em um objeto datetime
    dt_object = datetime.datetime.fromtimestamp(timestamp)

    # Extraia as horas, minutos e segundos do objeto datetime
    hours = dt_object.hour
    minutes = dt_object.minute
    seconds = dt_object.second

    # Exiba o resultado
    print(f"Hora: {hours}, Minuto: {minutes}, Segundo: {seconds}")


def soma(a, b):
    return (a + b)