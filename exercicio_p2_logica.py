
"""1. Utilize a linguagem de programação PYTHON. Crie um programa que registre cinco pessoas. Delas leia sexo (m/f), peso e altura. Calcule e apresente os seguintes itens:
a) Quantos homens?

b) Quantas mulheres?

c) Média de alturas?

d) Quantas pessoas pesam menos de 30 kg?"""
contador = 1;
qtd_mulheres = 0;
qtd_homens = 0;
soma_alturas = 0;
qtd_pesa_menos_30 = 0;

while contador <= 5:
     sexo = input("digite o sexo da pessoa sendo m(minusculo) para masculino e f(minusculo) para feminino:\n")
     peso = float(input("Digite o peso da pessoa em KG:\n"))
     altura = float(input("Digite a altura da pessoa em Metros:\n"))
     if sexo == "f":
         qtd_mulheres = qtd_mulheres + 1
     elif sexo == "m":
         qtd_homens = qtd_homens + 1
     soma_alturas = soma_alturas + altura
     if peso < 30:
         qtd_pesa_menos_30 = qtd_pesa_menos_30 + 1 
         
     contador = contador + 1;
print(" A quantidade de homens é de:",qtd_homens)
print(" A quantidade de mulheres é de:",qtd_mulheres)
print(" A média de alturas é de:", soma_alturas/5)
print(" A quantidade de pessoas que pesam menos 30 é de:",qtd_pesa_menos_30)

