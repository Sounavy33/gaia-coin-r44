# Consent & Partner Policy — Gaia Coin

## Objetivo
Definir regras claras e vinculantes para parceiros que queiram acessar, processar ou negociar informações relacionadas ao ecossistema GaIA. Prioriza-se privacidade, consentimento explícito e proibição de comercialização de PII sem autorização individual e contrato específico.

## Princípios básicos
- Privacidade primeiro: dados brutos permanecem na borda por padrão. Apenas provas, metadados, receipts e Merkle roots podem ser transmitidos ao Gate Hub.
- Consentimento explícito: qualquer uso adicional de dados deve ser opt‑in, informado e registrado como prova (timestamped consent receipt).
- Minimização: parceiros recebem apenas o mínimo de informação necessário (agregado, anonimizado, ou diferentially private) para o propósito acordado.
- Proibição de revenda de PII: revenda, redistribuição ou uso secundário de PII são estritamente proibidos, salvo consentimento explícito e separado.
- Auditoria pública de usos: logs e metadados (hashes, timestamps, id de acordo) devem ser públicos para auditoria — sem PII.

## Categorias de dados e regras de acesso
1. Dados brutos (conteúdo, arquivos pessoais) — nunca saem da borda sem consentimento explícito e contrato específico. Uso: somente mediante consentimento documentado.
2. Metadados e receipts (hashes, merkle roots, assinaturas) — podem ser enviados para Gate Hub para validação e prova.
3.estatísticas agregadas (sums, counts, modelos agregados) — podem ser compartilhadas se obedecem técnicas de anonimização e differential privacy.

## Regras para parceiros comerciais
- Contrato escrito: todo parceiro deve assinar contrato que define uso permitido, proibições, penalidades e auditoria.
- Atestação técnica: parceiro deve suportar mecanismos de auditoria (verificação de provas, preservação de logs imutáveis).
- Penalidades: violações resultam em revogação de acesso, multas contratuais e publicação do incidente (metadados), além de ações legais conforme aplicável.
- Transparência: parceiros devem publicar relatórios periódicos de uso (metadados) e aceitar auditorias independentes.

## Políticas de monetização
- Monetização por insights/serviços: permitida somente se baseada em dados agregados, anonimização comprovada e consentimento quando aplicável.
- Compartilhamento de receitas: percentuais acordados remuneram o ecossistema (Dividend Pool / Fundo Social), conforme política pública do Tokenomics.

## Consentimento e UX
- Consent receipt: qualquer opt‑in gera um receipt assinado (timestamp, scope, finalidade, duração) guardado no dispositivo e referenciado por hash no Gate Hub.
- Revogação: usuários podem revogar consentimentos; revogação não retroage aos contratos já executados, salvo cláusula contrária.

## Auditoria e conformidade
- Logs imutáveis (hashes) publicados para auditoria pública (sem PII).
- Revisões periódicas por auditoria independente.
- Mecanismos de denúncia e investigação interna.

## Observações finais
Esta política é parte do compromisso de proteger a privacidade dos participantes e garantir que parcerias comerciais sejam legítimas, transparentes e não exploratórias.
