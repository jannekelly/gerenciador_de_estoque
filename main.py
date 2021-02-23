from Estoque import Estoque
class Main:
    #def __init__(self):
    def iniciarSistema(self):
        while True:
            opcao = self.visualizarMenu()
            estoque = Estoque()
            if 1 <= opcao <= 9:
                if 1 <= opcao <= 2:
                    print("Id do produto: ")
                    id = int(input())
                    print("Quantidade: ")
                    qtd = int(input())
                    if opcao == 1:
                        print(estoque.efetuarTransacaoEntrada(id,qtd))
                    else:
                        print(estoque.efetuarTransacaoSaida(id,qtd))
                elif opcao == 3:
                    print(estoque.visualizarHistoricoSaida())
                elif opcao == 4:
                    print(estoque.visualizarHistoricoEntrada())
                elif opcao == 5:
                    #Visualizar produtos
                    print(estoque.produtos.visualizarProdutos() )
                elif opcao == 6:
                    #Cadastrar produto
                    print("\tInfome os dados do produto para ser cadastrado")
                    print("Nome: ")
                    nome = input()
                    print("Marca: ")
                    marca = input()
                    print("Preço de compra: ")
                    preco_c = float(input())
                    print("Preço de venda: ")
                    preco_v = float(input())
                    print("Quantidade: ")
                    qtd = int(input())
                    print(estoque.produtos.cadastrarProduto(nome,marca,preco_c,preco_v,qtd))
                elif opcao == 7:
                    #atualizar produto
                    print("Id: ")
                    id = int(input())
                    print("Escolha qual opção deseja atualizar: ")
                    print("1. Nome")        
                    print("2. Marca")                            
                    print("3. Preço de compra")
                    print("4. Preço de venda")
                    print("5. Quantidade")
                    opcao = int(input())
                    print("Informe o dado atualizado: ")
                    dado = input()
                    print(estoque.produtos.atualizarProduto(id, opcao, dado) )
                elif opcao == 8:
                    #Remover produto
                    print("Id: ")
                    id = int(input())
                    print(estoque.produtos.excluirProduto(id) )
                elif opcao == 9:
                    break

    def visualizarMenu(self):
        print("Escolha uma opção:")
        print("1. Efetuar uma transação de entrada")
        print("2. Efetuar uma transação de saída")
        print("3. Histórico de transações de saída")
        print("4. Histórico de transações de entrada")
        print("5. Visualizar produtos")
        print("6. Cadastrar produto")
        print("7. Atualizar produto")
        print("8. Remover produto")
        print("9. Sair")
        return int(input())

        


if __name__ == "__main__":
    main = Main()
    main.iniciarSistema()