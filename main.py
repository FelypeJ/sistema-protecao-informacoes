from criptografia import cifra_cesar, decifra_cesar
from hash_utils import gerar_hash, verificar_integridade
from autenticacao import cadastrar_usuario, autenticar_usuario
from combinacoes import calcular_combinacoes, demonstrar_tentativas

def menu():
    print("\n" + "=" * 48)
    print(" SISTEMA DE PROTEÇÃO DE INFORMAÇÕES")
    print("=" * 48)
    print("1 - Criptografar mensagem (Cifra de César)")
    print("2 - Descriptografar mensagem")
    print("3 - Gerar hash SHA-256")
    print("4 - Verificar integridade de um texto")
    print("5 - Cadastrar usuário")
    print("6 - Autenticar usuário")
    print("7 - Calcular combinações possíveis")
    print("8 - Simulação didática de tentativas")
    print("0 - Sair")

def ler_inteiro(mensagem, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensagem))
            if minimo is not None and valor < minimo:
                print(f"Digite um número a partir de {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"Digite um número até {maximo}.")
                continue
            return valor
        except ValueError:
            print("Digite um número inteiro válido.")

def executar():
    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            texto = input("Mensagem: ")
            chave = ler_inteiro("Deslocamento (1 a 25): ", 1, 25)
            print("Mensagem codificada:", cifra_cesar(texto, chave))

        elif opcao == "2":
            texto = input("Mensagem codificada: ")
            chave = ler_inteiro("Deslocamento usado (1 a 25): ", 1, 25)
            print("Mensagem original:", decifra_cesar(texto, chave))

        elif opcao == "3":
            texto = input("Texto para gerar hash: ")
            print("SHA-256:", gerar_hash(texto))

        elif opcao == "4":
            original = input("Texto original: ")
            recebido = input("Texto recebido para comparação: ")
            if verificar_integridade(original, recebido):
                print("Integridade confirmada: os textos são iguais.")
            else:
                print("Atenção: os textos são diferentes.")

        elif opcao == "5":
            usuario = input("Nome de usuário: ").strip()
            senha = input("Crie uma senha: ")
            try:
                cadastrar_usuario(usuario, senha)
                print("Usuário cadastrado com sucesso.")
            except ValueError as erro:
                print(erro)

        elif opcao == "6":
            usuario = input("Nome de usuário: ").strip()
            senha = input("Senha: ")
            if autenticar_usuario(usuario, senha):
                print("Autenticação realizada com sucesso.")
            else:
                print("Usuário ou senha incorretos.")

        elif opcao == "7":
            tamanho = ler_inteiro("Quantidade de caracteres da senha: ", 1, 100)
            possibilidades = calcular_combinacoes(tamanho)
            print(f"Usando letras maiúsculas, minúsculas e números,")
            print(f"existem {possibilidades:,} combinações possíveis.".replace(",", "."))

        elif opcao == "8":
            demonstrar_tentativas()

        elif opcao == "0":
            print("Encerrando o sistema. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    executar()
