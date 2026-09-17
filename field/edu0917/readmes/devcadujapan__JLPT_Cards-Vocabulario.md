# Estudo de Vocabulário 日本語

Aplicativo de flashcards para estudo de vocabulário da língua japonesa, com
interface gráfica moderna e colorida (PySide6/Qt) e banco de dados SQLite
próprio, que cresce conforme você cadastra novas palavras.

## Funcionalidades

- Cartão de estudo: mostra a palavra em **japonês** (fundo rosa) e, ao
  clicar, revela a **tradução em português** (fundo verde-água), junto com
  a legenda de **leitura em hiragana** do kanji (quando cadastrada).
- Navegação entre palavras: botões "Anterior", "Próxima" e "Embaralhar".
- Cadastro de novas palavras direto pelo programa, através do botão
  **"➕ Adicionar nova palavra"** — a palavra é salva no banco e já fica
  disponível para estudo na hora, sem precisar reiniciar o app.
- Banco de dados independente do código-fonte: pode ser copiado, feito
  backup ou apagado sem tocar em nenhuma linha de código.

## Estrutura do projeto

| Arquivo               | Função                                                              |
|------------------------|----------------------------------------------------------------------|
| `vocab_app.py` / `vocab_app.pyw` | Interface gráfica (janela, cartão, botões, diálogo de cadastro) |
| `banco_dados.py`       | Camada de acesso ao banco de dados SQLite (sem depender da interface) |
| `vocabulario.db`       | Arquivo de dados gerado automaticamente na primeira execução        |

> `vocab_app.pyw` é uma cópia idêntica ao `.py`, mas com a extensão `.pyw`,
> que no Windows abre direto com `pythonw.exe`, sem mostrar a janela preta
> de console — útil para criar atalhos na área de trabalho.

## Requisitos

- Python 3.9 ou superior
- Biblioteca PySide6

Instalação da dependência:

```bash
pip install PySide6
```

## Como executar

```bash
python vocab_app.py
```

No Windows, para abrir sem janela de console, use o `vocab_app.pyw`
(duplo clique, ou através de um atalho — veja a seção abaixo).

## Banco de dados

Na primeira execução, o arquivo `vocabulario.db` é criado automaticamente
na mesma pasta do script, já com algumas palavras de exemplo. Estrutura da
tabela `palavras`:

| Coluna      | Descrição                                              |
|-------------|---------------------------------------------------------|
| `id`        | Identificador único (gerado automaticamente)             |
| `japones`   | Palavra em japonês (kanji, hiragana ou katakana)         |
| `hiragana`  | Leitura em hiragana do kanji (opcional)                  |
| `portugues` | Tradução em português                                    |
| `categoria` | Categoria da palavra (ex: Saudações, Verbos, Animais)    |
| `criado_em` | Data/hora do cadastro                                    |

O banco migra automaticamente arquivos `vocabulario.db` mais antigos que
ainda não tinham a coluna `hiragana`, sem apagar nada que já estava
cadastrado.

Para começar do zero, basta apagar o `vocabulario.db` — um novo será
criado automaticamente na próxima execução.

## Criando um atalho na área de trabalho (Windows)

1. Coloque `vocab_app.pyw` na mesma pasta de `banco_dados.py`.
2. Clique com o botão direito em `vocab_app.pyw` → **Enviar para** →
   **Área de trabalho (criar atalho)**.
3. Se o atalho abrir o VSCode em vez do programa, é porque o Windows
   associou arquivos `.pyw` ao VSCode. Para corrigir: clique com o botão
   direito no `vocab_app.pyw` → **Abrir com** → **Escolher outro
   aplicativo** → selecione `pythonw.exe` → marque **"Sempre usar este
   aplicativo"**.

## Dicas

- Para exibir corretamente os caracteres japoneses com uma fonte mais
  bonita, instale a fonte **Noto Sans CJK JP** no sistema — o programa
  detecta e usa automaticamente se disponível.
