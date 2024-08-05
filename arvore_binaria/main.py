'''
Percurso em Ordem:
- Esquerda, Raiz e Direita

Percurso em pré-ordem:
- Raiz, esquerda e direita

Percurso em pós-ordem:
- Esquerda, direita e raiz

'''
class BTS:
  def __init__(self, dado=None):
    self.dado = dado
    self.esquerda = None
    self.direita = None

  
  def inserir(self, dado):
    if (self.dado == None):
      self.dado = dado
    else:
      if (dado < self.dado):
        if (self.esquerda):
          self.esquerda.inserir(dado)
        else:
          self.esquerda = BTS(dado)
      
      else:

        if (self.direita):
          self.direita.inserir(dado)
        else:
          self.direita = BTS(dado)
  
  def preOrdem(self, lst):
    if (self.esquerda):
      self.esquerda.emOrdem(lst)
    lst.append(self.dado) # raiz

    if (self.direita):
      self.direita.emOrdem(lst)

    return lst
  

  def emOrdem(self, lst):
    if self.esquerda:
        self.esquerda.emOrdem(lst)
    lst.append(self.dado)
    if self.direita:
        self.direita.emOrdem(lst)
    return lst
  

  def posOrdem(self, lst):
    if (self.esquerda):
      self.esquerda.posOrdem(lst)
    if (self.direita):
      self.direita.posOrdem(lst)
    
    lst.append(self.dado)

    return lst
  

