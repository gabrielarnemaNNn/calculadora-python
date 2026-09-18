# 🧮 Calculadora em Python

Calculadora de linha de comando feita em Python puro, sem bibliotecas externas.

## Funcionalidades

- Soma, subtração, multiplicação e divisão
- Potência, raiz quadrada e porcentagem
- Histórico dos cálculos da sessão
- Tratamento de erros (divisão por zero, entradas inválidas, raiz de número negativo)
- Testes automatizados com `unittest`

## Como executar

Requisito: Python 3.9 ou superior.

```bash
git clone https://github.com/SEU-USUARIO/calculadora-python.git
cd calculadora-python
python calculadora.py
```

## Como rodar os testes

```bash
python -m unittest -v
```

## Exemplo de uso

```
========== CALCULADORA ==========
1 - Soma            (+)
...
Escolha uma opção: 4
Primeiro número: 10
Segundo número: 4

Resultado: 10 / 4 = 2.5
```

## Estrutura do projeto

```
calculadora-python/
├── calculadora.py        # código principal
├── test_calculadora.py   # testes
└── README.md
```

## Próximos passos (ideias)

- [ ] Interface gráfica com Tkinter
- [ ] Salvar histórico em arquivo
- [ ] Interpretar expressões completas (ex.: `2 + 3 * 4`)

## Autor

Feito por **SEU NOME** · [LinkedIn](https://linkedin.com/in/seu-perfil)
