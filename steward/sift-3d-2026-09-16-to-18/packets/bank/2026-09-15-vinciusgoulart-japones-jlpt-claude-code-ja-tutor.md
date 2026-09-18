---
id: 2026-09-15-vinciusgoulart-japones-jlpt-claude-code-ja-tutor
kind: article
title: japones-jlpt — Claude Code JA tutor mesa+trajeto Anki loop
source: "https://github.com/VinciusGoulart/japones-jlpt"
author: VinciusGoulart
published: 2026-09-06
captured: 2026-09-15
via: grok-bot/Field
lane: learning
status: raw
private: false
---

=== README ===
# 日本語 — Sistema de estudo de japonês com Claude Code

Do **zero absoluto ao JLPT N3**, com o [Claude Code](https://claude.com/claude-code) como tutor e gestor de rotina. Este repositório é o sistema completo: currículo, ferramentas, skills e automações — em uso real desde 03/08/2026.

## Como funciona

O estudo tem **duas frentes**, que falham por motivos diferentes e por isso são medidas separadamente:

- **Mesa (1h/dia)** — a sessão conduzida pelo Claude no terminal (`/estudo`): gramática nova, produção ativa de frases, correção com o porquê, e geração automática dos cartões de Anki do dia.
- **Trajeto (~2h/dia)** — Anki e áudio no celular, sem o Claude. É o que transforma a aula em memória de longo prazo.

O ciclo se fecha sozinho: a mesa gera vocabulário → um `.apkg` é importado no Anki do PC via AnkiConnect → o AnkiWeb sincroniza com o celular → o tutor lê a coleção real no dia seguinte e ajusta a rota com números, não com impressão.

## O que tem aqui

```
CLAUDE.md            — o contrato do tutor: papel, regras de conduta, perfil do estudante
plano/
  curriculo.md       — a sequência de conteúdo, dia a dia (o real, não o idealizado)
  roadmap.md         — fases e calendário JLPT
  metodo.md          — como estudar: estrutura da sessão, ferramentas, regras
progresso/
  vocabulario.tsv    — todo o vocabulário das sessões (fonte dos decks)
  estado.exemplo.json— esqueleto do estado, para começar o seu
.claude/skills/
  estudo/            — /estudo: a sessão diária de 1h
  progresso/         — /progresso: relatório e correção de rota
tools/
  gerar_vocab_apkg.py— tsv → .apkg → importação automática (AnkiConnect) → sync
  anki_status.py     — lê a coleção real do Anki (fila, retenção, minutos/dia)
  trello.py          — ponte com o board de acompanhamento (checklists, pendências)
anki/                — decks de kana prontos (.apkg) e geradores
```

O diário de sessões e o estado pessoal ficam fora do repositório (ver `.gitignore`) — o método é público, a vida não.

## Quer montar o seu?

Leia **[COMECE-O-SEU.md](COMECE-O-SEU.md)** — o passo a passo para clonar o sistema, zerar o estado e começar do seu próprio zero.

## Princípios que fazem o sistema funcionar

1. **Nunca inventar japonês** — dúvida honesta custa menos que erro fossilizado.
2. **60 minutos e acabou** — o que sustenta a meta é voltar amanhã.
3. **Repetição espaçada acima de tudo** — revisão atrasada vira sessão só de revisão.
4. **Produção ativa todo dia** — reconhecer não é saber.
5. **Registrar sempre** — sessão sem registro é sessão perdida para o planejamento.
6. **Texto na conversa não se cobra; card com data se cobra** — todo pedido operacional vira card com vencimento no Trello.
7. **Medir com dados, não com impressão** — o tutor lê a coleção do Anki, não o relato.

=== COMECE-O-SEU.md ===
# Comece o seu — do zero ao seu próprio sistema

Este guia monta uma cópia limpa do sistema para **você**, com o seu perfil, o seu board e o seu Anki. Tempo estimado: ~40 minutos, uma vez só.

## 0. Pré-requisitos

- [Claude Code](https://claude.com/claude-code) instalado e funcionando no terminal
- Python 3 (já vem no Linux/macOS)
- Conta gratuita no [Trello](https://trello.com) e no [AnkiWeb](https://ankiweb.net)
- [Anki desktop](https://apps.ankiweb.net) no PC e AnkiDroid/AnkiMobile no celular

## 1. Clone e limpe

```bash
git clone https://github.com/VinciusGoulart/japones-jlpt.git meu-japones
cd meu-japones
cp progresso/estado.exemplo.json progresso/estado.json
echo "# Diário de sessões" > progresso/diario.md
```

O `.gitignore` já mantém `diario.md` e `estado.json` fora do git — seu progresso é seu.

Se você também parte do zero absoluto, **zere o vocabulário** (o arquivo vem com o vocabulário do dono original; as primeiras linhas `#` são o cabeçalho e ficam):

```bash
head -5 progresso/vocabulario.tsv > /tmp/vocab && mv /tmp/vocab progresso/vocabulario.tsv
```

## 2. Adapte o contrato do tutor

Abra o `CLAUDE.md` e reescreva a seção **Perfil do Estudante** com a SUA realidade: nome, cidade, nível inicial, quanto tempo você tem por dia (mesa e trajeto), e a meta com data. **Seja honesto no orçamento de horas** — o plano inteiro deriva daí, e meta que não fecha na conta vira frustração com data marcada.

Depois peça ao Claude, na primeira conversa: *"leia o CLAUDE.md e o plano/, e recalibre o roadmap para o meu perfil"*.

## 3. Trello (o cobrador)

1. Crie um board com as listas: `🔄 Semana atual`, `🎧 Audio (30 min/dia)`, `⚡ Pendencias`, `📅 Avisos do JLPT`, `Concluído`.
2. Pegue key e token em https://trello.com/app-key
3. Credenciais **fora do repositório** (ele pode virar público um dia):

```bash
mkdir -p ~/.config/japones
printf 'TRELLO_KEY=SUA_KEY\nTRELLO_TOKEN=SEU_TOKEN\n' > ~/.config/japones/trello.env
chmod 600 ~/.config/japones/trello.env
```

4. Troque o `BOARD_ID` no topo de `tools/trello.py` pelo id do seu board (está na URL dele) e rode `python3 tools/trello.py setup`.

## 4. Anki (o motor da memória)

1. No PC: instale o Anki, entre na sua conta AnkiWeb.
2. No celular: AnkiDroid/AnkiMobile, mesma conta, sincronização automática ligada.
3. **Kanji legível**: `sudo apt install fonts-noto-cjk` (sem isso, dakuten vira cisco e você "erra" o que não enxerga).
4. Add-on **AnkiConnect** (código `2055492159`, Tools → Add-ons → Get Add-ons) — é o que deixa o tutor importar os cartões do dia sozinho.
5. Baixe o deck de vocabulário [Kaishi 1.5k](https://github.com/donkuri/kaishi) e configure **10 cartões novos/dia** (não mais — 20/dia no começo é o erro que mais faz abandonar o Anki no terceiro mês).
6. Os decks de kana desta pasta (`anki/*.apkg`) são seus: importe o da semana 1 e comece.

## 5. A primeira sessão

```bash
claude
> /estudo
```

O tutor lê o estado (zerado), vê que é o dia 1, e começa do あ. A partir daí é rotina: 1h de mesa por dia, Anki e áudio no resto. O sistema cuida do resto — cartões, cobranças, correção de rota.

## As três regras que não se negociam

1. **Consistência vale mais que intensidade.** 1h todo dia ganha de 7h no domingo.
2. **O Anki decide o que revisar, não você.** Confie no algoritmo e use o botão Again sem culpa — ele é informação, não derrota.
3. **Produza todo dia.** Frase sua, errada e corrigida, vale mais que dez reconhecidas.

頑張ってください！

=== plano/metodo.md ===
# Método — duas frentes por dia

O estudo acontece em dois lugares com naturezas diferentes. Entender essa divisão é o que faz o plano caber na rotina de quem trabalha em período integral.

| Frente | Onde | Quanto | Para quê |
|---|---|---|---|
| **Trajeto** | Celular, ida e volta do trabalho | ~2h em dias úteis | **Volume**: repetição espaçada de vocabulário e kanji, mais áudio |
| **Mesa** | Computador, com Claude | 1h todos os dias | **Profundidade**: gramática nova, produção de frases, correção |

A regra que amarra as duas: **a mesa alimenta o trajeto**. Toda sessão de mesa termina gerando os cartões que vão para o Anki, e o trajeto do dia seguinte os transforma em memória.

---

## Frente 1 — Trajeto (~2h, celular)

Repetição espaçada em pé no ônibus funciona muito bem, porque o Anki é feito de sessões picadas de poucos minutos. É aqui que se resolve o maior gargalo do N3: os ~650 kanji e ~3.700 palavras.

**Divisão sugerida das 2 horas:**

| Bloco | Tempo | O quê |
|---|---|---|
| Anki — revisões devidas | ~60 min | A fila do dia. Prioridade absoluta. |
| Anki — cartões novos | ~30 min | 15 a 20 por dia na Fase 1. Nunca aumentar se a fila de revisão estiver crescendo. |
| Áudio | ~30 min | Podcast/listening. Vale mesmo sem entender no começo. |

**Se o trajeto for de carro dirigindo**, o Anki sai e sobra só o áudio — nesse caso avise no `/estudo`, porque a projeção de horas do plano muda bastante e o `/progresso` precisa saber.

### Regra do volume
Cartões novos por dia é o acelerador, e ele tem freio: se a fila de revisões passar de ~200 atrasados, **zere os cartões novos** até a fila voltar ao normal. Fila crescente é dívida técnica de memória — juros altos, e cobra tudo de uma vez perto da prova.

---

## Frente 2 — Mesa (1h, com Claude)

Como o vocabulário e os kanji já são tratados no trajeto, a hora de mesa fica inteira para o que o Anki **não** faz.

| Bloco | Tempo | O que acontece |
|---|---|---|
| **1. Aferição** | 5 min | Como foi o trajeto: quantos cartões, o que travou. Alimenta os pontos fracos. |
| **2. Conteúdo novo** | 25 min | Um ponto de gramática, sempre em frases de exemplo. Um só, nunca dois. |
| **3. Produção ativa** | 20 min | Escrever 5 frases próprias. Claude corrige com explicação. |
| **4. Fechamento** | 10 min | Registro no diário e **geração dos cartões novos** para o trajeto de amanhã. |

**Regra do dia ruim:** em dia sem tempo ou sem cabeça, o trajeto sozinho já mantém a curva de memória viva. Registre como sessão parcial e siga. O plano de 16 meses morre de semana zerada, não de dia fraco.

---

## Ritmo semanal

| Dia | Trajeto | Mesa |
|---|---|---|
| Seg–Sex | 2h (Anki + áudio) | 1h (os 4 blocos) |
| Sábado | — | Revisão da semana + 30 min de imersão ativa |
| Domingo | — | Quiz da semana + planejamento dos 7 dias |

Sábado e domingo não têm trajeto, então a hora de mesa absorve parte da revisão nesses dias.

---

## O pipeline do Anki

O Anki roda no **celular** (AnkiDroid), e o celular não é acessível daqui. O caminho dos cartões é este:

```
Sessão de mesa  →  progresso/vocabulario.tsv  →  importar no Anki  →  celular
```

**Duas rotas de importação, da mais automática para a mais simples:**

1. **Com Anki desktop como ponte (recomendado se quiser automação real).** Instala-se o Anki no computador uma vez, importa-se o TSV lá, e o AnkiWeb sincroniza para o celular sozinho. O desktop nunca é usado para estudar — é só o cano. Depois disso, cada lote novo é: importar no desktop, clicar em sincronizar, pronto.
2. **Direto no celular.** As versões recentes do AnkiDroid importam CSV/TSV pelo próprio app. Se a sua versão suportar, dá para pular o desktop inteiro — basta transferir o arquivo.

**Para o volume principal, não use nenhuma das duas: baixe um deck pronto.** O **Kaishi 1.5k** tem as 1.500 palavras mais úteis com áudio, frase de exemplo e furigana, e substituiu o antigo Core 2000 como deck padrão de iniciante. Ele é o motor do trajeto; os arquivos que geramos aqui são só o complemento do que aparece nas sessões.

- **Onde baixar:** [github.com/donkuri/kaishi](https://github.com/donkuri/kaishi) → *Releases*. Pelo celular também dá (AnkiDroid → *Obter baralhos compartilhados*), mas o GitHub é mais confiável: no AnkiWeb o deck às vezes fica em revisão e some da busca.
- **Baixado em 12/08/2026**, no dia 10 do plano. Até então o trajeto rodava sem ele, e a medição de 11/08 mostrou por quê isso importava: **48 cartões em 3,87 minutos**. Não era falta de esforço — com 150 cartões de kana não *existem* 90 minutos de revisão devida.

### Quantos cartões novos por dia

A conta que fixa o número (480 dias até 05/12/2027, meta de 3.700 palavras → **7,7/dia** no mínimo):

| novos/dia | em 480 dias | Kaishi acaba | fila em regime | tempo/dia |
|---|---|---|---|---|
| 5 | 2.400 | 300d | 50 | ~11 min |
| **10** | **4.800** | **150d** | **100** | **~22 min** |
| 15 | 7.200 | 100d | 150 | ~32 min |
| 20 | 9.600 | 75d | 200 | ~43 min |

**Fixado em 10/dia.** Cobre a meta com folga e usa 22 dos 120 minutos de trajeto. Subir para 20 não faz chegar mais longe — só antecipa o momento em que a fila fica grande, que é a causa número um de abandono no terceiro mês.

O número definitivo se descobre medindo: rodar 10/dia por duas semanas e olhar a fila de atrasados. Estável → sobe para 15. Crescendo → 10 já era o teto.

⚠️ **Nunca limite o máximo de revisões/dia** (deixe 9999). Limitar não reduz trabalho, **adia**: o cartão que não apareceu hoje volta amanhã somado aos de amanhã, e a fila vira bola de neve enquanto o app mostra um número confortável.

**Formato importa:** o AnkiDroid importa **`.apkg`**, não aceita TSV. Os TSV em `anki/` servem só para o Anki de computador; o que vai para o celular são os `.apkg`.

**Já pronto para importar:** `anki/kana-fase0-completo.apkg` — 150 notas, 300 cartões (cada nota gera dois: reconhecer kana→leitura e produzir leitura→kana), cobrindo hiragana, katakana, dakuten e yōon, com tags por linha (`hira-a`, `hira-ka`, …).

**Como liberar os cartões no ritmo certo.** O deck foi gerado na mesma ordem do currículo, então basta configurar **5 cartões novos por dia** e o Anki entrega a linha certa em cada dia sozinho — あいうえお no dia 1, かきくけこ no dia 2, e assim por diante. Se quiser controle fino, filtre por tag.

**Reimportar não duplica.** O identificador de cada nota é derivado do conteúdo, então importar o arquivo da semana e depois o completo apenas atualiza as notas já existentes.

Para regenerar os decks: `python3 tools/gerar_apkg.py`. Eles não são versionados no git (são artefatos gerados).

---

## Quadro de acompanhamento (Trello)

O board **https://trello.com/b/U4fKmMtx/japones-jlpt** existe para uma coisa que nem o Anki nem os arquivos daqui fazem bem: **ver o cronograma andando**. Ele tem cinco listas:

- **📚 Próximas semanas** — o que vem pela frente
- **🔄 Semana atual** — a semana em curso (arraste para cá na segunda-feira)
- **✅ Concluído** — o que já passou
- **📅 Avisos do JLPT** — onde a rotina automática escreve, e só quando há algo acionável
- **🎧 Áudio (30 min/dia)** — um card por semana, com checklist de 7 dias

### Por que o áudio ganhou lista própria

Nos primeiros 8 dias do plano, o áudio **não aconteceu nenhuma vez**. Ele estava previsto — na tabela do trajeto aqui em cima e numa linha da descrição de cada card de semana — e mesmo assim passou despercebido.

A lição é sobre o formato, não sobre disciplina: **linha de descrição não se cobra, checklist se cobra.** Um item que precisa acontecer todo dia tem que ter uma caixa para marcar, senão ele é lido uma vez na segunda-feira e esquecido.

Gerar ou atualizar a lista: `python3 tools/criar_audio_trello.py <KEY> <TOKEN>`. O script preserva os checks já marcados.

**Áudio não é dívida.** Dia perdido é perdido — não se recupera dobrando a dose depois. A exposição funciona por regularidade, e 30 min/dia por um ano vale muito mais que o mesmo total concentrado em fins de semana.

As 8 semanas da Fase 0 já estão lá, cada card com o dia a dia da mesa, quais tags liberar no Anki, o marco da semana e as armadilhas específicas daquele conteúdo. Arrastar o card para "Concluído" no domingo é o ritual de fechamento da semana.

**Os decks vão anexados nos cards, em `.apkg`.** Cada semana de kana (1 a 4) tem o próprio arquivo com exatamente os cartões daquela semana — 25, 79, 25 e 21 notas, somando as 150 do deck completo. Baixa pelo Trello no próprio celular e importa direto no AnkiDroid: **o computador não entra no caminho**. O card da Semana 1 leva também o `kana-fase0-completo.apkg`, para quem preferir importar tudo de uma vez.

Para regenerar os decks e ressincronizar os anexos (por exemplo, se o currículo mudar): `python3 tools/anexar_decks_trello.py <KEY> <TOKEN>`. Ele regenera os `.apkg`, remove anexos obsoletos e não duplica os que já existem.

---

## Ferramentas

Sistema deliberadamente enxuto. Acumular ferramenta é a forma mais comum de fingir que se está estudando.

| Função | Ferramenta | Custo | Onde |
|---|---|---|---|
| **SRS (essencial)** | AnkiDroid + deck Kaishi 1.5k | Grátis | Celular, trajeto |
| **Silabários** | `anki/kana-fase0.tsv` (gerado aqui) | Grátis | Celular, trajeto |
| **Livro-texto** | Genki I e II | ~R$300 o par | Mesa |
| **Gramática (SRS)** | Bunpro | ~US$5/mês | Opcional, entra na Fase 1 |
| **Audição** | Nihongo con Teppei for Beginners | Grátis | Celular, trajeto |
| **Leitura** | Graded readers do Tadoku | Grátis | Fase 2 em diante |
| **Simulados** | Questões oficiais em jlpt.jp | Grátis | Mesa, cronometrado |

Material em inglês é mais abundante e melhor que em português, e o inglês B2 dá acesso a ele.

---

## Princípios

**1. A fila de revisão manda.** 20 minutos de revisão valem mais que 60 de conteúdo novo sem revisão. O esquecimento é exponencial e o SRS é o único método barato que vence isso.

**2. Áudio desde o primeiro dia.** A audição é a seção que mais reprova autodidata brasileiro no JLPT e a única que não se compensa com mais gramática. Ouvir sem entender, no começo, já é trabalho útil: o ouvido está aprendendo a separar as palavras.

**3. Reconhecer ≠ saber.** Acertar um cartão não é saber a palavra. Por isso a mesa tem produção ativa todo dia: escrever frases próprias força a recuperação real.

**4. Kanji dentro de palavras, nunca soltos.** Decorar 心 = "coração" isolado é quase inútil. Aprender 安心（あんしん）= "tranquilidade" ensina o kanji, a leitura e uma palavra usável de uma vez.

**5. Volume vence perfeição na fase final.** Da Fase 2 em diante, ler e ouvir muito com entendimento parcial rende mais que analisar pouco com entendimento total.

**6. Estudar cansado ainda funciona.** Sessão fraca mantém a curva de memória viva. Só a sessão que não aconteceu é perda total.

## O que evitar

- **Trocar de método a cada dois meses.** O método medíocre seguido por 16 meses vence o método ótimo seguido por 3 semanas.
- **Colecionar recursos.** Mais um app, mais um livro, mais um canal: quase sempre é procrastinação disfarçada de preparação.
- **Aumentar cartões novos com a fila atrasada.** É o erro que mais faz gente abandonar o Anki no terceiro mês.
- **Romaji depois da Fase 0.** Muleta que impede a leitura de virar automática.
- **Maratonar no fim de semana para compensar a semana.** A memória se consolida no intervalo entre sessões, não dentro delas.
