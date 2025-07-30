def fibo(numero):
    if numero == 0:
        return 0
    if numero ==1:
        return 1
    if numero > 1:
        return fibo(numero - 2) + fibo(numero -1)
    
print(fibo(6))