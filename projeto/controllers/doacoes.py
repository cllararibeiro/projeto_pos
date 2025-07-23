from fastapi import APIRouter, HTTPException
from typing import List
from models import Doacao, DoacaoBase
from datetime import date

router = APIRouter()

doacoes: List[Doacao] = []

@router.post("/doacoes", response_model=Doacao)
def criar_doacao(doacao_base: DoacaoBase):
    novo_id = len(doacoes) + 1
    data = doacao_base.dict()
    if not data.get("data_doacao"):
        data["data_doacao"] = date.today()
    nova_doacao = Doacao(id=novo_id, **data)
    doacoes.append(nova_doacao)
    return nova_doacao


@router.get("/doacoes", response_model=List[Doacao])
def listar_doacoes():
    return doacoes

@router.get("/doacoes/por-nome/{nome_doador}", response_model=List[Doacao])
def listar_por_nome(nome_doador: str):
    resultado = [d for d in doacoes if d.nome_doador.lower() == nome_doador.lower()]
    if not resultado:
        raise HTTPException(404, detail="Nenhuma doação encontrada para esse nome.")
    return resultado
