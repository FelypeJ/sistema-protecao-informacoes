def cifra_cesar(texto, deslocamento):
    """Cifra educativa: desloca letras; mantém espaços e pontuação."""
    resultado = []
    for caractere in texto:
        if "a" <= caractere <= "z":
            base = ord("a")
            resultado.append(chr((ord(caractere) - base + deslocamento) % 26 + base))
        elif "A" <= caractere <= "Z":
            base = ord("A")
            resultado.append(chr((ord(caractere) - base + deslocamento) % 26 + base))
        else:
            resultado.append(caractere)
    return "".join(resultado)

def decifra_cesar(texto, deslocamento):
    return cifra_cesar(texto, -deslocamento)
