print('Informe o valor a ser pago: ')
preco = float(input())

print('Informe o número de parcelas: ')
parcelas = int(input())

res = preco / parcelas

print(f'O valor de cada parcela será: R${res}')