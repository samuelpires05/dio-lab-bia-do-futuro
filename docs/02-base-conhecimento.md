# Base de Conhecimento

## Estrutura de Dados

| Arquivo/Fonte | Formato | Descrição |
|---------------|---------|-----------|
| `perfil_investidor.json` | JSON | Questionário mockado e pontuação para classificar o perfil. |
| `cartilha_renda_fixa.md` | Markdown | Conceitos básicos e oficiais de Renda Fixa (Tesouro Direto, CDB). |
| `cartilha_renda_variavel.md`| Markdown | Conceitos básicos e oficiais de Renda Variável (Ações, FIIs). |

## Fluxo de Integração

1. **Checagem de Perfil:** O agente inicia checando o perfil do investidor.
2. **Busca Segura (RAG):** O agente faz uma busca semântica exclusiva nas cartilhas locais.
3. **Formatação da Resposta:** A resposta é formulada cruzando o System Prompt com a informação técnica.
