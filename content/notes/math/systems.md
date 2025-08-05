---
title: sistemas
desc: sistemas informais
draft: true
---

```{title}
```

# Sobre

Nestas notas, introduziremos os _sistema informais_, os quais serão a base de toda nossa discussão futura.

```{toc}
```

# Conceitos Primitivos 

A Matemática trata da definição, construção e estudo de _conceitos_. Novos conceitos são definidos e novas construções são realizadas partindo-se de conceitos preexistentes. Isso significa que para fazer Matemática são necessários certos conceitos iniciais, os quais se assume existentes _a priori_, e que não são construídos por nenhum outro conceito prévio. Tais conceitos são chamados de _primitivos_.  Tratam-se do ponto de partida para desenvolver nova Matemática.

Diferentes escolas estudam os fundamentos da Matemática de diferentes maneiras, assumindo como primitivos diferentes conceitos. Para nossa discussão futura, é suficiente que assumamos como primitivos conceitos bastante simples, como:

1. algo ser _verdadeiro_ ou ser _falso_;
2. o ato de _contar_;
3. algo ser um _símbolo_;
4. algo ter uma _dependência_ de certos símbolos.

# Afirmações

Para nós, _afirmações_ (também chamadas de _proposições_) são símbolos especiais :tex p, q, ...: os quais se apresentam como _verdadeiros_ ou _falsos_. Isso significa que, para uma afirmação, não há meio termo: ou é uma _verdade_ ou não a é. 

# Símbolos e Relações

Dados símbolos :tex x, y, z, ...:, pensamos em uma _relação_ entre eles como sendo uma _afirmação_ que depende de :tex x, y, z:.

(notation-1)=
> [Notation](#notation-1). Se :tex \varphi: é um relação, escrevemos :tex \varphi(x, y, z, ...): para representar o fato de que os símbolos :tex x, y, z, ...: se relacionam através dela. Isto é, que a afirmação :tex \varphi: é _verdadeira_ para os símbolos :tex x, y, z, ...:.

(obs-1)=
> [Observação 1](#obs-1). Diferentes símbolos podem (ou não) se relacionar através de uma mesma relação. Em outras palavras, uma afirmação :tex \varphi: pode ser verdadeira para certos símbolos, mas falsa para outros. Assim: _relações entre símbolos são independentes de símbolos específicos_.

# Relações :tex n:-árias

Lembre-se que estamos assumindo como primitivo o ato de _contar símbolos_. Isso significa que sentenças como "dados _dois_ símbolos", ou como "dada uma relação entre _três_ símbolos" fazem sentido.

Com a possibilidade de contagem, podemos definir classes particulares de relações:

(def-1)=
> [Definition 1](#def-1). Uma relação :tex \varphi: entre símbolos é dita ser _de grau :tex n:_ (ou _:tex n:-ária_) se ela é uma relação entre precisamente :tex n: símbolos.

Assim, em uma relação de grau :tex n:, as expressões :tex \varphi(x_1, x_2, ..., x_n): ou :tex \neg\varphi(x_1, x_2, ..., x_n): só fazem sentido para dados :tex n: símbolos :tex x_1, x_2, ..., x_n:.

Um caso bastante particular é o das relações de grau 2, também chamadas de _relações binárias_ (ao invés de _2-árias_).

(notation-2)=
> [Notation](#notation-2). Se :tex \varphi: é uma relação binária, costuma-se escrever :tex x\varphi y: ao invés de :tex \varphi(x, y):. Esse tipo de notação é chamada de [notação infixa](https://en.m.wikipedia.org/wiki/Infix_notation).

Tem-se, ainda, as _relações unárias_, que são aquelas de grau 1.

(notation-3)=
> [Notation](#notation-3). Se :tex \varphi: é uma relação unária, escreve-se :tex \varphi x: no lugar de :tex \varphi(x):

(exercise-1)=
> [Exercise 1](#exercise-1). Você consegue imaginar o que seria uma relação 0-ária?

# Conectivos

Uma classe particular de relações são os _conectivos_: tratam-se, pois, de relações não entre símbolos arbitrários, mas entre afirmações.

Assim, em outras palavras:

(def-2)=
> [Definition 2](#def-2). Um _conectivo_ é uma afirmação que depende de outras afirmações.

Todo conectivo é uma relação, de modo que faz sentido falar de _conectivos de grau :tex n:_, que são afirmações que dependem precisamente de outras :tex n: afirmações.

Em especial, podemos falar de _conectivos unários_ (ou de _de grau 1_) e de _conectivos binários_ (ou _de grau 2_).

# Exemplos

Apresentamos, agora, os principais exemplos de conectivos.

(example-1)=
> [Example 1](#example-1)(negação). Tem-se um conectivo unário :tex \neg: chamado de _negação_. A relação :tex \neg p: se caracteriza pelo fato de que se :tex p: é uma afirmação verdadeira (resp. falsa), então :tex \neg p: é uma afirmação falsa (resp. verdadeira).

(obs-2)=
> [Observação 2](#obs-2). Se uma afirmação :tex p: é verdadeira, então sua negação é falsa. Isso significa que para _definir_ uma proposição, basta dizer as condições sob as quais ela é verdadeira. Afinal, as condições para que seja falsa serão as mesmas condições para que seja verdadeira, mas aplicadas à sua negação.   

Outros dois exemplos de conectivos (estes binários) são a _conjunção_ (:tex \wedge:) e a _disjunção_ (:tex \vee:).

(example-3)=
> [Example 3](#example-3)(conjunção). Dadas duas proposições :tex p, q:, a _conjunção_ entre elas é a afirmação :tex p \wedge q: caracterizada pelo fato de ser verdadeira precisamente quando tanto :tex p: quanto :tex q: são verdadeiras.

(example-4)=
> [Example 4](#example-4)(disjunção). Em contrapartida, a _disjunção_ entre :tex p, q: é a afirmação :tex p \vee q: que é verdadeira se ao menos uma afirmação entre :tex p: e :tex q: é verdadeira.


# Condicionais

Um primeiro exemplo de conectivo binário é a _implicação_ (:tex \to:).

(example-2)=
> [Example 2](#example-2)(implicação). Diz-se que uma proposição :tex p: _implica_ outra proposição :tex q: (escrevendo-se :tex p \to q:) se o fato de :tex p: ser  verdadeira (resp. falsa) é suficiente para se concluir que :tex q: é também verdadeira (resp. falsa).

# Quantificadores

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
