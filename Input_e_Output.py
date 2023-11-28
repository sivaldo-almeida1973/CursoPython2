"""
Input e Output

Output - print(): apresenta daods para o usuário

Input - input(): Recebe dados do usuário

#Obs: Os dados recebiidos são do tipo string.

Ex 1:

print('Digite uma cor:')
cor = input()
print(cor)



cor = input('Digite uma cor:')
#O print por padrão ja vem com \n (pula linha)
print('Tomate')
print('Tomate')
print('Tomate')
print('Tomate')

print('tomate', end=' ') #O end= evita de pular linha
print('tomate', end=' ')
print('tomate', end=' ')
==========================================================
# cor = input('Digite uma cor:')
# num = input('Digite um numero: ')
#
# # # #versões 2.x
# # print('Você scolheu a cor %s e o numero %s' %(cor, num))
#
# # #versões 3.x até 3.7
# print('Voce escolheu a cor {0} eo numero {1}'.format(cor , num))
#
#
# # #versões apartir de 3.7 _recente
# print(f'Você escolheu a cor {cor} e o numero {num}')

"""
# print('Digite uma cor:')
# cor = input()
# #
# #versões 2.x
# #print('Você escolheu a cor %s' % cor)
#
# #versões 3.x até 3.7
# print('Você escolheu a cor {0}' .format(cor))
#
# #versões apartir de 3.7 _recente
# print(f'Você escolheu a cor {cor}')


num1 = input('Digite o primeiro numero')
num2 = input('Digite o segundo numero:')

print(f'A soma de {num1} +{num2}')#erro

print(f'A soma é: {int(num1) + int(num2)}')#certo

#Obs: casting: Coversão de um tipo de dado para outro
