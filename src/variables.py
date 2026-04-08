# ============================================================
# MÓDULO 1: Variables y Tipos de Datos
# ============================================================

def crear_saludo(nombre: str) -> str:
    """
    Retorna un saludo personalizado.
    """
    return f"Hola, {nombre}!"


def suma_enteros(a: int, b: int) -> int:
    """
    Retorna la suma de dos enteros.
    """
    return a + b


def es_mayor_de_edad(edad: int) -> bool:
    """
    Retorna True si edad >= 18, False caso contrario.
    """
    return edad >= 18


def tipo_de_dato(valor) -> str:
    """
    Retorna el nombre del tipo de dato del valor recibido.
    Ejemplo: tipo_de_dato(42) -> "int"
             tipo_de_dato("hola") -> "str"
    """
    return type(valor).__name__


def convertir_a_float(valor: str) -> float:
    """
    Convierte un string numérico a float.
    Ejemplo: convertir_a_float("3.14") -> 3.14
    """
    return float(valor)


def armar_mensaje(nombre: str, edad: int, ciudad: str) -> str:
    """
    Arma un mensaje presentándose con nombre, edad y ciudad.
    """
    return f"Soy {nombre}, tengo {edad} años y vivo en {ciudad}."