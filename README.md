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


---

## Aula 8 - 22/10/2021

Fez-se os scripts de testes da [classe Lote](https://github.com/offreitas/pcs3643-2021-grupo4/blob/implementacao/leilaoOnline/apps/leilao_fbv_user/tests/test_models.py) e da [classe Vendedor](https://github.com/offreitas/pcs3643-2021-grupo4/blob/implementacao/leilaoOnline/apps/leilao_fbv/tests/test_models.py). Alteramos a data de abertura da classe Lote para três escolhas do tipo drop down - mês de abertura, dia de abertura e ano de abertura.

---

## Atividade Pós-Aula 8 (WIP) - dias 28 e 29 de outubro de 2021

Serão realizadas atividades complementares para o desenvolvimento do projeto, como a criação de novas classes, desenvolvimentos dos outros casos de usos e ajustes do layout da página.