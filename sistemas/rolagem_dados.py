
import random


def rolar_dado(lados: int) -> int:
    if lados < 2:
        raise ValueError("Um dado precisa ter pelo menos 2 lados.")

    return random.randint(1, lados)


def rolar_varios(
    quantidade: int,
    lados: int,
    modificador: int = 0
) -> dict:

    if quantidade < 1:
        raise ValueError("A quantidade precisa ser positiva.")

    resultados = [
        rolar_dado(lados)
        for _ in range(quantidade)
    ]

    total = sum(resultados) + modificador

    return {
        "resultados": resultados,
        "modificador": modificador,
        "total": total
    }


if __name__ == "__main__":
    resultado = rolar_varios(2, 20, 3)

    print("Dados:", resultado["resultados"])
    print("Modificador:", resultado["modificador"])
    print("Resultado final:", resultado["total"])
