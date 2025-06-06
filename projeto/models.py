from pydantic import BaseModel
from datetime import date


class AdminBase(BaseModel):
    nome: str
    email: str
    senha: str
    ong: str


class Admin(AdminBase):
    id: int


class DoadorBase(BaseModel):
    nome: str
    email: str
    telefone: str
    senha: str


class Doador(DoadorBase):
    id: int


class CampanhaBase(BaseModel):
    titulo: str
    descricao: str
    meta_financeira: str
    meta_itens: str
    data_inicio: date
    data_fim: date
    status: bool


class Campanha(CampanhaBase):
    id: int


class CategoriaBase(BaseModel):
    nome: str


class Categoria(CategoriaBase):
    id: int


class DoacaoBase(BaseModel):
    id_doador: int
    id_campanha: int
    tipo_doacao: str
    tipo_item: str
    quantidade: int
    valor: float
    data_doacao: date


class Doacao(DoacaoBase):
    id: int


class RelatorioBase(BaseModel):
    id_campanha: int
    data_referencia: date
    total: float
    total_itens_doados: int
    meta_comparativo: str


class Relatorio(RelatorioBase):
    id: int

