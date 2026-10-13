# Black Box (cofre destrutivo) — Comportamento e operações

O Black Box é um cofre desenhado para armazenamento de alto risco que, sempre que solicitado, permite a exclusão irrevogável (crypto‑shred) do conteúdo.

Princípios
- Destruição deve ser irreversível: quando o usuário confirma, as chaves são destruídas e os dados tornam‑se inacessíveis.
- Confirmação reforçada: operações destrutivas exigem passphrase + confirmação por múltiplos passos.
- Backups: por padrão, não fazer backups remotos de conteúdos do Black Box. Se fizer, armazenar SOMENTE encriptados e com chaves sob controle do usuário.

Operação técnica (resumo):
1. Cada arquivo no Black Box é encriptado com uma chave simétrica única.
2. A chave simétrica é encriptada com a chave pública do usuário/keystore local.
3. Deleção irrevogável = destruir a chave simétrica e qualquer referência da chave privada -> dados tornam‑se inúteis.
4. Se hardware não permite overwrite físico, usar técnicas de chave única: destruir a chave torna os dados inacessíveis mesmo que bytes permaneçam.

UX
- Aviso claro e irreversível.
- Requer passphrase + confirmação dupla.
- Mostrar o hash do arquivo antes da operação para referência.

Limitações
- Se o usuário perdeu a chave privada, não há recuperação.
- Para dispositivos com armazenamento removível, atenção a cópias residuais em backups ou SD cards.
