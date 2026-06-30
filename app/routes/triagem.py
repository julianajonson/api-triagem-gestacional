from fastapi import APIRouter
from app.schemas.triagem_schema import RespostasTriagem, DadosGestante
from app.services.scoring_service import (
    calcular_epds,
    calcular_gad7,
    classificar_risco_epds,
    classificar_ansiedade_gad7
)
from app.services.explainability_service import interpretar_fatores
from app.schemas.triagem_schema import ResultadoTriagem
from app.services.orientacao_service import gerar_orientacao
router = APIRouter()


@router.get("/")
def home_triagem():
    return {
        "message": "Serviço de triagem gestacional ativo"
    }


@router.post("/calcular-escores")
def calcular_escores(dados: RespostasTriagem):
    score_epds = calcular_epds(dados.epds)
    score_gad7 = calcular_gad7(dados.gad7)

    return {
        "epds_score": score_epds,
        "epds_classificacao": classificar_risco_epds(score_epds),
        "gad7_score": score_gad7,
        "gad7_classificacao": classificar_ansiedade_gad7(score_gad7),
        "observacao": "Resultado de apoio à triagem. Não substitui avaliação profissional."
    }

@router.post("/interpretar-fatores")
def interpretar_fatores_endpoint(dados: DadosGestante):
    score_epds = calcular_epds(dados.epds)
    score_gad7 = calcular_gad7(dados.gad7)

    fatores = interpretar_fatores(
        score_epds=score_epds,
        score_gad7=score_gad7,
        diagnostico_previo=dados.diagnostico_previo,
        gravidez_planejada=dados.gravidez_planejada,
        apoio_emocional=dados.apoio_emocional,
        situacao_financeira=dados.situacao_financeira
    )

    return {
        "epds_score": score_epds,
        "gad7_score": score_gad7,
        "classificacao_epds": classificar_risco_epds(score_epds),
        "fatores_interpretativos": fatores,
        "observacao": "Interpretação baseada em fatores associados observados no estudo. Não representa diagnóstico clínico."
    }

@router.post("/gerar-orientacao")
def gerar_orientacao_endpoint(resultado: ResultadoTriagem):

    mensagem = gerar_orientacao(
        epds_score=resultado.epds_score,
        gad7_score=resultado.gad7_score,
        classificacao_epds=resultado.classificacao_epds,
        classificacao_gad7=resultado.classificacao_gad7
    )

    return {
        "orientacao": mensagem,
        "aviso": "Esta mensagem possui caráter informativo e não substitui avaliação profissional."
    }