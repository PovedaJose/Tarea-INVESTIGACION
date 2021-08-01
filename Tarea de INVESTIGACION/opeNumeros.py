class Basico:
    def __init__(self):
        pass

    def numerosN(self, n):
        i = 1
        while i <= n:
            print(i)
            i = i + 1

    def multiplo(self, numero):
        acu = 1
        multiplo = int(input('Ingrese el numero de multiplos que desea presentar: '))
        for cont in range(1, multiplo+1):
            acu = numero*cont
            print(acu)

    def DivisoresNumero(self, numero):
        acu = 1
        for cont in range(1,numero+1):
            divisor = numero % cont
            if divisor == 0:
                acu+=cont
                print(cont)

    def primo(self, numero):
        for n in range(2,numero):
            res = numero % n
            if res == 0:
                print('El número {} no es primo'.format(numero))
                return False
        print('El numero {} es primo'.format(numero))
        return True

    def perfecto(self, numero):
        acu = 0
        for cont in range(1,numero):
            residuo = numero % cont
            if residuo == 0:
                acu += cont
        if acu == numero:
            print('El número {} es perfecto'.format(numero))
        else:
            print('El número {} no es perfecto'.format(numero))


class Intermedio(Basico):
    def __init__(self):
        super().__init__()
        pass

    def numerosN(self, n): #Polimorfismo: sumar los numeros del 1 al n
        suma = 0
        acu = 1
        for acu in range(n+1):
            suma = suma + acu
            print('Interación {} -- {}'.format( acu,suma))
        print('Suma Total:', suma)

    def factorial(self, numero):
        try:
            numero = int
        except ValueError:
            print('invalido')
        factorial = 1
        print('{}! : '.format(numero), end='')
        if numero == 0:
            return 1
        else:
            while numero > 1:
                factorial = factorial*numero
                numero = numero-1
            return factorial

    def fibonacci(self, n):
        a,b = 0,1
        while a < n:
            print(a, end=' ')
            a,b = b,a+b
        print()


    def primosGemelos(self, num1, num2):
        x = 0
        if num1 > 0 and num2 > 0 and num1 != num2:
            if num1 > num2:  
                auxi = num1
                num1 = num2
                num2 = auxi
            for i in range (num1, num2+1):
                incre = 2
                Primo = True
                while Primo and incre < i:
                    if i % incre == 0:
                        Primo = False
                    else:
                        incre += 1
                if Primo and not x:
                    x = i
                elif Primo and x:
                    y = i
                    if y - x == 2:
                        print('Los números {} y {} son primos gemelos'.format(x, y))
                    x = i                   
        else:
            if num1 == num2:
                print('Los números son Iguales.Ingrese de nuevo')    
            else:
                print('Números incorrectos. Ingrese de nuevo')
                
    def amigos(self, num1, num2):
        acu1 = 0
        lista1 = []
        for i in range(1, num1):
            if num1 % i == 0:
                lista1.append(i)
                acu1 = acu1 + i        
        acu2 = 0
        lista2 = []
        for x in range(1, num2):
            if num2 % x == 0:
                lista2.append(x)
                acu2 = acu2 + x           
        if acu1 == num2 and acu2 == num1:
            print('Los números {} y {} son números amigos'.format(num1, num2))
        else:
            print('Los números {} y {} no son números amigos'.format(num1, num2))

