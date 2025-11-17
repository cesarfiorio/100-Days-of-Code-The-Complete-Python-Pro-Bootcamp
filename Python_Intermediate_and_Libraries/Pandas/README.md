# 🗺️ U.S. States Game

Um jogo educativo simples feito com **Turtle** e **Pandas**.  
O objetivo é adivinhar todos os **50 estados dos EUA**. Cada resposta correta é escrita no mapa.

## 🚀 Como Funciona

1. O programa exibe um mapa em branco dos EUA (`blank_states_img.gif`).
2. O usuário digita o nome dos estados em uma caixa de texto.
3. Se o estado estiver correto, ele aparece no mapa nas coordenadas corretas.
4. Digitar `Exit` encerra o jogo e gera um arquivo chamado `states_to_learn.csv` com todos os estados que o jogador não acertou.

## 📁 Arquivos Utilizados

- `50_states.csv` → Contém o nome de cada estado e suas coordenadas (x, y).
- `blank_states_img.gif` → Imagem de fundo do mapa dos EUA.
- `states_to_learn.csv` → Gerado quando o jogador sai do jogo antes de completar.

## 🧰 Tecnologias

- **Turtle** → Para GUI e renderização do mapa.
- **Pandas** → Para carregar, filtrar dados e gerar arquivos CSV.

