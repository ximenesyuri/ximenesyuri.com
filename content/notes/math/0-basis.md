---
title: base
desc: 
draft: false
weight: 10
---

<u>version: 1</u>

# Sobre

Nestas notas, introduziremos os conceitos de _proposição_, _predicados_ e _conectivos_ , os quais serão a base de toda nossa discussão futura.

```{toc}
```

# Conceitos Primitivos 

A Matemática trata da definição, construção e estudo de _conceitos_. Novos conceitos são definidos e novas construções são realizadas partindo-se de conceitos preexistentes. Isso significa que para fazer Matemática são necessários certos conceitos iniciais, os quais se assume existentes _a priori_, e que não são construídos por nenhum outro conceito prévio. Tais conceitos são chamados de _primitivos_.  Tratam-se do ponto de partida para desenvolver nova Matemática.

Diferentes escolas estudam os fundamentos da Matemática de diferentes maneiras, assumindo como primitivos diferentes conceitos. Para nossa discussão futura, é suficiente que assumamos como primitivos conceitos bastante intuitivos (mais filosoficamente bastante complexos), como:

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
> [Observação 1](#obs-1). Diferentes símbolos podem (ou não) se relacionar através de uma mesma relação. Em outras palavras, uma afirmação :tex \varphi(x, y, z, ...): pode ser verdadeira para certos símbolos, mas falsa para outros. Assim: _relações entre símbolos são independentes de símbolos específicos_.

# Relações :tex n:-árias

Lembre-se que estamos assumindo como primitivo o ato de _contar símbolos_. Isso significa que sentenças como "dados _dois_ símbolos", ou como "dada uma relação entre _três_ símbolos" fazem sentido.

Com a possibilidade de contagem, podemos definir classes particulares de relações:

(def-1)=
> [Definition 1](#def-1). Uma relação :tex \varphi: entre símbolos é dita ser _de grau :tex n:_ (ou _:tex n:-ária_) se ela é uma relação entre precisamente :tex n: símbolos.

Assim, em uma relação de grau :tex n:, a expressão :tex \varphi(x_1, x_2, ..., x_n): só faz sentido para dados :tex n: símbolos :tex x_1, x_2, ..., x_n:.

Um caso bastante particular é o das relações de grau 2, também chamadas de _relações binárias_ (ao invés de _2-árias_).

(notation-2)=
> [Notation](#notation-2). Se :tex \varphi: é uma relação binária, costuma-se escrever :tex x\varphi y: ao invés de :tex \varphi(x, y):. Esse tipo de notação é chamada de [notação infixa](https://en.m.wikipedia.org/wiki/Infix_notation).

Tem-se, ainda, as _relações unárias_ (também chamadas de _modalidades_), que são aquelas de grau 1.

(notation-3)=
> [Notation](#notation-3). Se :tex \varphi: é uma relação unária, costuma-se escrever :tex \varphi x: ou :tex x \varphi: (a depender da relação) no lugar de :tex \varphi(x):.

(exercise-1)=
> [Exercise 1](#exercise-1). Você consegue imaginar o que seria uma relação 0-ária?

# Conectivos

Uma classe particular de relações são os _conectivos_: tratam-se, pois, de relações que não ocorrem entre símbolos arbitrários, mas sim entre afirmações.

Assim, em outras palavras:

(def-2)=
> [Definition 2](#def-2). Um _conectivo_ é uma afirmação que depende de outras afirmações.

Todo conectivo é uma relação, de modo que faz sentido falar de _conectivos de grau :tex n:_, os quais são afirmações que dependem precisamente de outras :tex n: afirmações.

Em especial, podemos falar de _conectivos unários_ (ou de _de grau 1_) e de _conectivos binários_ (ou _de grau 2_).

# Exemplos

Apresentamos, agora, os principais exemplos de conectivos.

O primeiro exemplo nos permite considerar o _oposto_ (ou _negação_) de uma proposição.

(example-1)=
> [Example 1](#example-1) (negação). Tem-se um conectivo unário :tex \neg: chamado de _negação_. A relação :tex \neg p: se caracteriza pelo fato de que se :tex p: é uma afirmação verdadeira (resp. falsa), então :tex \neg p: é uma afirmação falsa (resp. verdadeira).

(obs-2)=
> [Observação 2](#obs-2). Se uma afirmação :tex p: é verdadeira, então sua negação :tex \neg p: é falsa. Isso significa que para _definir_ uma proposição, basta dizer as condições sob as quais ela é verdadeira. Afinal, as condições para que seja falsa serão as mesmas condições para que seja verdadeira, mas aplicadas à sua negação.   

Outros exemplos de conectivos são a _conjunção_ e a _disjunção_ (denotadas, respectivamente, por :tex \wedge: e :tex \vee:).

(example-2)=
> [Example 2](#example-3) (conjunção). Dadas duas proposições :tex p, q:, a _conjunção_ entre elas é a afirmação :tex p \wedge q: caracterizada pelo fato de ser verdadeira precisamente quando :tex p: e :tex q: são verdadeiras ou quando ambas são falsas.

(example-3)=
> [Example 3](#example-4) (disjunção). Em contrapartida, a _disjunção_ entre :tex p, q: é a afirmação :tex p \vee q: que é verdadeira se ao menos uma afirmação entre :tex p: e :tex q: é verdadeira.

Outro exemplo de conectivo binário é a _implicação_ (:tex \to:).

(example-4)=
> [Example 4](#example-2) (implicação). Diz-se que uma proposição :tex p: _implica_ outra proposição :tex q: (escrevendo-se :tex p \to q:) se o fato de :tex p: ser  verdadeira é suficiente para se concluir que :tex q: é também verdadeira.

Por fim, temos o exemplo da implicação mútua.

(example-5)=
> [Example 5](#example-2) (implicação mútua). Duas proposições :tex p, q: estão relacionadas por _implicação mútua_ (escrevendo-se :tex p \leftrightarrow q:) quando ambas são verdadeiras ou quando ambas são falsas. Em outras palavras, :tex p \leftrightarrow q: é verdadeira (resp. falsa) precisamente quando tanto :tex p: quando :tex q: são verdadeiras (resp. falsas).

# Conectivos Derivados

Podemos definir novos conectivos a partir de conectivos já existentes. Por exemplo, dado o conectivo binário :tex \wedge: e o conectivo unário :tex \neg:, podemos definir dois novos conectivos :tex \neg\wedge: e  :tex \wedge \neg:, tais que:

1. :tex p (\neg\wedge) q: é verdadeiro precisamente quando :tex (\neg p)\wedge q: é verdadeiro
2. :tex p (\wedge \neg) q: é verdadeiro precisamente quando :tex p \wedge (\neg q): é verdadeiro.

(exercise-2)=
> [Exercise 2)](#exercise-2)). Divirta-se definindo novos conectivos derivados.

# Equivalência

Diferentes conectivos podem ser _equivalentes_ entre si.

(def-3)=
> [Definition 3](#def-3). Dois conectivos :tex \alpha: e :tex \beta, ...: são ditos serem _equivalentes_ se:
> 1. possuem o mesmo grau, isto é, são ambos :tex n:-ários para um mesmo :tex n:;
> 2. para quaisquer sejam as proposições :tex p_1, p_2, ..., p_n:, tem-se uma relação de implicação mútua entre :tex \alpha(p_1, p_2, ..., p_n): e :tex \beta(p_1, p_2, ..., p_n):.

(notation-4)=
> [Notation](#notation-4). Se dois conectivos :tex \alpha, \beta: são equivalentes, escreve-se :tex \alpha \equiv \beta:.

Os seguintes exercícios nos ensinam equivalentes formas de mostrar que duas proposição estão relacionadas por implicação mútua.

(exercise-3)=
> [Exercise 3](#exercise-2).
> 1. Convença-se de que, independente de quais forem as proposições :tex p, q:, tem-se uma relação de implicação mútua entre :tex p \to q: e :tex (\neg q) \to (\neg p):.
> 2. Defina um conectivo derivado :tex \to_\neg: que represente :tex(\neg q) \to (\neg p):.
> 3. Conclua que :tex \to: e :tex \to_\neg: são equivalentes.

(exercise-4)=
> [Exercise 4](#exercise-3). Partindo do exercício anterior:
> 1. Mostre que :tex p \leftrightarrow q: se relaciona via implicação mútua com :tex (p \to q)\wedge (\neg p \to \neq q ):.
> 2. Defina um conectivo derivado :tex \to_{\wedge,\neg}: para :tex (p \to q)\wedge (\neg p \to \neq q ):.
> 3. Conclua que :tex \leftrightarrow \equiv \to_{\wedge,\neg}:.

(exercise-5)=
> [Exercise 5](#exercise-5). 
> 1. Mostre que há também uma implicação mútua entre :tex p \leftrightarrow q: e :tex (p \wedge q) \vee ((\neg p) \wedge (\neg q)):.
> 2. Defina um conectivo derivado para :tex (p \wedge q) \vee ((\neg p) \wedge (\neg q)):.
> 3. Conclua que ele é equivalente ao conectivo :tex \leftrightarrow:.
