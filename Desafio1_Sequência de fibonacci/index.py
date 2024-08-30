def verify_fibonacci():
    # Inicia os dois primeiros números da sequência de fibonacci
    a = 0 #Primeiro número da sequência
    b = 1 #Segundo número da sequência
    
    n = int(input('Digite um número: ')) # Solicita ao usuário que informe um número para verificar
    
    if n == 0 or n == 1:
        return True  # Retorna True porque 0 e 1 pertencem à sequência de Fibonacci
    
    
    while b < n:
        temp = b # Variavel para armazenar temporariamente o valor de b
        b = a + b
        a = temp
        
    # Após o loop, verifica se o valor de 'b' é igual ao número informado 'n'
    # Se for igual, significa que 'n' pertence à sequência de Fibonacci, então retorna True
    # Caso contrário, retorna False
    return b == n


# Chama a função verify_fibonacci para determinar se o número informado pertence à sequência de Fibonacci
if verify_fibonacci():
    print('O número digitado pertence à sequência de Fibonacci.')
else:
  print('O número digitado não pertence à sequência de Fibonacci.')

        