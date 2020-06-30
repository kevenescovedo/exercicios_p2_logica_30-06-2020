"""
 Utilize a linguagem de programação PYTHON. Crie um programa que leia um vetor de 10 elementos de nome de produtos e outro vetor de preços de produtos.
 Em outro laço de repetição, mostre o nome do produto e o preço do mesmo, mas
 o preço apresentado para alguns produtos será diferente, pois deve-se aplicar 5% de aumento aos produtos que estão entre os preços de 50 e 70 reais.
"""
produtos = []
precos = []
contador = 1;
index = 0;

while contador <= 10:
    produtos.append(input("Por favor digite o nome de um  produto:\n"))
    precos.append(float(input("Por favor digite o preço do produto:\n")))
                    
    contador = contador + 1;


while index <= 9:
     if precos[index] >= 50 and precos[index] <= 70:
        porcentagem = precos[index] * (5/100)
        aumento = precos[index] + porcentagem
        print("O preço de",produtos[index],"é de",aumento,"Reais")
       
     else:
        print("O preço de", produtos[index],"é de",precos[index],"Reais")
     index = index + 1
     
  
