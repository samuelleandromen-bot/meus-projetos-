#calcular media com peso no py

nota1 = float (input("digite a primeira nota"))
peso1= 2

nota2 = float (input("digite a segunda nota"))
peso2 = 3

nota3 = float (input("digite a terceira nota"))
peso4 = 5

media = (nota1 * peso1 + nota2 * peso2 + nota3 * peso4) / (peso1 + peso2 + peso4) / (10)

print("a media é:", media)

if media > 6.0:
    print("vc passou de ano")

else:
    print("vc não passou")
