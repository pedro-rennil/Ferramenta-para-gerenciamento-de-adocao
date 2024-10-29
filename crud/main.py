def menu_principal():
    print("===== CESAR'S ANIMAL HUB =====")
    print("1. Gerenciamento de Adoção de Animais")
    print("2. Gerenciamento de Clientes")
    print("3. Pet Shop")
    print("4. Sair")

def main():
    while True:
        menu_principal()
        op = input("Escolha a opção desejada: ")

        if op == '1':
            import adocao.init as adocao
            adocao.main()
        elif op == '2':
            import cliente.init as cliente
            cliente.main()
        elif op == '3':
            import pet_shop.init as pet_shop
            pet_shop.main()
        elif op == '4':
            print("Saindo do sitema... ")
            break
        else:
            print("Opção inválida! Tente novamente. ")

if __name__ == "__main__":
    main()




       