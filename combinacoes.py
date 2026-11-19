def calcular_combinacoes(tamanho, quantidade_caracteres=62):
    """Calcula o espaço teórico: quantidade_caracteres elevado ao tamanho."""
    if tamanho < 1:
        raise ValueError("O tamanho deve ser pelo menos 1.")
    return quantidade_caracteres ** tamanho

def demonstrar_tentativas():
    """
    Demonstra apenas a contagem de tentativas em um exemplo fictício.
    Não testa senhas reais nem tenta acessar contas ou sistemas.
    """
    candidatos_exemplo = ["sol", "lua", "mar", "ceu"]
    codigo_exemplo = "mar"

    print("\nSIMULAÇÃO DIDÁTICA — lista fictícia e local")
    print("A atividade percorre somente quatro palavras de exemplo.")
    for numero, candidato in enumerate(candidatos_exemplo, start=1):
        print(f"Tentativa {numero}: {candidato}")
        if candidato == codigo_exemplo:
            print(f"Exemplo encontrado após {numero} tentativas.")
            return
    print("O exemplo não foi encontrado.")
