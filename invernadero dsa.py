temperaturas = []
for i in range(5):
            temp = int(input("ingresa temp"))
            temperaturas.append(temp)

            prom=sum(temperaturas)/len(temperaturas)
            t_max = max(temperaturas)
if temperaturas <= 15 and 30:
    print("las temperaturas estan bajo 15 y 30° ")
    else:
    print("ADVERTENCIA, TEMPERATURAS FUERA DE 10 Y 35 GRADOS.")
