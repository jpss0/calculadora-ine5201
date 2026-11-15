"""Operacoes decimais da calculadora, sem dependencias da interface."""

from decimal import Decimal, InvalidOperation


OPERATORS = {"+", "-", "*", "/"}


def calculate(first: str, operator: str, second: str) -> Decimal:
    """Calcula uma operacao basica e rejeita entradas invalidas."""
    try:
        left = Decimal(first)
        right = Decimal(second)
    except (InvalidOperation, ValueError) as error:
        raise ValueError("Entrada inválida") from error

    if not left.is_finite() or not right.is_finite():
        raise ValueError("Entrada inválida")
    if operator not in OPERATORS:
        raise ValueError("Operador inválido")

    if operator == "+":
        return left + right
    if operator == "-":
        return left - right
    if operator == "*":
        return left * right
    if right == 0:
        raise ZeroDivisionError("Não é possível dividir por zero")
    return left / right
