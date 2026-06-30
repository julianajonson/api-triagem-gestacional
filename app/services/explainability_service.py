def interpretar_fatores(
    score_epds: int,
    score_gad7: int,
    diagnostico_previo: bool | None = None,
    gravidez_planejada: bool | None = None,
    apoio_emocional: str | None = None,
    situacao_financeira: str | None = None
) -> list[dict]:
    fatores = []

    if score_gad7 >= 10:
        fatores.append({
            "fator": "Sintomas de ansiedade",
            "nivel": "alto",
            "explicacao": "Pontuação elevada no GAD-7 foi considerada um fator associado ao maior risco de sintomas depressivos."
        })
    elif score_gad7 >= 5:
        fatores.append({
            "fator": "Sintomas de ansiedade",
            "nivel": "moderado",
            "explicacao": "Pontuação leve a moderada no GAD-7 pode indicar necessidade de atenção no acompanhamento psicossocial."
        })

    if diagnostico_previo is True:
        fatores.append({
            "fator": "Histórico prévio de depressão ou ansiedade",
            "nivel": "alto",
            "explicacao": "Diagnóstico prévio foi considerado um fator relevante na interpretação do risco psicossocial."
        })

    if gravidez_planejada is False:
        fatores.append({
            "fator": "Gravidez não planejada",
            "nivel": "moderado",
            "explicacao": "Gestação não planejada pode aumentar vulnerabilidades emocionais e sociais durante a gravidez."
        })

    if apoio_emocional:
        apoio = apoio_emocional.lower()

        if apoio in ["baixo", "ruim", "insuficiente", "não", "nao", "nenhum"]:
            fatores.append({
                "fator": "Baixo apoio emocional",
                "nivel": "alto",
                "explicacao": "Apoio emocional insuficiente foi considerado um fator psicossocial relevante."
            })

    if situacao_financeira:
        situacao = situacao_financeira.lower()

        if situacao in ["ruim", "instável", "instavel", "difícil", "dificil"]:
            fatores.append({
                "fator": "Instabilidade financeira",
                "nivel": "moderado",
                "explicacao": "Condições financeiras desfavoráveis podem contribuir para maior vulnerabilidade psicossocial."
            })

    if not fatores:
        fatores.append({
            "fator": "Nenhum fator adicional crítico informado",
            "nivel": "baixo",
            "explicacao": "Com os dados informados, não foram identificados fatores psicossociais adicionais de maior atenção."
        })

    return fatores