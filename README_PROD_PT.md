# Automação de Logins Simultâneos - Python + Selenium Grid

Automatize múltiplos logins simultâneos e configuráveis na aplicação de teste:  
[https://the-internet.herokuapp.com/login](https://the-internet.herokuapp.com/login)

---

## Principais Funcionalidades

- Entrada configurável: defina o número de logins via CLI, `.env` ou interface gráfica.
- Execução paralela eficiente: threads, Selenium Grid e controle via `.env`.
- Sequenciamento e ordenação de IDs configurável (`SEQUENCE=INCREASING|DECREASING|RANDOM`).
- Artefatos organizados por ID: screenshots e HTML salvos em pastas dedicadas por login.
- Exportação de resultados: JSON, CSV, TXT, screenshots e HTML (para sucesso e falha).
- Pronto para Docker/Docker Compose, uso local ou produção.
- Pronto para auditoria, monitoramento e replicação cross-platform (Windows, Mac, Linux).
- **Mensagens de erro e sistema centralizadas** em:
  - `source/message_errors.py`: erros específicos de módulo.
  - `source/message_system.py`: mensagens de sucesso, status e sistema.
- Facilita tradução, auditoria e manutenção.

---

## Estrutura do Projeto

```
selenium-login-load/
├─ source/
│  ├─ main.py
│  ├─ run_logins.py
│  ├─ login_worker.py
│  ├─ driverconfig.py
│  ├─ gui.py
│  ├─ message_errors.py
│  ├─ message_system.py
├─ results/
│  ├─ results.json
│  ├─ results.csv
│  ├─ report_summary.txt
│  ├─ screenshot/
│  │    ├─ ID-uuid/
│  │        └─ uuid.png
│  ├─ html/
│  │    ├─ ID-uuid/
│  │        └─ uuid.html
├─ .env
├─ requirements.txt
├─ Dockerfile
├─ docker-compose.yml
├─ entrypoint.sh
└─ README_PROD.md
```

---

## Configuração (`.env`)

Exemplo:

```dotenv
# Limites configuráveis para logins simultâneos!
MIN_LOGINS=1      # Mínimo permitido de logins simultâneos.
MAX_LOGINS=1000   # Máximo permitido de logins simultâneos.

# SEQUENCE define o tipo de sequência de IDs de login (INCREASING, DECREASING, RANDOM)
SEQUENCE=RANDOM     # INCREASING, DECREASING, RANDOM

# Número de logins simultâneos (tentativas totais)
CONCURRENT_LOGINS=50

# Máximo de threads/processos concorrentes
MAX_CONCURRENT=10

# Executar navegador em modo headless. Use 'true' para produção.
HEADLESS=true

# Tempo máximo de carregamento de página (segundos)
PAGE_LOAD_TIMEOUT=30

# Tempo máximo de espera de elementos na página (segundos)
ELEMENT_WAIT_TIMEOUT=10

# Usuário de login
LOGIN_USERNAME=tomsmith

# Senha de login
LOGIN_PASSWORD=SuperSecretPassword!

# Pasta principal para salvar resultados
OUTPUT_DIR=./results

# Pasta para screenshots de cada login
OUTPUT_DIR_SCREENSHOT=./results/screenshot

# Pasta para salvar HTML de cada login
OUTPUT_DIR_HTML=./results/html

# Salvar screenshots dos logins (true/false)
SAVE_SCREENSHOTS=true

# Salvar HTML da página após falha no login (true/false)
SAVE_HTML_ON_FAILURE=true

# Exportar resultados em JSON (true/false)
EXPORT_JSON=true

# Exportar resultados em CSV (true/false)
EXPORT_CSV=true

# Modo de execução do Selenium ('local' para máquina local, 'grid' para Selenium Grid)
SELENIUM_MODE=local

# URL do Selenium Hub (usado apenas no modo grid)
SELENIUM_REMOTE_URL=http://selenium-hub:4444/wd/hub

# URL da página de login (aplicação alvo)
TARGET_URL=https://the-internet.herokuapp.com/login

# Fragmento de URL que indica sucesso no login (usado para validação)
TARGET_URL_TO_CHECK=/secure

# Habilitar/desabilitar Selenium Grid (true/false)
USE_GRID=false

# Número de nós Chrome no Grid (usado no docker-compose)
GRID_NODES=3

# Caminho local do ChromeDriver (necessário para execução local no Windows)
CHROMEDRIVER_PATH=C:\WebDriver\bin\chromedriver.exe
```

- Para Docker/Grid: `SELENIUM_MODE=grid`, `USE_GRID=true`
- Para local: `SELENIUM_MODE=local`, `USE_GRID=false` e defina `CHROMEDRIVER_PATH`

### `.env` (execução grid docker)

```dotenv
MIN_LOGINS=1
MAX_LOGINS=1000
SEQUENCE=RANDOM
CONCURRENT_LOGINS=2
MAX_CONCURRENT=10
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
SELENIUM_MODE=grid
SELENIUM_REMOTE_URL=http://selenium-hub:4444/wd/hub
TARGET_URL=https://the-internet.herokuapp.com/login
TARGET_URL_TO_CHECK=/secure
USE_GRID=true
GRID_NODES=3
CHROMEDRIVER_PATH=
```

---

## Como Executar

### 1. Local (Windows, Mac, Linux)

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Baixe o ChromeDriver compatível com sua versão do Chrome:
   - [Google Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing)
   - Windows:
     - 64 bit: [chromedriver-win64.zip](https://storage.googleapis.com/chrome-for-testing-public/140.0.7339.207/win64/chromedriver-win64.zip)
     - 32 bit: [chromedriver-win32.zip](https://storage.googleapis.com/chrome-for-testing-public/140.0.7339.207/win32/chromedriver-win32.zip)
   - Mac:
     - [chromedriver-mac-arm64.zip](https://storage.googleapis.com/chrome-for-testing-public/140.0.7339.207/mac-arm64/chromedriver-mac-arm64.zip)
     - [chromedriver-mac-x64.zip](https://storage.googleapis.com/chrome-for-testing-public/140.0.7339.207/mac-x64/chromedriver-mac-x64.zip)
   - Linux:
     - [chromedriver-linux64.zip](https://storage.googleapis.com/chrome-for-testing-public/140.0.7339.207/linux64/chromedriver-linux64.zip)
   - Mais info: [ChromeDriver Docs](https://developer.chrome.com/docs/chromedriver/downloads?hl=pt)
3. Defina o caminho no `.env`:
   ```dotenv
   CHROMEDRIVER_PATH=C:\WebDriver\bin\chromedriver.exe
   ```
4. Execute:
   ```bash
   python -m source.main -n 10
   ```
   - Ajuste o número de logins conforme desejar.
   - Defina `SEQUENCE` para controlar ordem/IDs exibidos.

### Docker + Selenium Grid (Produção)

1. **Construir contêineres:**
```bash
docker compose build
```

2. **Iniciar o ambiente completo:**
```bash
docker compose up
```
- O aplicativo detecta automaticamente o modo Grid ou Local a partir do seu `.env`:
- Se `SELENIUM_MODE=grid`, ele usa o Selenium Grid.
- Se `SELENIUM_MODE=local`, ele executa localmente.
- Os logs exibirão o **tempo gasto** e o **status** de cada tentativa de login.

3. **Gerar e executar com o script Python:**
```bash
python generate_compose.py
```
- Este script gera automaticamente um `docker-compose.yml` com o número de nós definido em `.env` (`GRID_NODES`), exclui qualquer arquivo anterior e executa `docker compose up --build`.

---


## Resultados Gerados

- `results/results.json` → detalhes de cada login
- `results/results.csv` → exportação CSV
- `results/report_summary.txt` → resumo com tempo total e status de cada login
- `results/screenshot/ID-uuid/uuid.png` → Screenshot (sucesso e falha)
- `results/html/ID-uuid/uuid.html` → HTML (sucesso e falha)

---

## Sequenciamento e Ordenação

- **SEQUENCE=RANDOM**: IDs aleatórios, ordem de chegada.
- **SEQUENCE=INCREASING**: IDs de 1 a N, ordem crescente.
- **SEQUENCE=DECREASING**: IDs de N a 1, ordem decrescente.
- Ordem de exibição e artefatos segue o tipo selecionado.

---

## Escalabilidade & Produção

- Paralelismo configurável via `MAX_CONCURRENT` e `CONCURRENT_LOGINS`
- Grid distribuído para centenas de logins simultâneos
- Pronto para replicação em qualquer SO

---

## Monitoramento & Auditoria

- Logs em container e CLI mostram tempo/status por login
- Artefatos de erro e sucesso salvos por ID
- Relatórios exportados em formatos profissionais
- Auditabilidade e rastreabilidade fácil por ID
- **Mensagens de erro e sistema centralizadas** em:
  - `source/message_errors.py`: erros específicos de módulo.
  - `source/message_system.py`: mensagens de sucesso, status e sistema.
- Facilita tradução, auditoria e manutenção.

---

## ChromeDriver: Windows, Mac, Linux

- Sempre baixe o ChromeDriver **com a mesma versão do seu Chrome**.
- Links oficiais: [Google Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing)
- Defina `CHROMEDRIVER_PATH` no `.env` para execução local.
- Para Grid/Docker, configuração do ChromeDriver é automática.

---

## FAQ

**Como executar com mais ou menos logins?**  
- Edite `CONCURRENT_LOGINS` no `.env` ou use o argumento `-n`.

**Como escalar para centenas de logins?**  
- Ajuste `MAX_CONCURRENT` e `CONCURRENT_LOGINS` no `.env` e aumente Chrome nodes no `docker-compose.yml`.

**Como configurar sequência de IDs e ordem de exibição?**  
- Use `SEQUENCE=INCREASING`, `SEQUENCE=DECREASING`, `SEQUENCE=RANDOM` no `.env`.

**Os artefatos são organizados?**  
- Sim, cada login tem sua própria pasta por ID para screenshot e HTML.

**PySimpleGUI não funciona?**  
- Siga as instruções do README para instalar pelo repositório privado.

---

## Observações

- O código atende 100% dos requisitos do desafio, pronto para produção e auditoria.
- Artefatos e logs garantem rastreabilidade e confiabilidade.
- Replicável em qualquer computador, Windows, Mac, Linux, local ou Grid com Docker.

---

## O QUE O CÓDIGO DEVE FAZER (DESAFIO)

### Funcionalidade do Sistema

1. **Entrada para Número de Logins Simultâneos:**  
   ○ Usuário define número de logins simultâneos via campo de entrada.
2. **Execução dos Múltiplos Logins Simultâneos:**  
   ○ Selenium automatiza logins, cada um com instância isolada de WebDriver.
   ○ Login: tomsmith | Senha: SuperSecretPassword!
3. **Cálculo do Tempo de Execução:**  
   ○ Tempo total para todos os logins exibido ao final.
4. **Validação de Sucesso:**  
   ○ Verifica redirecionamento para página de sucesso e registra status de cada login.
5. **Exibição de Tempo e Status:**  
   ○ Mostra tempo total, status (sucesso/falha) e token único para cada login.

### Etapas de Implementação

1. Interface do Usuário
   - Campo de entrada para número de logins simultâneos.
   - Botão de execução.
2. Execução dos Logins Simultâneos
   - Selenium, WebDrivers independentes, Grid para produção.
3. Cálculo de Tempo e Exibição
   - Tempo total, relatório e artefatos.
4. Validação de Sucesso
   - Redirecionamento validado e exportado.
5. Feedback ao Usuário
   - Status em tempo real, artefatos para auditoria, relatórios claros.

### Pontos de Avaliação

- Processo de login correto: login real e validação do redirecionamento.
- Execução paralela eficiente: múltiplos logins simultâneos, Grid e local.
- Cálculo de tempo preciso: total e individual exibidos.
- Feedback ao usuário: status, artefatos, logs e relatórios claros.
- Deploy & Monitoramento: Docker, Grid, artefatos e replicação em qualquer ambiente.

## PySimpleGUI & Docker

Se for usar a interface gráfica (`--gui`) no Linux/Docker, pode ser necessário instalar dependências extras para o PySimpleGUI funcionar:

```bash
apt-get update && apt-get install -y python3-tk
```

Para Docker, adicione no Dockerfile:

```dockerfile
RUN apt-get update && apt-get install -y python3-tk
```

Se estiver em modo headless, a GUI não funcionará. Prefira CLI (`python -m source.main -n 20`) ou execução via Grid/Docker.

---

## Solução de Problemas

- **Erro "element not found" ou timeout:**  
  Pode ser lentidão de rede ou máquina. O sistema aguarda até 10 segundos (configurável em `ELEMENT_WAIT_TIMEOUT` no `.env`) para cada elemento aparecer.
- **PySimpleGUI não abre em VM/Docker:**  
  Instale `python3-tk` como acima. Ou use CLI.
- **Incompatibilidade Chrome/Chromedriver:**  
  Baixe a versão correta em [Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing) e defina o caminho no `.env`.
