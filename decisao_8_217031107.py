salario = float(input("Insira o seu salário: "))
vendas = int(input("Insira o número de vendas: "))

if 1000< vendas <= 5000:
    print("Seu salário final é de R$%.2f e o prêmio é de R$500,00"%(500 + salario))
elif 5000< vendas <= 7500:
    print("Seu salário final é de R$%.2f e o prêmio é de R$700,00"%(700 + salario))
elif 7500 < vendas:
    print("Seu salário final é de R$%.2f e o prêmio é de R$1000,00"%(1000 + salario))
else:
    print("Seu salário final é de R$%.2f e você não ganhou prêmio :("%(salario))
