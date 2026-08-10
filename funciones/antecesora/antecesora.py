def antecesor(n):
    return n - 1

a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))

for i in range(b):
    a = antecesor(a)

print("La resta es:", a)
