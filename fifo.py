class Processos:
  def __init__(self, nome, tempo):
    self.nome = nome
    self.tempo = tempo
    
def Create_Processoss(quantidade):
  vet = 0
  while vet < quantidade:
    nome = input("Nome do Processos:")
    tempo = int(input("Tempo de Processamento:"))
    vet += 1
    yield Processos(nome, tempo) 

#Retorna a fila de processoss em execução e os Momentos em que estão sendo executados
def List_Processoss(lista_processoss):
  Momento_processoss = Check_Processos_Atual(lista_processoss)
  fila_processoss = Check_Fila(Momento_processoss)
  return list(enumerate(zip(Momento_processoss, fila_processoss)))

#Checa e retorna a fila dos processos em espera
def Check_Fila(Momento_processoss):
  
  fila = "".join(Momento_processoss)
  result_check = []
  for vet in range(1, len(fila)): result_check.append(fila[vet:])
  result_check.append("")
  return result_check

#Checa e retorna o processos que está sendo executado
def Check_Processos_Atual(lista_processoss):
  result_check = []

  for vet in range(len(lista_processoss)):
    tempo_processos_individual = lista_processoss[vet].tempo
    for processos in range(tempo_processos_individual): result_check.append(lista_processoss[vet].nome)
  return result_check

#Printar os Momento de processamento
def Print_Fila(fila_processoss):
  for vet in range(len(fila_processoss)):
    print("Momento: %i" % (fila_processoss[vet][0]))
    print("Processos em Execução: %s" % (fila_processoss[vet][1][0]))
    print("Proximos Processoss que estão na Fila: %s" % (fila_processoss[vet][1][1]))
    print("\n\t\n")

def Print_Processoss(lista_processoss):
  for vet in range(len(lista_processoss)):
    print("Processos: %s" % (lista_processoss[vet].nome))
    print("Tempo em Milissegundo: %i" % (lista_processoss[vet].tempo))
    print("\n\t\n")

quantidade = int(input("Quantos processoss deseja escalonar?"))
print("\n")
lista_processoss = list(Create_Processoss(quantidade))
print("\n")
fila_processoss = List_Processoss(lista_processoss)
print("\tProcessoss\n")
Print_Processoss(lista_processoss)
print("\tMomento\n")
Print_Fila(fila_processoss)