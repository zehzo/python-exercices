valordoproduto = float(input('Digite o valor do produto: '))
condicao = str(input('Digite como será pago: ')).strip()
parcelas = int(input('Número de parcelas: '))

if condicao.upper() == 'DINHEIRO':
    valor = valordoproduto * 0.9
    print('Você pagará R${:.2f} em dinheiro'.format(valor))
elif condicao.upper() == 'CARTAO' and parcelas == 1:
    valor = valordoproduto * 0.95
    print('Você pagará R${:.2f} em {}x no cartão'.format(valor,parcelas))
elif condicao.upper() == 'CARTAO' and parcelas == 2:
    valor = valordoproduto / 2
    print('Você pagará R${:.2f} em {}x no cartão'.format(valor,parcelas))
elif condicao.upper() == 'CARTAO' and parcelas >= 3:
    valor = (1.2 * valordoproduto) / parcelas
    print('Você pagará R${:.2f} em {}x no cartão'.format(valor,parcelas))
else:
    print('Parâmetros inválidos!')
