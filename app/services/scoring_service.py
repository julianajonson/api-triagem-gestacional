from fastapi import HTTPException


def validar_respostas(respostas: list[int], tamanho_esperado: int, nome_escala: str):
    if len(respostas) != tamanho_esperado:
        raise HTTPException(
            status_code=400,
            detail=f"A escala {nome_escala} deve conter {tamanho_esperado} respostas."
        )

    for resposta in respostas:
        if resposta < 0 or resposta > 3:
            raise HTTPException(
                status_code=400,
                detail=f"Todas as respostas da escala {nome_escala} devem estar entre 0 e 3."
            )


def calcular_epds(epds: list[int]) -> int:
    validar_respostas(epds, 10, "EPDS")
    return sum(epds)


def calcular_gad7(gad7: list[int]) -> int:
    validar_respostas(gad7, 7, "GAD-7")
    return sum(gad7)


def classificar_risco_epds(score_epds: int) -> str:
    if score_epds >= 13:
        return "risco elevado"
    elif score_epds >= 10:
        return "risco moderado"
    return "baixo risco"


def classificar_ansiedade_gad7(score_gad7: int) -> str:
    if score_gad7 >= 15:
        return "ansiedade severa"
    elif score_gad7 >= 10:
        return "ansiedade moderada"
    elif score_gad7 >= 5:
        return "ansiedade leve"
    return "ansiedade mínima"