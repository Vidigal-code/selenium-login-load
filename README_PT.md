# Automação de Logins Simultâneos - Python + Selenium Grid

Automatize múltiplos logins simultâneos configuráveis na aplicação de teste:  
[https://the-internet.herokuapp.com/login](https://the-internet.herokuapp.com/login)

## Exemplo 

<img src="./example/example.png" alt="" width="800"/> 



## Como usar

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

2. Baixe o ChromeDriver compatível com a sua versão do Chrome.
   - Defina o caminho no `.env` (`CHROMEDRIVER_PATH`).

3. Execute:
   ```bash
   python -m source.main -n 5
   ```

## Funcionalidades

- Quantidade de logins concorrentes definida pelo usuário
- Cada login utiliza um WebDriver isolado
- Validação de sucesso/falha
- Resultados exportados para a pasta `results`

## Estrutura de Pastas

```
source/
├─ main.py
├─ system/
│  ├─ login_worker.py
│  ├─ run_logins.py
├─ config/
│  ├─ driverconfig.py
├─ messages/
│  ├─ message_errors.py
│  ├─ message_system.py
requirements.txt
.env
README.md
```

## Configuração

### `.env` (exemplo)

```dotenv
MIN_LOGINS=1
MAX_LOGINS=1000
SEQUENCE=RANDOM
CONCURRENT_LOGINS=5
MAX_CONCURRENT=2
HEADLESS=true
PAGE_LOAD_TIMEOUT=30
ELEMENT_WAIT_TIMEOUT=10
LOGIN_USERNAME=tomsmith
LOGIN_PASSWORD=SuperSecretPassword!
OUTPUT_DIR=./results
OUTPUT_DIR_SCREENSHOT=./results/screenshot
OUTPUT_DIR_HTML=./results/html
SAVE_SCREENSHOTS=true
SAVE_HTML_ON_FAILURE=true
EXPORT_JSON=true
EXPORT_CSV=true
TARGET_URL=https://the-internet.herokuapp.com/login
TARGET_URL_TO_CHECK=/secure
CHROMEDRIVER_PATH=C:\WebDriver\bin\chromedriver.exe
```

## ChromeDriver: Windows, Mac, Linux

- Sempre baixe o ChromeDriver compatível com a sua versão do Chrome!
- [Google Chrome for Testing: Downloads](https://googlechromelabs.github.io/chrome-for-testing)
- Para execução local (Windows, Mac, Linux), configure `CHROMEDRIVER_PATH` no `.env`.
- Para Docker/Grid, a configuração do ChromeDriver é automática.