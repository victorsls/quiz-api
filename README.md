## Quiz API

#### Como rodar o projeto localmente:

##### Dependências:
* Docker
* Docker Compose
* Git

~~~shell script
git clone https://github.com/victorsls/quiz-api.git
cd quiz-api
docker-compose up
~~~

Para criar um novo usuário, com o container da api em execução execute:
~~~shell script
docker-compose exec api python manage.py createsuperuser
~~~

O projeto utiliza a biblioteca `drf-yasg` para gerar a documentação automaticamente e também para testar as API's.

Acesse a URL: [http://localhost:8000](http://localhost:8000)

##### Autenticação:
Acesse o endpoint **/token** e adicione o username e password do usuário criado e copie o token de acesso gerado.

**Todos os outros endpoints precisam do token para autenticar.**

#### Popular as tabelas:
Será necessário criar Categorias, Perguntas e Respostas antes de iniciar o Quiz.

Após popular o banco de dados, é possível iniciar um Quiz no endpoint:
**/quiz/start-quiz**

Para responder o Quiz é necessário utilizar o endpoint: **/quiz/answer-quiz**.

#### Consultar o Ranking:
Utilizar o endpoint **/ranking**

#### Executar os testes:
~~~shell script
docker-compose run run_tests
~~~

###### Melhorias:
* Utilizar Celery para processar as respostas do Quiz em background.
* Escrever testes automatizados para as customizações feitas nos Models e Views.
* Utilizar UUID e não ID incremental
