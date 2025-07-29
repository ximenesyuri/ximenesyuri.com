---
title: sistemas
desc: informais  
---

```{title}
```

# Sobre

Nestas notas, introduziremos o conceito de _sistema informal_, o qual será a base de toda nossa discussão futura.

```{toc}
```

# Símbolos e Relações

No que segue, assumiremos como primitivos os conceitos de _símbolos_ e de _relações_ (também chamadas de _predicados_ ou de _fórmulas_) entre eles. Isso significa que tais conceitos não serão formalmente definidos: eles serão nosso ponto de partida.

Dados símbolos :tex x, y, z, ...:, pensamos em uma _relação_ entre eles como sendo uma _afirmação_ a respeito deles, a qual pode ser verdadeira ou falsa. Se :tex \varphi: é um relação, escrevemos :tex \varphi(x, y, z, ...): para representar o fato de que os símbolos :tex x, y, z, ...: se relacionam através dela. Isto é, que a afirmação :tex \varphi: é _verdadeira_ ou _falsa_ para os símbolos :tex x, y, z, ...:.

(obs-1)=
> [Observação 1](#obs-1). Diferentes símbolos podem (ou não) se relacionar através de uma mesma relação. Em outras palavras, uma afirmação :tex \varphi: pode ser verdadeira para certos símbolos, mas falsa para outros. Assim: _relações entre símbolos são independentes de símbolos específicos_.

Acima guardamos uma notação especial para o caso em que símbolos se relacionam através de uma dada relação: :tex\varphi(x, y, z, ...):. Precisamos, também, de uma notação para dizer quando a relação _não_ é satisfeita, isto é, quando a afirmação obtida é _falsa_.

(notation-1)=
> [Notation](#notation-1). Se os símbolos :tex x, y, z: _não_ se relacionam através de uma determinada relação :tex \varphi:, escrevemos :tex \neg\varphi(x, y, z, ...):.

# Relações :tex n:-árias

Por hora, vamos assumir como primitivo também o processo de _contar símbolos_. Isso significa que afirmações como "dados _dois_ símbolos", ou como "dada uma relação entre _três_ símbolos" fazem sentido.

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

Exemplos de hipóteses que poderiam ser impostas na definição de um sistema são as seguintes:

(example-1)=
> [Example 1](#example-1)(Vacuidade de :tex \alpha:). Existe um símbolo que não se relaciona com nenhum outro símbolo através de uma certa relação :tex \alpha:. 

Em outras palavras, existe um símbolo especial :tex \emptyset_\alpha: dentre os símbolos do sistema tal que :tex \neg \alpha(\emptyset_\alpha, x, y, z ...): para quaisquer que sejam os outros símbolos :tex x, y, z, ...:. Podemos chamar tal símbolo de _símbolo vazio de :tex \alpha:_. 

Uma condição mais rígida de vacuidade seria a seguinte:

(example-1)=
> [Example 1](#example-2)(Vacuidade). Existe um símbolo que não se relaciona com nenhum outro símbolo através de _qualquer_ relação :tex \alpha, \beta, ...: do sistema.

Se um sistema satisfaz a condição acima, dizemos que possui um _símbolo vazio_ e o denotamos por :tex \emptyset:.
