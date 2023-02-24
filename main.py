import numpy as np
import pprint as pp


class Camisa(object):
    def __init__(self, tipo, botaoG, botaoP):
        self.tipo = tipo
        self.botaoG = botaoG
        self.botaoP = botaoP


class VendaCamisa(object):
    def __init__(self, camisa, vmaio, vjunho):
        self.camisa = camisa
        self.vjunho = vjunho
        self.vmaio = vmaio


class VendaBotao(object):
    def __init__(self, botao, vmaio, vjunho):
        self.botao = botao
        self.vjunho = vjunho
        self.vmaio = vmaio


def tabelaCamisa(camisas):
    titulo = np.array([])
    tabela = np.array([])

    for camisa in camisas:
        print(camisa)


def EncodeCamisas(objects):
    lista = []

    for camisa in objects:
        f = {}
        f["botaoG"] = camisa.botaoG
        f["botaoP"] = camisa.botaoP
        f["tipo"] = camisa.tipo
        lista.append(f)
    return lista


def EncodeVendas(objects):
    lista = []

    for venda in objects:
        f = {}
        f["camisa"] = venda.camisa
        f["vjunho"] = venda.vjunho
        f["vmaio"] = venda.vmaio
        lista.append(f)
    return lista


def EncodeBotao(objects):
    lista = []

    for botao in objects:
        f = {}
        f["Tamanho"] = botao.botao
        f["Vendas Junho"] = botao.vjunho
        f["Vendas Maio"] = botao.vmaio
        lista.append(f)
    return lista


camisas = []
tipo = input("digite o tipo de camisa:")
while tipo != "":
    # print("deu bão")

    botaoG = input("digite o a quantidade de botões grandes:")
    botaoP = input("digite o a quantidade de botões Pequenos:")

    camisas.append(Camisa(tipo, botaoG, botaoP))
    tipo = input("digite o tipo de camisa:")

print("")

pp.pprint(EncodeCamisas(camisas))

vendascamisa = []
for camisa in camisas:
    vmaio = input("Quantas camisas tipo " + camisa.tipo + " foram vendidas em Maio?")
    vjunho = input("Quantas camisas tipo " + camisa.tipo + " foram vendidas em Junho?")
    vendascamisa.append(VendaCamisa(camisa.tipo, vmaio, vjunho))

print("")

pp.pprint(EncodeVendas(vendascamisa))

vendasbotao = []

botpmaio = 0
botpjunho = 0

botgmaio = 0
botgjunho = 0

for camisa in camisas:
    for venda in vendascamisa:
        if venda.camisa == camisa.tipo:
            botpmaio += int(venda.vmaio) * int(camisa.botaoP)
            botpjunho += int(venda.vjunho) * int(camisa.botaoP)

            botgmaio += int(venda.vmaio) * int(camisa.botaoG)
            botgjunho += int(venda.vjunho) * int(camisa.botaoG)

print("")
vendasbotao.append(VendaBotao("G", botgmaio, botgjunho))
vendasbotao.append(VendaBotao("P", botpmaio, botpjunho))

pp.pprint(EncodeBotao(vendasbotao))
