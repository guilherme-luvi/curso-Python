import re
pattern = re.compile("^[MFmf]+$")

def calculo_imc():
    valid_sexo_input = False
    valid_altura_input = False
    valid_peso_input = False

    #validar sexo
    while valid_sexo_input == False:
        sexo = input('Digite Seu sexo (M ou F): ').lower()
        if pattern.match(sexo):
            valid_sexo_input = True
            print('\n')
        else:
            print('Responda apenas com "F" ou "M"')

    #validar altura
    while valid_altura_input == False:
        altura = input('Digite sua altura: ')
        try:
            altura = float(altura)
            if  0.40 <= altura <= 2.20:
                valid_altura_input = True
                print('\n')
            else:
                print('Não é possível. Verifique sua entrada de dados')
        except:
            print('Formato inválido. Utilize pontos, não vírgulas.')
    
    #validar peso    
    while valid_peso_input == False:
        peso = input('Digite seu peso atual: ')
        try:
            peso = float(peso)
            if  1.0 <= peso <= 300.0:
                valid_peso_input = True
                print('\n')
            else:
                print('Não é possível. Verifique sua entrada de dados')
        except:
            print('Formato inválido. Utilize pontos, não vírgulas.')

    valid_sexo_input = False
    valid_altura_input = False
    valid_peso_input = False

    IMC = peso / (altura*altura)
    v_imc = str(IMC)
    print('\n'+'IMC:',v_imc[0:5])

    def classificação():
        if sexo == 'f':
            if IMC < 19.1:
                print('Abaixo do peso')
            elif 19.1 <= IMC < 25.8:
                print('Peso normal')
            elif 25.8 <= IMC < 27.3:
                print('marginalmente acima do peso')
            elif 27.3 <= IMC < 32.3:
                print('acima do peso ideal')
            else:
                print('Obesidade')
        elif sexo == 'm':
            if IMC < 20.7:
                print('Abaixo do peso')
            elif 20.7 <= IMC < 26.4:
                print('Peso normal')
            elif 26.4 <= IMC < 27.8:
                print('marginalmente acima do peso')
            elif 27.8 <= IMC < 31.1:
                print('acima do peso ideal')
            else:
                print('Obesidade')
        else:
            print('Erro no calculo')
    classificação()

    again()

def again():
    outro = input('\n'+'Gostaria de calcular outro IMC (S ou N)? ').lower()

    if outro == 's':
        calculo_imc()
    elif outro == 'n': 
        print('''
        fim do programa
        ''')
    else:
        print('verifique sua resposta')
        again()

calculo_imc()