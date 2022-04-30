import math as mt

def silnia(liczby):
  n_k = liczby.split(" ")
  n_k_tablica_int = [int(x) for x in n_k]
  n = n_k_tablica_int[0]
  k = n_k_tablica_int[1]
  wynik = int(mt.factorial(n)/(mt.factorial(k)*mt.factorial(n-k)))
  print(wynik)

silnia(input())

