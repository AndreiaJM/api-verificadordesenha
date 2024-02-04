# verificadordesenha

## API Verificadora de senha

A api verifica se a senha enviada esta possui os seguintes parametros:

- Nove ou mais caracteres
- Ao menos 1 numero
- Ao menos uma letra minuscula
- Ao menos uma letra maiuscula
- Ao menos um caracter especial
- Ao menos 1 caracter especial, sendo: !@#$%^&*()-+
- Não possuir caracteres repetidos dentro do conjunto
- Espaços em branco não devem ser considerados como caracter

## Pré requisitos para rodar o projeto

- Python 3.11

## Como executar o projeto

- Clonar o projeto localmente
- Abrir com a IDE de sua preferecia (indicado Pycharm)
- Criar um ambiente virtual para isolar as instalações do projeto através do comando:
```sh 
  python -m venv nome-do-ambiente
```
- Apos a criação do ambiente virtual você precisa ativa-lo através do comando:

- **No Windows:**
```sh
  nome-do-ambiente\Scripts\activate
```
- **No macOS/Linux:**
```sh
  source nome-do-ambiente/bin/activate
```

- Ao executar o comando de ativação você vera o nome do ambiente virtual aparecendo no terminal indicando que esta ativo.

- Agora dentro do ambiente virtual você pode fazer a instalação das dependencias do projeto, **dentro da pasta app** executar do comando: 
```sh
  pip install requirements.txt
```
- Agora com as dependencias instaladas podemos rodar o projeto através do comando: 
```sh
  Flask run
```
## Usuabilidade

- Api foi desenvolvida com framework Flask e roda na porta padrão: http://127.0.0.1:5000
- Rotas: 

**[POST]**
```sh
  http://127.0.0.1:5000/senha
```
- Recebe um JSON via body, exemplo: 
```sh
  	{
		"senha": "AbTp9!fok"
	}
```
- Caso a senha recebida corresponda ao padrão a API retorna **true**, caso nao retorna **false**
- Exemplo de saída caso corresponda ao padrão:
```sh
  	{
		"resposta": true
	}
```
- Exemplo de saída não corresponda ao padrao:
```sh
  	{
		"resposta": false
	}
```
## Para executar os testes unitarios
 
- Dentro da pasta de teste **app>tests** rodar o comando: 
```sh
  pytest
```