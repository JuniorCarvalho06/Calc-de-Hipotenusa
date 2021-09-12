print('Bem-vindo a Calculadora de Hipotenusas')


c1 = int(input('Digite o valor do Cateto a: '))
c2 = int(input('Digite o valor do Cateto b: '))
h = int(input('Digite o valor da hipotenusa '))
elevando1 = c1 * c1 
elevando2 = c2 * c2 
elevandoh = h * h 
elevando = elevando1 + elevando2

if elevandoh == elevando:

    print('A teoria de Pitágoras diz que a soma do quadrado dos catetos é igual ao quadrado da hipotenusa então ')
    print('O quadrado dos catetos a é {}, o quadrado do cateto b é {} e a hipotenusa é {} então podemos dizer que a soma dos quadrados do cateto é {} e o Quadrado da Hipotenusa é {} '.format(elevando1, elevando2, h, elevando, elevandoh))
    print('A teoria é verdadeira!')
