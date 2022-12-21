# FSE (Fundamentos de Sistemas Embarcados)
# Trabalho 1 - 2022/2

[Enunciado do trabalho](https://gitlab.com/fse_fga/trabalhos-2022_2/trabalho-1-2022-2)

## Dados do Aluno

| Nome | Matrícula  |
| :-: | :-: |
| Lorrayne Alves Cardozo | 19/0032863 |

## Dependências

- Python3

## Como Executar
- Primeiramente, é necessário clonar o repositório 
```bash
$ git clone https://github.com/LorrayneCardozo/FSE_T1.git
```

- Em seguida, entrar na raiz do projeto
 ```bash
$ cd src
 ```

 - Rodar na rasp44 (IP 164.41.98.26) o servidor distribuído
 ```bash
$ python3 distribuido_main.py
 ```

 - Rodar na rasp43 (IP 164.41.98.15) o servidor central
 ```bash
$ python3 central_main.py
 ```