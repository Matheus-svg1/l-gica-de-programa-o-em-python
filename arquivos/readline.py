#readline()
with open("exemplo.txt", "r") as f:      #readline() busca somente uma linha por vez, caso você queira mais de uam linha é necessario usar o print
    linha1= f.readline()
    print(linha1)
    linha2 = f.readline()
    print(linha2)
