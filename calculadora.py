"""
Calculadora em Python
---------------------
Uma calculadora de terminal que fica em execução até o usuário decidir sair.
Operações: soma, subtração, multiplicação, divisão, potência e resto.
"""


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Não é possível dividir por zero.")
    return a / b


def potencia(a, b):
    return a ** b


def resto(a, b):
    if b == 0:
        raise ZeroDivisionError("Não é possível calcular o resto com divisor zero.")
    return a % b


OPERACOES = {
    "1": ("Soma", "+", somar),
    "2": ("Subtração", "-", subtrair),
    "3": ("Multiplicação", "*", multiplicar),
    "4": ("Divisão", "/", dividir),
    "5": ("Potência", "**", potencia),
    "6": ("Resto", "%", resto),
}


def mostrar_menu():
    print("\n===== CALCULADORA =====")
    for codigo, (nome, simbolo, _) in OPERACOES.items():
        print(f"{codigo} - {nome} ({simbolo})")
    print("H - Ver histórico")
    print("0 - Sair")


def ler_numero(mensagem):
    """Pede um número até o usuário digitar um valor válido."""
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            return float(entrada)
        except ValueError:
            print("Valor inválido! Digite apenas números.")


def formatar(numero):
    """Mostra 5.0 como 5 e mantém 2.5 como 2.5."""
    return int(numero) if numero == int(numero) else round(numero, 6)


def mostrar_historico(historico):
    if not historico:
        print("\nNenhum cálculo realizado ainda.")
        return
    print("\n--- Histórico ---")
    for i, item in enumerate(historico, start=1):
        print(f"{i}. {item}")


def main():
    historico = []
    print("Bem-vindo à Calculadora!")

    while True:  # mantém o programa rodando
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip().upper()

        if opcao == "0":
            print("Encerrando a calculadora. Até logo!")
            break

        if opcao == "H":
            mostrar_historico(historico)
            continue

        if opcao not in OPERACOES:
            print("Opção inválida! Tente novamente.")
            continue

        nome, simbolo, funcao = OPERACOES[opcao]
        a = ler_numero("Digite o primeiro número: ")
        b = ler_numero("Digite o segundo número: ")

        try:
            resultado = funcao(a, b)
        except ZeroDivisionError as erro:
            print(f"Erro: {erro}")
            continue

        conta = f"{formatar(a)} {simbolo} {formatar(b)} = {formatar(resultado)}"
        historico.append(conta)
        print(f"\nResultado: {conta}")


if __name__ == "__main__":
    main()
