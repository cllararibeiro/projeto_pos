from fastapi import APIRouter, HTTPException
from typing import List
from models import Campanha, CampanhaBase
from datetime import date


router = APIRouter()

campanhas: List[Campanha] = []

# Listar todas as campanhas
@router.get("/campanhas", response_model=List[Campanha])
def listar_campanhas():
    return campanhas

# Buscar campanha pelo título
@router.get("/campanhas/{titulo}", response_model=Campanha)
def buscar_campanha_por_titulo(titulo: str):
    for campanha in campanhas:
        if campanha.titulo == titulo:
            return campanha
    raise HTTPException(status_code=404, detail="Campanha não encontrada")

@router.post("/campanhas", response_model=Campanha)
def criar_campanha(campanha_base: CampanhaBase):
    for campanha in campanhas:
        if campanha.titulo == campanha_base.titulo:
            raise HTTPException(status_code=400, detail="Título já cadastrado.")
    novo_id = len(campanhas) + 1
    campanha = Campanha(id=novo_id, **campanha_base.dict())
    campanhas.append(campanha)
    return campanha


# Editar campanha pelo título
@router.put("/campanhas/{titulo}", response_model=Campanha)
def editar_campanha_por_titulo(titulo: str, dados: CampanhaBase):
    for i, campanha in enumerate(campanhas):
        if campanha.titulo == titulo:
            campanhas[i] = Campanha(id=campanha.id, **dados.dict())
            return campanhas[i]
    raise HTTPException(status_code=404, detail="Campanha não encontrada")

# Excluir campanha pelo título
@router.delete("/campanhas/{titulo}", response_model=Campanha)
def excluir_campanha_por_titulo(titulo: str):
    for i, campanha in enumerate(campanhas):
        if campanha.titulo == titulo:
            return campanhas.pop(i)
    raise HTTPException(status_code=404, detail="Campanha não encontrada")

