# Gate Hub — Verificação Primária de Borda

Este módulo implementa a verificação obrigatória de nós de borda antes da operação do ecossistema Gaia.

## Visão geral
O Gate Hub atua como porta de entrada e oráculo de verificação para todo nó de borda do ecossistema Gaia.

## Regras do Gate Hub
1. Check-in obrigatório: nenhum nó pode emitir dividendos ou processar tokens R44 sem validação prévia de conectividade e telemetria no Gate Hub.
2. Checagem de saúde do hardware: valida se a inteligência de borda teve ambiente operacional suficiente para executar o runtime local.
3. Barreira antifraude: desativa a atribuição de cashback para nós corrompidos, inativos ou em versões descontinuadas antes da execução da regra de negócio.
4. Economia de recursos: reduz tráfego de rede verificando a integridade local antes de autorizar sincronizações com a nuvem.

## Fluxo principal
- registrar_ou_atualizar_no(id_no, versao_slm, status_hardware)
- checar_status_no(id_no)

Esses métodos validam:
- status_hardware
- compatibilidade de versão mínima
- aptidão do nó para ficar online e operar

## Observação
O processo é conservador e privilegia segurança, consistência e auditabilidade. Nenhum nó sem muito controle de borda deve participar de emissão de benefício ou cashback sem passar pelo Gate Hub.

## Parceiros experimentais
Também estamos considerando uma parceria experimental com Gemini para avaliação e checagem em conjunto com o GitHub, sempre com fluxos de autoridade e consentimento explícitos. O foco será em metadados, hashes e receipts, nunca em dados brutos sem autorização do usuário.
