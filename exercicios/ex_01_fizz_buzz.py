"""
Implemente a função fizz_buzz. Ela deve receber um inteiro "n" como argumento.
Ela deve iterar de 1 até n imprimindo (i), de tal forma que:
fizz, se i é divisivel por 2
buzz, se i é divisivel por 3
i, caso contrário
"""

def fizz_buzz(n: int) -> None:
    """
    >>> fizz_buzz(3)
    1
    fizz
    buzz
    >>> fizz_buzz(7)
    1
    fizz
    buzz
    fizz
    5
    fizz, buzz
    7

    """
    for i in range(1, n + 1):
        saida=[]
        if i % 2 ==0:
            saida.append("fizz")
        if i % 3 == 0:
            saida.append("buzz")
        if len(saida) == 0:
            saida.append(str(i))
        print(', '.join(saida))


