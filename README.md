# Speed Click Game

Oi! Bem-vindo ao projeto speedclick. :)

Criei este jogo para sanar a curiosidade sobre os fundamentos da aplicacao dos conceitos de orientacao a objetos no desenvolvimento de jogos, organizando as responsabilidades em classes como `Cell` e `Scoreboard`.

## Como o jogo funciona

- Uma grade de celulas aparece na tela.
- A cada intervalo de tempo, uma celula alvo fica verde.
- Quando voce clica com o botao esquerdo na celula alvo, ganha 1 ponto.
- A pontuacao aparece no canto superior esquerdo (`Score`).

## Como rodar

No diretorio do projeto, execute:

```bash
python main.py
```

## Como aumentar ou diminuir a tela

No arquivo `main.py`, ajuste as constantes:

```python
WIDTH, HEIGHT = 1200, 800
```

- Aumente `WIDTH` para deixar a janela mais larga.
- Diminua `WIDTH` para deixar a janela mais estreita.

## Como aumentar ou diminuir a quantidade de celulas

Tambem em `main.py`, ajuste:

```python
ROWS, COLS = 8, 12
```

- `ROWS`: quantidade de linhas.
- `COLS`: quantidade de colunas.

Exemplos:

- Mais celulas: `ROWS, COLS = 10, 16`
- Menos celulas: `ROWS, COLS = 6, 8`

Se quiser manter uma boa visualizacao ao mudar muito a grade, ajuste tambem:

```python
CELL_SIZE = 80
MARGIN = 2
```

- Diminua `CELL_SIZE` se a grade ficar grande demais para a janela.
- Aumente `CELL_SIZE` se houver espaco sobrando e voce quiser celulas maiores.

## Estrutura orientada a objetos

- `entities/cell.py`: classe `Cell` (desenho, estado e interacao de cada celula).
- `entities/scoreboard.py`: classe `Scoreboard` (controle e exibicao da pontuacao).
- `main.py`: loop principal do jogo, eventos e gerenciamento da grade.

Divirta-se testando e evoluindo o projeto! Se quiser, o proximo passo natural e adicionar niveis de dificuldade (ex.: diminuir o intervalo do alvo com o tempo).
