
                                                                                                                                                                                                                                                                                   
# Função para adicionar um produto ao inventário
def adicionar_produto(inventario, nome, preco, quantidade):
    if nome in inventario:
        print(f"O produto '{nome}' já está no inventário.")
    else:
        inventario[nome] = {'preco': preco, 'quantidade': quantidade}
        print(f"Produto '{nome}' adicionado com sucesso.")

# Função para remover um produto do inventário
def remover_produto(inventario, nome):
    if nome in inventario:
        del inventario[nome]
        print(f"Produto '{nome}' removido com sucesso.")
    else:
        print(f"O produto '{nome}' não foi encontrado no inventário.")

# Função para listar todos os produtos do inventário
def listar_produtos(inventario):
    if inventario:
        print("Inventário de Produtos:")
        for nome, info in inventario.items():
            print(f"Nome: {nome}, Preço: {info['preco']}, Quantidade: {info['quantidade']}")
    else:
        print("O inventário está vazio.")

# Função principal do programa
def main():
    inventario = {}

    while True:
        print("\nMenu:")
        print("1. Adicionar Produto")
        print("2. Remover Produto")
        print("3. Listar Produtos")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: "))
            quantidade = int(input("Digite a quantidade do produto: "))
            adicionar_produto(inventario, nome, preco, quantidade)

        elif opcao == '2':
            nome = input("Digite o nome do produto a ser removido: ")
            remover_produto(inventario, nome)

        elif opcao == '3':
            listar_produtos(inventario)

        elif opcao == '4':
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
                                                                                                                                                                                                               

                                                                                                                                                                                                                                                                             