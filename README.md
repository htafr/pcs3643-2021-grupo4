# PCS3643

## Baseline

A organização das 4 etapas (análise, projeto, implementação e teste) serão realizadas em branchs. Ao final de cada bloco (baseline) vamos dar um merge na main.

[Branch atual](https://github.com/offreitas/pcs3643-2021-grupo4/tree/implementacao)

---

## Instruções para execução do projeto em seu computador local.

Para o funcionamento correto do projeto, será necessário fazer a instalação de algumas bibliotecas:

A instalação pode ser realizada de duas formas:

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

Também é necessário criar um banco de dados ```leilaoOnline``` o qual é acessado com o usuário ```kenji``` e senha ```pcs3643labengsoft``` que está no arquivo ```settings.py```.

No ponto atual da implementação, a criação de novos usuários, sejam eles compradores, vendedores ou leiloeiros, deve ser feita a cada novo pull do projeto. Você terá a oportunidade de fazer um breve teste em cada classe de usuário final da plataforma. As telas dos três tipos mencionados anteriormente são similares, mas com algumas diferenciações (i.e. comprador não deve criar lote). Variações para cada classe serão implementadas posteriormente.

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
