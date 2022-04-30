import math as mt

def silnia():
  n_k = input()
  n_k = n_k.split(" ")
  n_k_tablica_int = [int(x) for x in n_k]
  n = n_k_tablica_int[0]
  k = n_k_tablica_int[1]
  return mt.factorial(n)/(mt.factorial(k)*mt.factorial(n-k))



silnia()
