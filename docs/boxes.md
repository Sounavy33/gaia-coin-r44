# Boxes — Definição e Regras de Uso

Este documento descreve as caixas (Boxes) utilizadas pelo sistema Gaia para organização, privacidade e fluxo de atualização.

Boxes iniciais (mínimo 4):

1. Box Violeta (violet)
   - Propósito: pacotes de atualização (Box Violeta), patches, adapters e pacotes aplicáveis offline.
   - Uso: pacotes assinados (.zip). Aplicação local no dispositivo.
   - Compartilhamento: opt‑in; manifestos e hashes podem ser publicados para auditoria.

2. Box Blue (blue)
   - Propósito: armazenamento aberto do usuário para itens que desejam compartilhar ou tornar facilmente exportáveis.
   - Uso: notas públicas, arquivos exportáveis, conteúdo para autônomos.
   - Compartilhamento: opt‑out por padrão (aberto por design se usuário optar).

3. Box Red (red)
   - Propósito: armazenamento privado do usuário. Conteúdo encriptado, apenas o usuário tem a chave.
   - Uso: documentos sensíveis que não devem ser publicados, backups encriptados.
   - Compartilhamento: nunca sem consentimento explícito.

4. Box Black (black)
   - Propósito: cofre destrutivo (crypto‑shred). Conteúdo que, ao ser deletado, deve se tornar irrecuperável.
   - Uso: segredos extremos, chaves privadas, material comprometedor que o usuário deseja remover de forma definitiva.
   - Compartilhamento: NÃO; referência demonstrativa e de alto risco. Requer confirmação dupla/tripla.

Notas sobre extensão:
- Podemos adicionar até 7 boxes/cores conforme a necessidade (ex.: Hatch, Green, Yellow).
- Cada box tem políticas próprias de retenção, encriptação e compartilhamento.

Fluxos importantes:
- Aplicação de Box Violeta: verificação de assinatura → sandboxed apply → backup automático → commit do manifest.
- Restauração de Box Red/Black: uso de chaves locais do usuário; Black exige confirmação e passphrase para destruir a chave.

Auditoria e metadados:
- Todos os itens possuem metadados (.meta.json) e hash SHA256.
- Apenas metadados e hashes podem ser publicados no Gate Hub/GitHub para auditoria (sem dados brutos).
