nombre = input('cual es tu nombre?\n')
peso = input(f'{nombre}, cual es tu peso?\n')
peso = float(peso)
altura = input(f'{nombre}, una cosa mas, cual es tu altura?\n')
altura = float(altura)
imc = peso / (altura * altura)
if imc >= 40:
    grado_obesidad = 'Obesidad muy severa (obesidad morbica).'
elif imc >= 35:
    grado_obesidad = 'Obesidad severa.'
elif imc >= 30:
    grado_obesidad = 'Obesidad moderada.'
elif imc >= 25:
    grado_obesidad = 'Sobrepeso'
elif imc >= 18.5:
    grado_obesidad = 'Peso saludable'
elif imc >= 16:
    grado_obesidad = 'Delgadez'
elif imc >= 15:
    grado_obesidad = 'Delgadez severa'
else:
    grado_obesidad = 'Delgadez muy severa'
resultado = f'{nombre} tu IMC es {imc:.2f}, quiere decir que tienes {grado_obesidad}'
print(resultado)