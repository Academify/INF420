# Nome: Thiago Ferreira 
# Matricula: 98893

from Posicao import Posicao
from AEstrela import AEstrela
from QuebraCabeca import QuebraCabeca
from QuebraCabecaImp import QuebraCabecaImp
from heapq import heappush, heappop
from copy import deepcopy

class AEstrelaImp(AEstrela):
  def getSolucao(self, qc):

    resolvido = False  # Se o quebra cabeca esta resolvido
    resposta = []  # Resposta

    initial = qc.hashCode()  # Hash inicial
    fila = [(qc.getValor(), initial, qc)]  # Fila de prioridade
    distancias = {qc.hashCode(): 0}  # Distancias
    anterior = {qc.hashCode(): -1}  # Anterior
    vazio = {qc.hashCode(): qc.getPosVazio()}  # Posicao do vazio

    while fila:  # Enquanto a fila nao estiver vazia
      custo, cd, unset = heappop(fila)  # Pega o menor custo
      if cd not in vazio:  # Se o codigo nao esta na lista de vazios
        vazio[cd] = unset.getPosVazio()  # Adiciona o codigo na lista de vazios

      if unset.isOrdenado():  # Se o quebra cabeca esta ordenado
        resolvido = True  # Achou
        hashOrdenado = unset.hashCode()  # Codigo do quebra cabeca
        break  # Para o loop

      if custo - unset.getValor() > distancias[cd]:  # Se o custo - o valor do quebra cabeca for maior que a distancia do codigo
        continue  # Continua o loop

      movimentos = unset.getMovePossiveis()  # Pega os movimentos possiveis

      for movimento in movimentos:  # Para cada movimento
        qcaux = deepcopy(unset)  # Cria um novo quebra cabeca
        qcaux.move(vazio[cd].getLinha(), vazio[cd].getColuna(), movimento.getLinha(), movimento.getColuna())  # Move o vazio
        cd_qcaux = qcaux.hashCode()  # Pega o codigo do quebra cabeca

        if cd_qcaux not in distancias or distancias[cd_qcaux] > distancias[cd] + 1:  # Se o codigo nao esta na lista de distancias ou a distancia do codigo for maior que a distancia do codigo + 1
          distancias[cd_qcaux] = distancias[cd] + 1  # Adiciona o codigo na lista de distancias
          anterior[cd_qcaux] = cd  # Adiciona o codigo na lista de anteriores
          heappush(fila, (distancias[cd_qcaux] + qcaux.getValor(), cd_qcaux, qcaux))  # Adiciona o codigo na fila de prioridade

    if resolvido:  # Se achou
      cd = hashOrdenado  # Codigo do quebra cabeca

    while anterior[cd] != -1:  # Enquanto o anterior do código atual for diferente de -1
      resposta.append(vazio[cd])  # Adiciona o codigo na lista de solucao
      cd = anterior[cd]  # Codigo atual recebe o anterior do codigo atual

    resposta.reverse()  # Inverte a lista de solucao

    return resposta  # Retorna a lista de solucao
