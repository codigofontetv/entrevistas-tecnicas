"""
Implemente uma função que receba uma string de tamanho "n" e faça a contagem da frequencia de cada
caracter presente.

Faça a análise de complexidade de tempo e memória

"""

def freq(s:str) -> dict[str, int]:
    """
    >>> freq('a') == {'a': 1}
    True
    >>> freq('aa') == {'a': 2}
    True
    >>> freq('banana') == {'a': 3, 'b': 1, 'n': 2}
    True

    Análise: linear em memória e em tempo de execução
    """
    saida = {}
    for char in s:
        saida[char] = saida.get(char, 0) + 1

    return saida