print("Digite os valores dos lados dos triângulos")


num1 = int(input("lado 1:\t"))
num2 = int(input("lado 2:\t"))
num3 = int(input("lado 3:\t"))

a = 0
b = 0
c = 0

if num1 >= num2 and num1 >= num3:
    a = num1
    b = num2
    c = num3
elif num2 >= num1 and num2 >= num3:
    a = num2
    b = num1
    c = num3
else:
    a = num3
    b = num2
    c = num1


print(f"\n\nSeus lados\nLado A:\t{a}\nLado B:\t{b}\nLado C:\t{c}\n")

def ladosTriangulo():
    if a == b and a == c and b == c:
        print("FORMA UM TRIANGULO EQUILATERO")
    elif b == c or b == a or a == c:
        print("FORMA UM TRIANGULO ISOSCELES")
    else:
        print("FORMA UM TRIANGULO ESCALENO")

if a >= b + c:
    print("NÃO FORMA TRIÂNGULO!")
elif a**2 == b**2 + c**2:
    print("TRIÂNGULO RETANGULO SERA FORMADO!")
    ladosTriangulo()
elif a**2 > b**2 + c**2:
    print("TRIÂNGULO OBTUSÂNGULO SERA FORMADO!")
    ladosTriangulo()
elif a**2 < b**2 + c**2:
    print("TRIÂNGULO AGUTÂNGULO SERA FORMADO!")
    ladosTriangulo()
else:
    print("ai tu ta tirando")







