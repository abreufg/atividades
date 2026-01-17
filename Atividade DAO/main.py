from crudproduto import CRUDProduto

class SistemaProduto:
    def __init__(self):
        self.crud_produto = CRUDProduto()

    def executar(self):
        while True:
            print("\n--- MENU ---")
            print("1 - Inserir Produto")
            print("2 - Listar Produtos")
            print("3 - Buscar Produto por ID")
            print("4 - Atualizar Produto")
            print("5 - Excluir Produto")
            print("0 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                nome = input("Nome do Produto: ")
                preco = float(input("Preço do Produto: "))
                id_categoria = int(input("ID da Categoria: "))

                self.crud_produto.inserir(nome, preco, id_categoria)
                print("Produto inserido com sucesso!")

            elif opcao == "2":
                produtos = self.crud_produto.listar()

                if produtos:
                    for p in produtos:
                        print(f"ID: {p[0]} | Nome: {p[1]} | Preço: {p[2]} | Categoria: {p[3]}")
                else:
                    print("Nenhum produto cadastrado.")

            elif opcao == "3":
                id_produto = int(input("Informe o ID do produto: "))
                produto = self.crud_produto.buscar_por_id(id_produto)

                if produto:
                    print(f"ID: {produto[0]}")
                    print(f"Nome: {produto[1]}")
                    print(f"Preço: {produto[2]}")
                    print(f"Categoria: {produto[3]}")
                else:
                    print("Produto não encontrado.")

            elif opcao == "4":
                id_produto = int(input("ID do produto a atualizar: "))
                nome = input("Novo nome: ")
                preco = float(input("Novo preço: "))
                id_categoria = int(input("Nova categoria: "))

                self.crud_produto.atualizar(id_produto, nome, preco, id_categoria)
                print("Produto atualizado com sucesso!")

            elif opcao == "5":
                id_produto = int(input("ID do produto a excluir: "))
                self.crud_produto.excluir(id_produto)
                print("Produto excluído com sucesso!")

            elif opcao == "0":
                print("Saindo do sistema.")
                break

            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    sistema = SistemaProduto()
    sistema.executar()
