# 📋 Integrantes do grupo

- Wagner Wilson
- Lucas Kalebe
- Isabela Kalebe

## 📱 Automação Mobile - TikTok (Appium + Python)

Este projeto tem como objetivo realizar **testes automatizados mobile** no aplicativo **TikTok**, utilizando **Appium** com **Python** para validação de funcionalidades básicas da aplicação.

## 🛠️ Tecnologias Utilizadas

- Python 3
- Appium
- Appium-Python-Client
- Selenium
- Android Studio (Emulador) ou dispositivo físico Android
- UIAutomator2

## 📋 Pré-requisitos

Antes de executar o projeto, certifique-se de ter instalado:

- Python 3.x
- Node.js
- Appium Server
- Android Studio
- Java JDK
- Git

## 📦 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/wagner2332/Mobile-Automation
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

⚙️ Configuração
Configure o Appium Server

Capabilities utilizados:

	"platformName": "Android",
	"appium:deviceName": "Pixel 6",
	"appium:automationName": "UiAutomator2",
	"appium:ensureWebviewsHavePages": True,
	"appium:nativeWebScreenshot": True,
	"appium:newCommandTimeout": 3600,
	"appium:connectHardwareKeyboard": True

Certifique-se de que o emulador ou dispositivo esteja conectado

▶️ Execução dos Testes
Execute os arquivos de teste:

- AbaMensagem.py
- AbaShop.py
- TrocaAbas.py
- TrocaIdioma.py

✅ Funcionalidades Validadas:

- Troca de Idioma nas configurações do aplicativo
- Acesso a aba de mensagem sem estar conectado a nenhuma conta
- Acesso ao tiktok shop sem estar conectado a nenhuma conta
- Exibição da aba de Seguindo

Verificação da tela inicial

Interações básicas (ex: navegação, elementos visíveis, validações de textos)

🚀 Observações

O projeto é apenas para fins educacionais e de aprendizado

O TikTok é uma aplicação de terceiros, e os testes podem falhar caso a interface seja alterada
