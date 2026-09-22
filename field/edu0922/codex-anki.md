# Codex + Anki

Servidor MCP local para consultar baralhos e notas, criar baralhos e cartões, editar campos e adicionar etiquetas. Requer Node.js 22 ou superior, Anki aberto com um perfil carregado e AnkiConnect.

## Ativar

1. No Anki: Ferramentas → Complementos → Obter complementos → código `2055492159`.
2. Reinicie o Anki.
3. Reinicie o Codex para carregar o servidor MCP `anki` já registrado nesta máquina.
4. Peça: “Liste meus baralhos do Anki” ou “Crie cinco cartões sobre este texto no baralho Direito”.

O servidor usa somente `http://127.0.0.1:8765`. Não exige chave da OpenAI. Se você configurar uma chave no AnkiConnect, defina `ANKI_API_KEY` no ambiente do servidor MCP.

Notas duplicadas são recusadas. Não há ferramentas de exclusão ou de alteração do histórico de revisão. A edição de campos preserva os campos não informados. Após falha de comunicação em uma escrita, consulte a coleção antes de tentar novamente.

## Desenvolvimento

Execute `node --test test.mjs` nesta pasta. Não há dependências externas. O teste usa AnkiConnect simulado e não altera a coleção real. Para verificar a conexão real sem editar cartões, execute `node check-connection.mjs`.

Para registrar em outra instalação, execute `codex mcp add anki -- node CAMINHO_ABSOLUTO/server.mjs`.

Referências: https://developers.openai.com/codex/mcp e https://ankiweb.net/shared/info/2055492159.
