---
title: sistemas
desc: sistemas informais
draft: true
weight: 20
---


# Sistemas

À escolha de determinados símbolos e relações entre eles, damos o nome de _sistema_. Mais precisamente:

(def-2)=
> [Definition 2](#def-2). Um _sistema_ é definido pela escolha das seguintes informações: 
> 1. _símbolos_ :tex x, y, z, ...:
> 2. _relações_ :tex \alpha, \beta, ...:
> 3. _hipóteses_ acerca da existência de símbolos :tex a, b, c, ...: (entre os símbolos :tex x, y, z, ...:  escolhidos) que se relacionam (ou não) através de alguma das relações :tex \alpha, \beta, ...:.

Observe que podem existir muitos símbolos e relações para além daquelas integrantes de um certo sistema. Com efeito, dado um sistema, dizemos que seus símbolos e relações são _internos_ a ele. Os demais símbolos e relações (isto é, não escolhidos para fazerem parte do  sistema) são ditos serem _externos_.

(obs-1)=
> [Observação 1](#obs-1). As "hipóteses" de um sistema poderiam muito bem ser chamadas de _axiomas_. No entanto, guardaremos o nome _axioma_ para quando estivermos tratando de sistemas verdadeiramente formais.

Vejamos alguns exemplos de hipóteses que poderiam ser impostas na definição de um sistema.

# Vacuidade

(example-1)=
> [Example 1](#example-1)(Vacuidade de :tex \alpha:). Existe um símbolo que não se relaciona com nenhum outro símbolo através de uma certa relação :tex \alpha:. 

Em outras palavras, existe um símbolo especial :tex \varnothing_\alpha: dentre os símbolos do sistema tal que :tex \neg \alpha(\varnothing_\alpha, x, y, z ...): para quaisquer que sejam os outros símbolos :tex x, y, z, ...:. Trata-se do _símbolo vazio de :tex \alpha:_. 

Uma condição mais rígida de vacuidade seria a seguinte:

(example-1)=
> [Example 1](#example-2)(Vacuidade). Existe um símbolo que não se relaciona com nenhum outro símbolo através de _qualquer_ relação :tex \alpha, \beta, ...: do sistema.

Se um sistema satisfaz a condição acima, dizemos que possui um _símbolo vazio_ e o denotamos por :tex \varnothing:.

#  
