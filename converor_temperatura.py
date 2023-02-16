# Programa conversor temperatura
print("-------------------------")
print("--conversor temperatura--")
print("-------------------------")

# input
C = int(input("digite e valor de c: "))

# procesing 
F = C*1.8 + 32 
K = C + 273.15

#output 
print("--------------------")
print("-----resultados-----")
print("--------------------")

print("la conversion de C a F es: " +str(F))
print("la conversion de C a K es: " +str(K))