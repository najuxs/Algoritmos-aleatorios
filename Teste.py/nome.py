def nome():
    nome = input("Digite o seu nome")
    if not nome:
        nome = "você"
        print(f"Um para {nome}, um para mim")
    else:
        print(f"Um para {nome}, um para mim")

nome()