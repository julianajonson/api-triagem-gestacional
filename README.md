*API de Triagem Psicossocial Gestacional

API REST desenvolvida com FastAPI para apoio à triagem psicossocial de gestantes, utilizando informações derivadas dos instrumentos EPDS (Edinburgh Postnatal Depression Scale) e GAD-7 (Generalized Anxiety Disorder Assessment).

A aplicação realiza o cálculo de escores, interpreta fatores de risco e gera orientações iniciais com base nos resultados obtidos.

Aviso: Esta API possui finalidade educacional e acadêmica. Não substitui avaliação, diagnóstico ou acompanhamento realizado por profissionais de saúde.

*Objetivo

O projeto foi desenvolvido com o objetivo de demonstrar a construção de uma API REST utilizando boas práticas de desenvolvimento, organização em camadas, validação de dados e documentação automática.

Além do aspecto técnico, a solução foi inspirada em um estudo sobre saúde mental perinatal, buscando transformar conhecimento acadêmico em uma aplicação prática.

*Funcionalidades
- Cálculo de Escores
Calcula automaticamente os escores dos instrumentos EPDS e GAD-7 a partir das respostas informadas.

Endpoint
POST /v1/triagem/calcular-escores

- Interpretação dos Fatores de Risco

Analisa características psicossociais e gera interpretações relacionadas aos possíveis fatores de vulnerabilidade.

Endpoint
POST /v1/triagem/interpretar-fatores

- Geração de Orientações

Gera recomendações iniciais de acordo com os resultados obtidos nos instrumentos e fatores informados.

Endpoint

POST /v1/triagem/gerar-orientacao

- Health Check

Verifica se a aplicação está em funcionamento.

Endpoint
GET /health

*Tecnologias Utilizadas
Python 3.12
FastAPI
Pydantic
Uvicorn
OpenAPI / Swagger

*Estrutura do Projeto
app/
├── core/
│   ├── config.py
│   ├── logger.py
│   └── security.py
│
├── routes/
│   └── triagem.py
│
├── schemas/
│   └── triagem_schema.py
│
├── services/
│   ├── scoring_service.py
│   ├── explainability_service.py
│   └── orientacao_service.py
│
└── main.py

A arquitetura foi organizada em camadas para facilitar manutenção, escalabilidade e separação de responsabilidades.

*Instalação

Clone o repositório:

git clone https://github.com/seu-usuario/api-triagem-gestacional.git

Acesse a pasta do projeto:

cd api-triagem-gestacional

Crie um ambiente virtual:

python -m venv .venv

Ative o ambiente:

Windows
.venv\Scripts\activate
Linux/Mac
source .venv/bin/activate

Instale as dependências:

pip install -r requirements.txt
Executando a Aplicação
uvicorn app.main:app --reload

A API ficará disponível em:

http://127.0.0.1:8000
Documentação Interativa

Swagger UI:

http://127.0.0.1:8000/docs

ReDoc:

http://127.0.0.1:8000/redoc
Exemplo de Requisição
Cálculo dos Escores
{
  "epds_respostas": [3,2,2,1,2,1,2,1,1,0],
  "gad7_respostas": [2,2,1,1,2,1,1],
  "idade": 28,
  "primeira_gestacao": true,
  "gravidez_planejada": false,
  "apoio_emocional": "baixo",
  "situacao_financeira": "instavel",
  "diagnostico_previo": true
}
Exemplo de Resposta
{
  "epds_score": 15,
  "gad7_score": 10,
  "classificacao_epds": "Risco Elevado",
  "classificacao_gad7": "Ansiedade Moderada"
}
Motivação

Este projeto foi inspirado em uma pesquisa sobre fatores associados a sintomas depressivos durante a gestação, realizada com gestantes brasileiras utilizando os instrumentos EPDS e GAD-7.

O objetivo foi aplicar conceitos de desenvolvimento de APIs REST a um contexto real da área da saúde, promovendo a integração entre tecnologia, análise de dados e impacto social.

Autora

Juliana Jonson