frutas = []

for i in range(3):
    while True:
        fruta = input(f"Digite a {i+1}ª fruta: ")
        if fruta in frutas:
            print("Fruta já cadastrada, digite outra.")
        else:
            frutas.append(fruta)
            break

quantidade = 3

print("Lista inicial")
print(frutas)

while True:
    resposta = input("Deseja excluir alguma fruta da lista? (sim/não): ")
    if resposta == "sim":
        print("Frutas cadastradas:")
        for i in range(quantidade):
            print(frutas[i])
        nome = input("Digite o nome da fruta que deseja excluir: ")
        for i in range(quantidade):
            if frutas[i] == nome:
                print(f"Fruta '{frutas[i]}' excluída.")
                frutas.pop(i)
                quantidade = quantidade - 1
                break
        else:
            print("Fruta não encontrada.")
        if quantidade == 0:
            print("Não há mais frutas para excluir.")
            break
    elif resposta == "não" or resposta == "nao":
        break
    else:
        print("Opção inválida. Digite 'sim' ou 'não'.")

print("Lista final de frutas:")
print(frutas)