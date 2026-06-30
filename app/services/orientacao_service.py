def gerar_orientacao(
    epds_score: int,
    gad7_score: int,
    classificacao_epds: str,
    classificacao_gad7: str
) -> str:
    if classificacao_epds == "risco elevado":
        return (
            "A pontuação obtida sugere a presença de sintomas depressivos "
            "que merecem atenção especializada. Recomenda-se procurar "
            "avaliação de um profissional de saúde mental ou da equipe "
            "de pré-natal para acompanhamento adequado."
        )

    if classificacao_epds == "risco moderado":
        return (
            "Foram identificados sinais que indicam atenção ao bem-estar "
            "emocional durante a gestação. O acompanhamento psicológico "
            "e o fortalecimento da rede de apoio podem ser benéficos."
        )

    return (
        "Os resultados não indicam sinais importantes de risco neste momento. "
        "Mesmo assim, é importante manter acompanhamento pré-natal regular "
        "e observar alterações emocionais ao longo da gestação."
    )