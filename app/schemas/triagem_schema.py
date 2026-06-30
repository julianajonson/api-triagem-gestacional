from pydantic import BaseModel, Field
from typing import List, Optional


class RespostasTriagem(BaseModel):
    epds: List[int] = Field(
        ...,
        min_length=10,
        max_length=10,
        description="Lista com 10 respostas da escala EPDS, valores de 0 a 3."
    )

    gad7: List[int] = Field(
        ...,
        min_length=7,
        max_length=7,
        description="Lista com 7 respostas da escala GAD-7, valores de 0 a 3."
    )

class DadosGestante(BaseModel):
    epds: List[int] = Field(..., min_length=10, max_length=10)
    gad7: List[int] = Field(..., min_length=7, max_length=7)

    idade: Optional[int] = Field(None, ge=10, le=60)
    primeira_gestacao: Optional[bool] = None
    gravidez_planejada: Optional[bool] = None
    apoio_emocional: Optional[str] = None
    situacao_financeira: Optional[str] = None
    diagnostico_previo: Optional[bool] = None

class ResultadoTriagem(BaseModel):
    epds_score: int
    gad7_score: int
    classificacao_epds: str
    classificacao_gad7: str