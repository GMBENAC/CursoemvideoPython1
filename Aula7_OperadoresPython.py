n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
p = n1 ** n2
di = n1 // n2
rd = n1 % n2

print('A soma é igual a: {}'.format(s))
print('A subtração é igual a: {}'.format(sub))
print('A multiplicação é igual a: {}'.format(m))
print('A divisão é igual a:{:.2f}'.format(d))
print('A potenciação é igual:{}'.format(p))
print('A divisão inteira é igual a:{}'.format(di))
print('O resto da divisão é igual a:{}'.format(rd))