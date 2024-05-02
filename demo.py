"""
    This file serves as a demo of Structures.
    It also serves as a testing ground so I don't test directly inside the libraries...
"""
import Structures as S
import random as r

mappy : S.matrix
marvelfiller : S.matrix
monstro : S.alcazar
marvel : S.graph
newGuy : S.matrix

#creating our main men
mappy = S.matrix(5,5,'.')
monstro = S.alcazar(5,10,10,"monstro",'#')
marvelfiller = S.matrix.numberFlood(S.matrix(r.randint(2,10),r.randint(2,10)).iterable(),0,5)
marvel = S.graph.matrixToGraph(marvelfiller.iterable())

S.matrix.matrixToCSV(filenameNEW="mappy.txt",Iterableof2D=marvelfiller.iterable())
newGuy = S.matrix.CSVToMatrix("mappy.txt")

marvelfiller.archaicPrint()
newGuy.archaicPrint()




