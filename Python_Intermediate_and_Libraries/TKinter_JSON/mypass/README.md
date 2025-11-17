# 🔐 Password Manager (Tkinter + JSON)

Um **gerenciador de senhas desktop** simples, feito com **Tkinter**, com funcionalidades de geração de senhas, pesquisa e armazenamento de dados em **JSON**.

## 🚀 Funcionalidades

### ✔️ Gerar Senhas Seguras
- Mistura aleatória de letras, números e símbolos.
- Copia automaticamente para a área de transferência usando **pyperclip**.

### ✔️ Salvar Credenciais
- Armazena **website**, **email** e **senha** no arquivo `data.json`.
- Atualiza automaticamente os dados existentes no JSON.
- Valida campos vazios antes de salvar.

### ✔️ Buscar Senhas Salvas
- Localiza rapidamente credenciais pelo **nome do site**.
- Mostra **email** e **senha** em um popup.
- Trata casos de site inexistente ou arquivo ausente de forma elegante.

## 🧰 Tecnologias Utilizadas
- **Tkinter** → Interface gráfica (GUI)  
- **JSON** → Armazenamento persistente de dados  
- **pyperclip** → Suporte à área de transferência  
- **random** → Geração de senhas  

## ▶️ Como Rodar
```bash
pip install pyperclip
python main.py
