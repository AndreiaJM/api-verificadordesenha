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

## Ferramentas usadas no projeto

- Python 3.11
- Framework Flask 1.1.4
- IDE Pycharm
- pytest
- flask-swagger-ui 3.36.0

## Pré requisitos para rodar o projeto

- Python 3.11
- IDE

## Como executar o projeto localmente

- Clonar o projeto localmente
- Abrir com a IDE Pycharm
- Selecionar a pasta app como diretorio principal: 
```sh 
  clicar com o botão direito na pasta app> Mark Diretory as > Sources Root
```
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
- Selecionar o ambiente virtual para que o pycharm reconheça:
```sh
  Menu > File > Settings > Python Interpreter > Add Interpreter > Existing

  Selecionar o seu ambiente virtual e dar ok
```
- Você tambem pode criar seu ambiente virtual atráves da propria IDE:
```sh
  Menu > File > Settings > Python Interpreter > Add Interpreter > New > Ok > 

```

- Ao executar o comando de ativação você vera o nome do ambiente virtual aparecendo no terminal indicando que esta ativo.

- Agora dentro do ambiente virtual você pode fazer a instalação das dependencias do projeto, **dentro da pasta app** executar do comando: 
```sh
  pip install -r requirements.txt
```
- Agora com as dependencias instaladas podemos rodar o projeto através do comando: 
```sh
  Flask run
```

- Api foi desenvolvida com framework Flask e roda na porta padrão: http://127.0.0.1:5000
- **Rotas**: 

**[POST]  /senha**

```sh
  http://127.0.0.1:5000/senha
```
- A rota /senha Recebe um JSON via body
- **Parametros de entrada:**
  - senha: string

- **Retorno**: 
  - resposta: boolean
  
- Exemplo de entrada:
```sh
  	{
		"senha": "AbTp9!fok"
	}
```
- Caso a senha recebida corresponda ao padrão a API retorna **true**, caso nao retorna **false**


- Exemplo de saída caso a senha corresponda ao padrão:
```sh
  	{
		"resposta": true
	}
```
- Exemplo de saída caso senha não corresponda ao padrão:
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
## Documentação
 
- Apos executar o projeto localmente você tambem consegue acessar a documentação Swagger através da url:  
```sh
  http://127.0.0.1:5000/api/docs/
```