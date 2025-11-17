# 📡 ISS Overhead Notifier

Este script verifica periodicamente se a **Estação Espacial Internacional (ISS)** está passando sobre sua localização durante a **noite**.  
Se ambas as condições forem verdadeiras, ele envia automaticamente um **e-mail de alerta** usando **SMTP**.

## 🚀 Como Funciona

1. Consulta a posição atual da ISS via **API pública**.
2. Verifica o horário de **nascer e pôr do sol** para sua latitude/longitude.
3. A cada **60 segundos**, checa:
   - A ISS está perto de você?
   - Está de noite?
4. Se sim → Envia um e-mail dizendo para olhar para o céu 🌌.

## 🔧 Configuração

Edite no código:

- `MY_EMAIL` → Seu e-mail  
- `MY_PASSWORD` → Sua senha ou app password  
- `MY_LAT` / `MY_LONG` → Sua localização  
- `SMTP` (ex.: `connection = smtplib.SMTP(...)`) → Servidor do seu provedor de e-mail
