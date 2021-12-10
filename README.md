# PCS3643

## Baseline

A organização das 4 etapas (análise, projeto, implementação e teste) serão realizadas em branchs. Ao final de cada bloco (baseline) vamos dar um merge na main.

[Branch atual](https://github.com/offreitas/pcs3643-2021-grupo4/tree/implementacao)

---

## Instruções para execução do projeto em seu computador local.

Para o funcionamento correto do projeto, será necessário fazer a instalação de algumas bibliotecas:

As instalações necessárias podem ser realizadas de duas formas:

### **Forma 1**:

- Biblioteca do Framework Django:
```
pip install django
```
- Biblioteca de extensões do Django:
```
pip install django_extensions
```
- Biblioteca de extensões para utilização do MySQL:
```
pip install pymysql
```

### **Forma 2**:

Executar a instalação via arquivo *requirements.txt*. Nesse arquivo existem as três bibliotecas necessárias para execução do projeto. Para fazer a instalação execute:

```
pip install -r requirements.txt
```

### **Banco de Dados:**

O projeto utiliza  sistema de gerenciamento de Banco de dados do MySQL. Você pode utilizar o software de interface de sua preferência. O grupo utiliza a extensão ```DataBase``` do ```VSCode``` no desenvolvimento do projeto.

#### **Configuração do Banco de Dados:**

Para o funcionamento correto, realize a criação do banco de dados com o comando a seguir:

```
CREATE DATABASE leilaoOnline;
```

Também é necessário criar um usuário e senha. Utilize usuário - ```kenji``` - e senha - ```pcs3643labengsoft``` - que também está disponível no arquivo ```settings.py```.

No atual estágio do projeto não é necessário a criação de superusuários.

### **Set up do Projeto**

Antes de executar o projeto, deve-se migrar os aplicativos criados. Portanto execute os seguintes comandos:

```
python3 manage.py makemigrations leilao_fbv
python3 manage.py makemigrations leilao_fbv_user
python3 manage.py migrate
```

### **Execução do Projeto**

Para executar o projeto, o comando a seguir deve ser executado:

```
python3 manage.py runserver
```

### **Funcionalidades**

No estado atual do projeto é possível realizar a criação de 3 tipos de usuários:

- Comprador - pode participar de leilões fazendo lances e competindo em um leilão
- Vendedor - Pode vender objetos anunciando lotes no sistema
- Leiloeiro - Gerencia o sistema e avalia os lotes criados por vendedores

A funcionalidade de cada usuário é exclusiva de sua classe, ou seja, o comprador não pode criar lotes - o vendedor e o leiloeiro não podem dar lances.

Para teste das funcionalidades do sistema, crie ao menos um usuário de cada tipo.

---

## Aula 8 - 22/10/2021

Fez-se os scripts de testes da [classe Lote](https://github.com/offreitas/pcs3643-2021-grupo4/blob/implementacao/leilaoOnline/apps/leilao_fbv_user/tests/test_models.py) e da [classe Vendedor](https://github.com/offreitas/pcs3643-2021-grupo4/blob/implementacao/leilaoOnline/apps/leilao_fbv/tests/test_models.py). Alteramos a data de abertura da classe Lote para três escolhas do tipo drop down - mês de abertura, dia de abertura e ano de abertura.

---

## Atividade Pós-Aula 8 - 29/10/2021

Foram realizadas atividades complementares para o desenvolvimento do projeto, como a criação de novas classes, desenvolvimentos dos outros casos de usos e ajustes do layout da página.

---

## Aula 9 - 05/11/2021

Os testes que foram feitos durante a aula 8 foram refeitos para adequar-se às alterações realizadas durante no dia 29 de outubro. Também foram feitos testes com *Selenium* para as views de classes que temos, no mínimo, parcialmente implementadas.

### Testes com Selenium

- Rodar primeiro ```test_signup_login```, pois eles criarão os usuários que serão utilizados em ```test_vendedor_views``` e ```test_computador_views```.

---

## Aulas 10 e 11  - 12/10/2021 e 19/10/2021

Completou-se os 3 casos de usos presentes no projeto: *Cadastrar Lote*, *Realizar Leilão* e *Gerar Relatório*. Os arquivos de testes para os casos de uso utilizando o *Selenium IDE* estão disponibilizados na pasta raiz deste repositório - arquivos ```.side```. As maiores alterações encontram-se em [models.py](https://github.com/offreitas/pcs3643-2021-grupo4/blob/main/leilaoOnline/apps/leilao_fbv_user/models.py), [views.py](https://github.com/offreitas/pcs3643-2021-grupo4/blob/main/leilaoOnline/apps/leilao_fbv_user/models.py) e [urls.py](https://github.com/offreitas/pcs3643-2021-grupo4/blob/main/leilaoOnline/apps/leilao_fbv_user/urls.py), além das alterações nos templates.
