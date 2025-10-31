# 🖨️ SPrinter — Looker Screenshot Automator

**SPrinter** é uma aplicação em **Python** desenvolvida para capturar automaticamente **screenshots de dashboards e relatórios no Looker**.  
Ela utiliza **Selenium WebDriver** para automatizar o acesso, login e geração de imagens, permitindo documentar e compartilhar visualizações do Looker de forma rápida e consistente.

---

## 🚀 Funcionalidades

- 🔐 **Login automático** no Looker com credenciais configuráveis  
- 🖼️ **Captura de telas completas** ou seções específicas de dashboards  
- 📁 **Salvamento automático** das imagens em pastas organizadas  
- 🕒 **Execução agendada** (via script, cron ou Task Scheduler)  
- ⚙️ **Configuração simples** via arquivo `.env`  
- 🧩 **Suporte a múltiplos dashboards**  

---

## 🧠 Tecnologias Utilizadas

- **Python 3.12+**  
- **Selenium WebDriver**  
- **Google Chrome / Chromium**  
- **ChromeDriver**  
- **dotenv** (para variáveis de ambiente)  
- **os / pathlib** (para manipulação de diretórios e arquivos)

---

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/SPrinter.git
cd SPrinter
```

Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuração

Crie um arquivo `.env` na raiz do projeto com as variáveis abaixo:

```bash
LOOKER_URL=https://seu-dominio.looker.com
LOOKER_EMAIL=seu_email@empresa.com
LOOKER_PASSWORD=sua_senha
CHROME_DRIVER_PATH=C:/caminho/para/chromedriver.exe
OUTPUT_DIR=./screenshots
```

> 💡 Dica: use um usuário de automação no Looker para evitar bloqueios de autenticação.

---

## ▶️ Como Usar

Execute o script principal:

```bash
python main.py
```

O **SPrinter** irá:
1. Iniciar o Chrome em modo headless  
2. Acessar o Looker  
3. Navegar até o dashboard configurado  
4. Capturar o screenshot  
5. Salvar a imagem na pasta definida (`/prints`)  

---

## 📁 Estrutura do Projeto

```
SPrinter/
├── main.py                 # Script principal
├── utils/
│   ├── driver.py           # Inicialização e configuração do WebDriver
│   ├── helpers.py          # Funções Auxiliares
│   ├── screenshot.py       # Funções de captura de tela
│   └── seatalk_sender.py   # Funções de envio da imagem
├── prints                  
├── .env                    # Variáveis de ambiente
├── .gitignore              # Dependencias que não irão para o github
├── requirements.txt        # Dependências do projeto
└── README.md               # Este arquivo
```

---

## 🧩 Exemplo de Uso Programático

Você também pode importar o SPrinter em outros scripts:

```python
from utils.screenshot import take_fullpage_screenshot

dashboards = [
    "https://seu-dominio.looker.com/dashboards/1",
    "https://seu-dominio.looker.com/dashboards/2",
]

for url in dashboards:
    capture_dashboard(url, output_name=f"dashboard_{url.split('/')[-1]}.png")
```

---

## ⏰ Execução Automática (opcional)

Para agendar capturas periódicas, instale a biblioteca `schedule`:

```bash
pip install schedule
```

E use um script simples:

```python
import schedule
import time
from main import run_sprinter

schedule.every().day.at("08:00").do(run_sprinter)

while True:
    schedule.run_pending()
    time.sleep(60)
```

> 💡 Ideal para relatórios diários ou monitoramento de dashboards.

---

## 🧰 Problemas Comuns

**Erro: `Chrome failed to start: crashed`**  
→ Verifique se o `chromedriver` está compatível com a versão do Google Chrome instalada.  
→ Use `chrome://version` para confirmar.  

**Screenshot cortado ou incompleto**  
→ Aumente o tempo de espera antes da captura (`driver.implicitly_wait(10)`).  

**Erro de login**  
→ Desative autenticação multifator (2FA) ou use uma conta de automação.  

---

## 🤝 Contribuindo

Contribuições são muito bem-vindas!  
Faça um **fork**, crie uma **branch** para sua feature e envie um **pull request**.

---

## 📄 Licença

Este projeto está licenciado sob a **MIT License** — veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 💬 Contato

Desenvolvido por **Carlos Eduardo Salvador**  
📧 [carlos1992.ces@gmail.com](mailto:carlos1992.ces@gmail.com)
