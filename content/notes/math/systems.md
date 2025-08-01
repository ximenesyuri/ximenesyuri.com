---
title: sistemas
desc: sistemas informais
draft: true
---

```{title}
```

# Sobre

Nestas notas, introduziremos o conceito de _sistema informal_, o qual será a base de toda nossa discussão futura.

```{toc}
```

# Conceitos Primitivos 

A Matemática trata da definição, construção e estudo de _conceitos_. Novos conceitos são definidos e novas construções são realizadas partindo-se de conceitos preexistentes. Isso significa que para fazer Matemática são necessários certos conceitos iniciais, os quais se assume existentes _a priori_, e que não são construídos por nenhum outro conceito prévio. Tais conceitos são chamados de _primitivos_.  Tratam-se do ponto de partida para desenvolver nova Matemática.

Diferentes escolas estudam os fundamentos da Matemática de diferentes maneiras, assumindo como primitivos diferentes conceitos. Para nossa discussão futura, é suficiente que assumamos como primitivos conceitos bastante simples, como:

1. algo ser _verdadeiro_ ou ser _falso_;
2. o ato de _contar_;
3. algo ser um _símbolo_;
4. algo ser uma _relação entre símbolos_.

# Afirmações

(sup-1)=
> [Suposição](#sup-1). Nossa primeira suposição são os conceitos de _símbolo_ e de  ser _verdadeiro_ e ser _falso_.

Uma _afirmação_ (também chamada de _proposição_) é qualquer coisa que se apresenta como _verdadeira_ ou _falsa_. Isso significa que, para uma afirmação, não há meio termo: ou é uma _verdade_ ou não é.


# Símbolos e Relações

(sup-2)=
> [Suposição](#sup-2). A partir deste ponto, é necessário que também assumamos como primitivo o conceito _relações_ (também chamadas de _predicados_ ou de _fórmulas_) entre símbolos.

Dados símbolos :tex x, y, z, ...:, pensamos em uma _relação_ entre eles como sendo uma _afirmação_ a respeito deles, a qual pode ser verdadeira ou falsa. Se :tex \varphi: é um relação, escrevemos :tex \varphi(x, y, z, ...): para representar o fato de que os símbolos :tex x, y, z, ...: se relacionam através dela. Isto é, que a afirmação :tex \varphi: é _verdadeira_ ou _falsa_ para os símbolos :tex x, y, z, ...:.

(obs-1)=
> [Observação 1](#obs-1). Diferentes símbolos podem (ou não) se relacionar através de uma mesma relação. Em outras palavras, uma afirmação :tex \varphi: pode ser verdadeira para certos símbolos, mas falsa para outros. Assim: _relações entre símbolos são independentes de símbolos específicos_.

Acima guardamos uma notação especial para o caso em que símbolos se relacionam através de uma dada relação: :tex\varphi(x, y, z, ...):. Precisamos, também, de uma notação para dizer quando a relação _não_ é satisfeita, isto é, quando a afirmação obtida é _falsa_.

(notation-1)=
> [Notation](#notation-1). Se os símbolos :tex x, y, z: _não_ se relacionam através de uma determinada relação :tex \varphi:, escrevemos :tex \neg\varphi(x, y, z, ...):.

# Relações :tex n:-árias

Por hora, vamos assumir como primitivo, por fim, o processo de _contar símbolos_. Isso significa que afirmações como "dados _dois_ símbolos", ou como "dada uma relação entre _três_ símbolos" fazem sentido.

Com a possibilidade de contagem, podemos definir classes particulares de relações:

(def-1)=
> [Definition 1](#def-1). Uma relação :tex \varphi: entre símbolos é dita ser _de grau :tex n:_ (ou _:tex n:-ária_) se ela é uma relação entre precisamente :tex n: símbolos.

Assim, em uma relação de grau :tex n:, as expressões :tex \varphi(x_1, x_2, ..., x_n): ou :tex \neg\varphi(x_1, x_2, ..., x_n): só fazem sentido para dados :tex n: símbolos :tex x_1, x_2, ..., x_n:.

Um caso bastante particular é o das relações de grau 2, também chamadas de _relações binárias_ (ao invés de _2--árias_).

(notation-2)=
> [Notation](#notation-2). Se :tex \varphi: é uma relação binária, costuma-se escrever :tex x\varphi y: ao invés de :tex \varphi(x, y):. Esse tipo de notação é chamada de [notação infixa](https://en.m.wikipedia.org/wiki/Infix_notation).

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
