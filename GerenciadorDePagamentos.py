produto = int(input("Digite o preço do produto: R$"))
pagamento = int(input("Qual o modelo de pagamento '1 A Vista''2 Cheque''3 Cartão': "))
parcelado = int(input("Digite quantas vezes voce vai efetuar o pagamento'0 é a vista''De 1 a infinito é o valor de vezes que voce deseja parcelar': "))
if pagamento == 1 or pagamento == 2 and parcelado == 0:
    desconto = produto * 0.10
    produtofinal = produto - desconto
    print("A vista dinheiro/cheque tem 10% de desconto e irá sair {}".format(produtofinal))
elif pagamento == 3 and parcelado == 0:
    desconto = produto * 0.05
    produtofinal = produto - desconto
    print("O preço á vista no cartão tem 5% de desconto e irá sair {}".format(produtofinal))
elif pagamento == 3 and parcelado == 2:
    print("Voce irá pagar o mesmo valor, {}".format(produto))
elif pagamento == 3 and parcelado >=3:
    desconto = (produto * 0.20) + produto
    print("{}x no cartão tem 20% de juros e irá sair {}".format(parcelado,desconto))


