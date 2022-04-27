def search(ano_buscado, noraiz):
    no = noraiz
    numachado = False
    while (no.folha == False):
        for x in range(len(no.chaves)):
          if (ano_buscado <= no.chaves[x]):
               i = no.chaves[x]
               numachado = True
               indice_numachado = x
        if numachado == False:
            up = no.ponteiros[len(no.ponteiros) - 1]
            no = up
        elif (ano_buscado == no.chaves[indice_numachado]):
           no = no.ponteiros[indice_numachado + 1]
        else:
           no = no.ponteiros[indice_numachado]


class node:
    def __init__(self, ponteiros, chaves):
        self.ponteiros = ponteiros
        self.chaves = chaves
        self.pai = False
        self.folha = False






ponteiros = []
chaves = []
ai = [1, 2, 3]
bi = [1, 2, 3]
c = [9]
teste = node(ai, bi)
interno = teste
teste.ponteiros[0] = interno

noraiz = node(ponteiros, chaves)
if ai[0].pai == False:
    if (id(teste) == id(interno)):
        print("iguais")
    else:
        print("diferentes")


