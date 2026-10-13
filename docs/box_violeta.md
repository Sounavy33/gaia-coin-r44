# Box Violeta — Distribuição e Atualização de Gaia na Borda

Box Violeta é a imagem/container/appliance leve destinada a entregar a runtime Gaia para dispositivos de borda com recursos limitados. O objetivo é promover inclusão digital e permitir que usuários com hardware fraco recebam o software e pacotes de atualização sem depender exclusivamente de conexão constante.

Principais características
- Runtime mínimo para Gaia (Gaia runtime + model manager + policy enforcer).
- Suporte para dois perfis de modelo: Very Minimum Reliable (VMR: 0.7–1.3B quant) e Quality Tier (3B quant).
- Atualizações por pacote (.zip) aplicáveis offline (SD-card, pendrive, rádio/transferência local).
- Pacotes contêm: metadados, adapter patch (LoRA-style stub), vetor export (memória), assinatura para integridade.
- Processo opt-in: o usuário decide aplicar pacotes locais ou receber via rede quando autorizado.

Formato do pacote (.zip)
- manifest.json (metadados: version, base_model, adapter_id, created_by, signature_type)
- adapter/ (pasta com adapter patch files — pequenos por design)
- vectors.json (export da memória vetorial local)
- README.patch (descrição humana do pacote)

Fluxo de atualização (offline manual)
1. Usuário recebe pacote Box Violeta (SD/USB).
2. Copia o pacote para o dispositivo e abre Gaia → Atualizar → Selecionar pacote.
3. Gaia verifica assinatura e integridade do pacote.
4. Se verificado, Gaia aplica adapter patch (ou registra vectors em memória) e atualiza metadados locais.
5. Mantém backup dos arquivos antigos em storage (.gaia/backups).

Fluxo de atualização (online opt-in)
1. Usuário autoriza upload de adapter export para servidor de agregação.
2. Servidor agrega patches (com consentimento) e publica um patch agregado.
3. Usuário pode baixar patch agregado e aplicar localmente.

Assinaturas e integridade
- Pacotes devem conter assinatura HMAC-SHA256 ou ed25519 (se o dispositivo possuir chave privada segura).
- Gaia valida assinatura antes de permitir aplicação.

Notas de segurança e privacidade
- Adapters e vetores só são compartilhados com consentimento explícito do usuário.
- Pacotes são assinados para evitar adulteração.
- O sistema prioriza preservação local dos dados: uploads são opt‑in e, por padrão, os usuários controlam o que é compartilhado.
