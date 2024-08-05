from main import BTS

def teste():
  bts = BTS()
  bts.inserir(8)
  bts.inserir(3)
  bts.inserir(10)
  bts.inserir(1)
  bts.inserir(6)
  bts.inserir(14)
  bts.inserir(4)
  bts.inserir(7)
  bts.inserir(50)
  bts.inserir(0)
  bts.inserir(13)

  print(f'Em ordem: ', bts.emOrdem([]))
  print(f'Em pré-ordem: ',bts.preOrdem([]))
  print(f'Em pós-ordem: ',bts.posOrdem([]))

'''
  7
  / \
  3  10
  / \  / \
  1  6  8  14
  / \  / \
  0  4 13 50

'''


teste()