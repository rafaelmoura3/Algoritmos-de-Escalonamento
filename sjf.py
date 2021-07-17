class Processos:
  def __init__(self, nome, tempo, tamanho):
    self.nome = nome
    self.tempo = tempo
    self.tamanho = tamanho

#Função que gera processos e escalar
def CreateProcessos(quantidade):
  for vet in range(quantidade):
    nome = input("Nome do Processos:")
    tempo = int(input("Tempo em Processamento:"))
    tamanho = int(input("Tamanho do Processos:"))
    yield Processos(nome, tempo, tamanho) 

#Pegar o nome,tamanho do processo e retornar em uma lista
def GetDados(lista_processos):
  for vet in range(len(lista_processos)):
    nome = lista_processos[vet].nome
    tamanho = lista_processos[vet].tamanho
    yield nome, tamanho

#Ordena os processos em ordem crescente com base no tamanho deles como base
def OrdenarDados(lista_dados): 
  return lista_dados.sort(key = lambda retorno: retorno[1])

def OrdenarLista(lsita_processos):
  dados_processos = list(GetDados(lista_processos))
  OrdenarDados(dados_processos)
  return dados_processos

#Função que retorna a fila de processos em execução e os Momento em que quais estão sendo executados
def Listar_Processos(lista_processos):
  dados_processos = OrdenarLista(lista_processos)
  lista_processos = ReposicionarProcesso(lista_processos, dados_processos)
  Momento_processos = CheckProcessoAtual(lista_processos)
  fila_processos = CheckFila(Momento_processos)
  return list(enumerate(zip(Momento_processos, fila_processos)))


def ReposicionarProcesso(lista_processos, dados_processos): 
  lista_reposicionada = []
  for vet_dados in range(len(dados_processos)):
    nome = dados_processos[vet_dados][0] 
    for vet_lista in range(len(lista_processos)):
      if nome == lista_processos[vet_lista].nome: 
        lista_reposicionada.append(lista_processos[vet_lista])
        break
      else: continue
  return lista_reposicionada

#Checa e retorna o processo que está sendo executado
def CheckProcessoAtual(lista_processos):
  resultado_checagem = []
  for vet in range(len(lista_processos)):
    tempo_processo_individual = lista_processos[vet].tempo
    for processo in range(tempo_processo_individual): resultado_checagem.append(lista_processos[vet].nome)
  return resultado_checagem
  
#Checa e retorna a fila dos processos em espera
def CheckFila(Momento_processos):
  fila = "".join(Momento_processos)
  resultado_checagem = []
  for vet in range(1, len(fila)): resultado_checagem.append(fila[vet:])
  resultado_checagem.append("")
  return resultado_checagem

#Printa os Momento de processamento
def Print_Fila(fila_processos):
  for vet in range(len(fila_processos)):
    print("Momento: %i" % (fila_processos[vet][0]))
    print("Processos em Execução: %s" % (fila_processos[vet][1][0]))
    print("Proximo Processos que estão na Fila: %s" % (fila_processos[vet][1][1]))
    print("\n\t\n")

#Printa os Processos na Fila
def Print_Processos(lista_processos):  
  for vet in range(len(lista_processos)):
    print("Processos: %s" % (lista_processos[vet].nome))
    print("Tempo em Milissegundo: %i" % (lista_processos[vet].tempo))
    print("Tamanho em blocos: %i" % (lista_processos[vet].tamanho))
    print("\n\t\n")

quantidade = int(input("Quantos processos deseja escalonar?"))
print("\n")
lista_processos = list(CreateProcessos(quantidade))
print("\n")

fila_processos = Listar_Processos(lista_processos)
fila_processos

print("\tProcessos\n")
Print_Processos(lista_processos)

print("\tMomento\n")
Print_Fila(fila_processos)