#writelines()
linhas = ["Linha 1\n",
          "Linha 2\n",
          "Linha 3\n"]
with open("Saida.lines.txt", "w") as f:
    f.writelines(linhas)