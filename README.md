# Troco Mínimo

## Descrição

Você trabalha em uma loja e precisa dar o troco usando o menor número possível de moedas. As moedas disponíveis são de 1, 5, 10, 25 e 50 centavos.

Dado um valor de troco N, determine o número mínimo de moedas necessárias.

## Entrada

Um único inteiro N (1 ≤ N ≤ 10000) representando o valor do troco em centavos.

## Saída

Um único inteiro representando o número mínimo de moedas necessárias.

## Exemplos

### Exemplo 1
**Entrada:**
```
67
```
**Saída:**
```
4
```
**Explicação:** 50 + 10 + 5 + 1 + 1 = 67 (4 moedas)

### Exemplo 2
**Entrada:**
```
100
```
**Saída:**
```
2
```
**Explicação:** 50 + 50 = 100 (2 moedas)

### Exemplo 3
**Entrada:**
```
13
```
**Saída:**
```
4
```
**Explicação:** 10 + 1 + 1 + 1 = 13 (4 moedas)

## Dica

Use uma abordagem gulosa: sempre escolha a maior moeda possível que não ultrapasse o valor restante. Continue esse processo até o troco ser zero.
