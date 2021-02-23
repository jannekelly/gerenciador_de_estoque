from Produtos import Produtos
from datetime import datetime
import os.path


class Estoque:
    def __init__(self):
        if os.path.isfile('histórico_de_entrada.txt') == False:
            with open("histórico_de_entrada.txt",'w'):
                pass
        if os.path.isfile('histórico_de_saída.txt') == False:
            with open("histórico_de_saída.txt",'w'):
                pass
        self.produtos = Produtos()
    def fazerNovaTransacao(self,id,qtd,tipoTransacao):
        informa = False
        msg = "Concluído"
        with open("estoque.txt",'r') as estoque:
            produtos = estoque.readlines()

        with open("estoque.txt",'w') as estoque:
            for produto in produtos:
                conteudo = produto.split()
                if (int(conteudo[len(conteudo)-1]) == id):
                    informa = True
                    if qtd+int(conteudo[4]) >= 0:
                        conteudo = conteudo[0:4]+[(str(qtd+int(conteudo[4])))]+conteudo[5:]
                        if tipoTransacao == "entrada":
                            self.atualizarHistoricoEntrada(conteudo,qtd)
                        else:
                            self.atualizarHistoricoSaida(conteudo,qtd*-1)
                    else:
                        msg = "Não há produtos suficientes para esta operação"
                estoque.write(conteudo[0]+" "+conteudo[1]+" "+conteudo[2]+" "+conteudo[3]+" "+conteudo[4]+" "+conteudo[5]+"\n") 
        if informa:
            return msg
        return "Erro"
    def atualizarHistoricoEntrada(self,produto,qtd):
        with open("histórico_de_entrada.txt",'a') as historicoEntrada:
            historicoEntrada.write(produto[0]+" "+produto[1]+" "+produto[2]+" "+str(qtd)+" "+produto[5]+" "+self.dataAtual()+" "+self.horaAtual()+"\n")
    def atualizarHistoricoSaida(self,produto,qtd):
        with open("histórico_de_saída.txt",'a') as historicoSaida:
            historicoSaida.write(produto[0]+" "+produto[1]+" "+produto[3]+" "+str(qtd)+" "+produto[5]+" "+self.dataAtual()+" "+self.horaAtual()+"\n")
    def efetuarTransacaoEntrada(self,id,qtd):
        return self.fazerNovaTransacao(id,qtd,"entrada")
    def efetuarTransacaoSaida(self,id,qtd):
        return self.fazerNovaTransacao(id,(qtd * -1),"saida")
    def visualizarHistoricoSaida(self):
        texto=""
        with open("histórico_de_saída.txt",'r') as historicoSaida:
            for linha in historicoSaida:
                conteudo = linha.split()
                texto += "Nome: "+conteudo[0] + " , Marca: " + conteudo[1] + " , Preco de venda: " + conteudo[2] + " , Quantidade: " +conteudo[3] + " , Id: "+conteudo[4]+" , Data: "+conteudo[5]+" , Hora: "+conteudo[6]+ "\n"
        return texto
    def visualizarHistoricoEntrada(self):
        texto=""
        with open("histórico_de_entrada.txt",'r') as historiEntrada:
            for linha in historiEntrada:
                conteudo = linha.split()
                texto += "Nome: "+conteudo[0] + " , Marca: " + conteudo[1] + " , Preco de compra: " + conteudo[2] + " , Quantidade: " +conteudo[3] + " , Id: "+conteudo[4]+" , Data: "+conteudo[5]+" , Hora: "+conteudo[6]+ "\n"
        return texto
    def dataAtual(self):
        data = datetime.now()
        return data.strftime("%d/%m/%Y")
    def horaAtual(self):
        hora = datetime.now()
        return hora.strftime("%H:%M")
    

#estoque = Estoque()
#rint(estoque.efetuarTransacaoEntrada(1,))
    #print(estoque.mostrarHistoricoEntrada())

    #print( estoque.produtos.visualizarProdutos())