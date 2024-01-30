
def fibonacci_hasta_n(n):
    a, b = 0, 1

    while a <= n:
        print(a, end=" ")
        a, b = b, a + b

# Ejemplo: Obtener la serie de Fibonacci hasta el número 100
numero_limite = 100
fibonacci_hasta_n(numero_limite)
