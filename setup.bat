@echo off

echo Criando ambiente virtual...
python -m venv myenv

echo Ativando o ambiente virtual...
call myenv\Scripts\activate.bat

echo Instalando os pacotes necessarios...
pip install jawa

echo Ambiente configurado com sucesso.
