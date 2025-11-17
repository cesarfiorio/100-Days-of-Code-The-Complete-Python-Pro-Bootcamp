# 🐢 Turtle – Classic Arcade Games Collection

Esta pasta contém **três jogos clássicos estilo arcade** desenvolvidos com a biblioteca **Turtle** do Python.  
Cada projeto é modular, organizado em múltiplos arquivos `.py`, e demonstra **programação orientada a objetos**, **lógica de animação** e **interação guiada por eventos**.

Esses jogos foram criados como parte da minha jornada de aprendizado, evoluindo do Python básico para conceitos intermediários como **classes, instâncias, detecção de colisão, loops temporizados** e comportamento de **GUI com Turtle**.

## 🎮 Projetos Incluídos

### 1️⃣ Pong Game
Uma versão para dois jogadores do clássico jogo Pong.

**Arquivos**
- `main.py` — loop do jogo, configuração da tela, eventos
- `ball.py` — movimento da bola e colisões
- `paddle.py` — objetos das raquetes e controles
- `scoreboard.py` — pontuação e exibição na tela

**Destaques**
- Movimentação da raquete
- Bola quicando e detecção de paredes
- Colisão com raquetes
- Sistema de pontuação
- Estrutura OOP com múltiplas classes

---

### 2️⃣ Snake Game
Um jogo completo da cobrinha com código modular.

**Arquivos**
- `main.py` — loop do jogo e controles de teclado
- `snake.py` — segmentos da cobra e movimentação
- `food.py` — geração de comida e atualização de posição
- `scoreboard.py` — pontuação e mensagens de game over

**Destaques**
- Crescimento da cobra
- Colisão com paredes e consigo mesma
- Geração aleatória de comida
- Movimento suave usando atualizações de tela
- Arquitetura limpa baseada em classes

---

### 3️⃣ Turtle Crossing (Frogger-Style)
Jogo de travessia por níveis, onde o jogador evita carros em movimento.

**Arquivos**
- `main.py` — loop principal e progressão de níveis
- `player.py` — tartaruga controlada pelo jogador
- `car_manager.py` — criação e movimentação dos carros, aumento de dificuldade
- `scoreboard.py` — acompanhamento de níveis e mensagens

**Destaques**
- Aumento de dificuldade por nível
- Vários objetos de carro na tela
- Detecção de colisão com o jogador
- Separação clara das classes: carros, jogador e placar

---

## 🧰 Conceitos Demonstrados
- **Programação Orientada a Objetos (OOP)**
  - Encapsulamento
  - Comportamento de métodos
  - Interação entre instâncias
  - Arquitetura modular
- **Programas baseados em Eventos**
  - Usando listeners de teclado do Turtle: `screen.listen()` e `screen.onkey()`
- **Lógica de Game Loop**
  - Atualização temporizada da tela: `screen.update()` e `time.sleep()`
- **Detecção de Colisões**
  - Pong: Bola ↔ Raquete
  - Snake: Cabeça ↔ Comida / Cobra ↔ Paredes
  - Turtle Crossing: Jogador ↔ Carros
- **Animação e Movimento**
  - Movimentação suave dos sprites
  - Tratamento de limites
  - Spawn aleatório

---

## 🎯 Objetivo da Coleção
Essa coleção de jogos com Turtle foi construída para **praticar e consolidar habilidades** como:
- Design de programas Python modulares
- Construção de aplicações interativas
- Uso de classes em múltiplos arquivos
- Criação de animações com Turtle
- Gerenciamento de estados, colisões e lógica de jogos

Esses projetos são um **passo inicial** para tópicos mais avançados, como frameworks de GUI, motores de jogos e sistemas OOP mais complexos.
