import os.path

class Produtos:
    def __init__(self):
        if os.path.isfile('idAtual.txt') == False:
            with open("idAtual.txt",'w') as cont:
                cont.write("0")

    def atualizarContId(self): 
        with open('idAtual.txt','r') as cont:
            x = str( (int(cont.read())+1) )
        with open('idAtual.txt','w') as cont:
            cont.write(x)            
        return x
            
    def cadastrarProduto(self, nome, marca, preco_C, preco_V, qtd):        
        with open("estoque.txt",'a') as estoque:
            x = self.atualizarContId()
            estoque.write(nome+" "+marca+" "+str(preco_C)+" "+str(preco_V)+" "+str(qtd)+" "+ x +"\n")
        return "\tProduto cadastrado com sucesso.\n"
    
    def visualizarProdutos(self):   
        with open("estoque.txt",'r') as estoque:
            dados = ""
            for linha in estoque:
                conteudo = linha.split()
                dados += "Nome: "+conteudo[0] + " , Marca: " + conteudo[1] + " , Preco_compra: "+ conteudo[2] + " , Preco_venda: " + conteudo[3] + " , Quantidade: " +conteudo[4] + " , Id: "+conteudo[5]+ "\n"
        return dados
    
    def excluirProduto(self, id):
        informa = False
        with open("estoque.txt",'r') as estoque:
            produtos = estoque.readlines()

        with open("estoque.txt",'w') as estoque:
            for produto in produtos:
                conteudo = produto.split()
                if (int(conteudo[len(conteudo)-1]) != id):
                    estoque.write(conteudo[0]+" "+conteudo[1]+" "+conteudo[2]+" "+conteudo[3]+" "+conteudo[4]+" "+conteudo[5]+"\n")    
                else:
                    informa = True
            if informa:
                return "\tProduto excluído com sucesso\n"
            return "\tProduto não enontrado\n"
    def atualizarProduto(self, id, opcao, dado):
        informa = False
        with open("estoque.txt",'r') as estoque:
            produtos = estoque.readlines()

        with open("estoque.txt",'w') as estoque:
            for produto in produtos:
                conteudo = produto.split()
                if (int(conteudo[len(conteudo)-1]) == id):
                    if opcao == 1:
                        conteudo = [dado]+conteudo[1:]
                        informa = True
                    else:
                        conteudo = conteudo[0:(opcao-1)]+[dado]+conteudo[opcao:]
                        informa = True
                estoque.write(conteudo[0]+" "+conteudo[1]+" "+conteudo[2]+" "+conteudo[3]+" "+conteudo[4]+" "+conteudo[5]+"\n") 
        if informa:
            return "\tProduto alterado com sucesso.\n"
        return "\tProduto não encontrado.\n"


#p = Produtos()
#p.cadastrarProduto("cuscuz","Flocao","1.00","2.50","500")
#p.cadastrarProduto("tapioca","seila","2.00","5.50","300")
#print(p.visualizarProdutos())
#p.excluirProduto(2)
#p.alterarProduto(2,2,"Boa")
#print(p.visualizarProdutos())
#print(p.visualizarProdutos()+"Fim")


    