# Avaliação e Métricas

## Objetivo

Verificar se o assistente responde corretamente utilizando apenas sua base de conhecimento.


## Critérios Avaliados

### Precisão

Verifica se a resposta está correta.

Resultado esperado:
Resposta correta.


### Clareza

Verifica se o usuário consegue compreender facilmente a resposta.

Resultado esperado:
Resposta simples e objetiva.


### Fidelidade

Verifica se o agente respondeu apenas utilizando sua base de conhecimento.

Resultado esperado:
Nenhuma informação inventada.


### Robustez

Verifica o comportamento quando recebe perguntas fora do domínio.

Resultado esperado:

O agente informa que não possui conhecimento suficiente.


## Casos de Teste

### Caso 1

Pergunta:

"O que é Python?"

Resultado esperado:

Resposta correta.

Status:

Aprovado.


### Caso 2

Pergunta:

"O que faz o comando JOIN?"

Resultado esperado:

Resposta correta.

Status:

Aprovado.


### Caso 3

Pergunta:

"Quem descobriu o Brasil?"

Resultado esperado:

Informar que não possui essa informação.

Status:

Aprovado.


### Caso 4

Pergunta:

"Explique Banco de Dados."

Resultado esperado:

Resposta baseada na base de conhecimento.

Status:

Aprovado.
