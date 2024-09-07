import os
import subprocess
from pathlib import Path
BYellow='\033[1;33m'
BRed='\033[1;31m'

def rename_file(file, newname):
    filepath = Path(file)
    if filepath.exists():
        filepath.rename(newname)
        print(f"{BYellow}{file} foi renomeado.")
    else:
        print(f"{BRed}{file} não existe.")

def delete_file(file):
    first_run = Path(file)
    if first_run.exists():
        first_run.unlink()
        print(f"{BYellow}{file} foi removido.")
    else:
        print(f"{BRed}{file} não existe.")

def check_first_run():
    first_run_file = '.first_run'
    
    # Verifica se o arquivo de "primeira execução" existe
    if not os.path.exists(first_run_file):
        print("Primeira vez que o projeto é iniciado.")
        
        # Executa o script Bash
        try:
            rename_file('example.env', '.env')
            email = input('Digite o email da conta:\n> ')
            senha = input('Agora digite a senha:\n> ')

            with open('.env', 'w') as f:
                f.write(f'EMAIL={email}\nSENHA={senha}')

            subprocess.run(['bash', 'setup.sh'], check=True)
        except subprocess.CalledProcessError as e:
            print(f"{BRed}Erro ao rodar o script: {e}")
            return
        
        # Cria o arquivo para marcar que já rodou
        with open(first_run_file, 'w') as f:
            f.write("Este arquivo indica que o script Bash já foi rodado.")
    else:
        print(f"{BRed}O projeto já foi iniciado anteriormente.")

if __name__ == "__main__":
    check_first_run()
    delete_file('.first_run')
    delete_file('first_run.py')
