#!/bin/bash
BYellow='\033[1;33m'

python3 -m venv .venv # Cria o ambiente virtual
source .venv/bin/activate # Ativa o ambiente virtual
pip install -r requirements.txt # Instala as dependências
echo -e "${BYellow} Configuração inicial feita."
python3 main.py # Executa o arquivo Python principal