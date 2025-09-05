---
title: logic
weight: 10
---

# Sobre

Aqui você encontrará um glossário com definições de termos ligados à Lógica Matemática.

```{toc-hor}
```

# A

(afirmacao)= 
> [Afirmação](#afirmacao) (Lógica).
>
> Uma _afirmação_ é sinônimo para uma {logic:proposição lógica}.

(alfabeto)= 
> [Alfabeto](#alfabeto) (Lógica).
> 
> Um _alfabeto_ é uma entidade que contém os {logic:símbolos} definidores de uma {logic:linguagem formal}. 


# C

(concatenacao)=
> [Concatenação](#concatenacao) (Lógica).
> 
> _Concatenação_ é a {logic:operação} básica entre {logic:strings}, a qual recebe duas {logic:sequências} finitas de {logic:símbolos}, digamos :tex x_1x_2...x_n: e :tex y_1y_2y_m:, e retorna a correspondente {logic:sequência} finita :tex x_1x_2...x_ny_1y_2...y_m: obtida colocando-se uma após a outra. 

(conceito-primitivo)=
> [Conceito Primitivo](#conceito-primitivo) (Lógica).
>
> Um _conceito primitivo_ é aquele que é assumido como dado _à priori_: isto é, que não é definido a partir de outros {general:conceitos}, e a partir dos quais se define {general:conceitos} que não são primitivos.

(conjunto)=
> [Conjunto](#conjunto) (Lógica).
> 
> Um _conjunto_  é uma {general:entidade} composta de outras {general:entidades}, chamadas de {logic:elementos} do {logic:conjunto} em questão. Podem ser formalmente {logic:definidos} dentro de uma {logic:teoria formal} ou assumidos como {logic:conceitos primitivos}. 

(constante)=
> [Constante](#constante) (Lógica).
> 
> _Constantes_ são símbolos específicos do {logic:alfabeto} de uma {logic:linguagem formal}, distintos de {logic:variáveis}, os quais não aparecem dentro de {logic:relações lógicas} ou {logic:símbolos funcionais}, e cujo {logic:valor} não depende de um dado {logic:contexto}. Podem também ser vistas como {logic:relações} de {logic:aridade} zero.

# D

(delimitador)=
> [Delimitador](#delimitador) (Lógica).
> 
> _Delimitadores_ são {logic:símbolos} dentro do {logic:alfabeto} de uma {logic:linguagem formal}, normalmente representados por parênteses ou colchetes, os quais são utilizados para explicitar o {logic:ordenamento} de {logic:operações} dentro de uma {logic:fórmula}. Também são utilizados entre {logic:variáveis} para dizer que estão sendo sujeitas à ação da {logic:relação lógica} ou do {logic:símbolo funcional} que os precede.

# L

(linguagem-formal)= 
> [Linguagem Formal](#linguagem-formal) (Lógica).
> 
> Uma _linguagem formal_ é um {logic:par ordenado} :tex L = (A, V(A)): formado por um {logic:alfabeto} :tex A: e um {logic:conjunto} de {logic:strings} :tex V(A): do dado {logic:alfabeto}, chamado de {logic:vocabulário} da {logic:linguagem formal} em questão.

# N

(notacao-funcional)= 
> [Notação Funcional](#notacao-funcional) (Lógica).
> 
> Notação _funcional_ é aquela que faz uso de parênteses como {logic:delimitadores lógicos} para representar a dependência de um {logic:símbolo} (digamos :tex f:) com respeito a outros {logic:símbolos}: :tex f(x, y, z):.

(notacao-infixa)=
> [Notação Infixa](#notacao-infixa) (Lógica).
> 
> Notação _infixa_ é aquela que coloca um {logic:símbolo} (digamos :tex f:) entre outros {logic:símbolos} (digamos :tex x, y:) para representar a dependência do primeiro com respeito aos demais: :tex xfy:.

# O

(ordem-simbolos)=
> [Ordem](#ordem-simbolos) (Lógica).
> 
> Dizemos que {logic:símbolos} :tex x, y, z, ...: então _ordenados_ (ou que possuem uma _ordem_) se, quando trocados de posição (digamos :tex x, z, y, ...:), passam a admitir um significado (isto é, um {logic:valor}) diferente. Em outras palavras, se o significado (ou {logic:valor}) associado aos {logic:símbolos} depende da posição em que foram apresentados.

(operacao)=
> [Operação](#operacao) (Lógica).
> 
> Em Lógica Matemática, _operação_ é um sinônimo para {logic:símbolo funcional}.

(operacao-unaria)=
> [Operação Unária](#operacao-unaria) (Lógica).
> 
> Uma {logic:operação} é dita ser _unária_ se ela depende de apenas uma {logic:variável}.

(operacao-binaria)=
> [Operação Binária](#operacao-binaria) (Lógica).
>
> Uma {logic:operação} _binária_ é aquela que depende de precisamente duas {logic:variáveis}. Assim como ocorre com as {logic:relações binárias}, normalmente se denota uma {logic:operação binária} por meio de {logic:notação infixa}.

# P 

(predicado)=
> [Predicado](#predicado) (Lógica).
> 
> Um _predicado_ é uma {logic:proposição} que "depende" de (isto é, cujo {logic:valor} varia relativamente a) outro {logic:símbolo}. Pensamos num {logic:predicado} como sendo uma {general:propriedade} de um {general:indivíduo}, ou mesmo como uma {logic:relação unária}.

(proposicao)= 
> [Proposição](#proposicao) (Lógica).
>
> Uma _proposição_ (também chamada de {logic:afirmação}) é um {logic:símbolo} ao qual está associado um entre possíveis {logic:valores} {logic:constantes}.

# R

(relacao)= 
> [Relação](#relacao) (Lógica).
>
> Uma _relação_ é um {logic:símbolo} que _depende_ de outros {logic:símbolos}, chamados de {logic:variáveis}. Para cada {logic:relação} está associado um número não negativo, chamado de {logic:aridade}: trata-se do número de {logic:símbolos} ao qual a {logic:relação} depende. Relações são normalmente denotadas por letras gregas, como :tex \alpha, \beta, \varphi:. 
> 
> O fato de que {logic:variáveis} :tex x, y, z: se relacionam através de uma dada {logic:relação} :tex \varphi: é normalmente denotado via {logic:notação funcional} :tex \varphi(x, y, z, ...):

(relacao-unaria)= 
> [Relação Unária](#relacao-unaria) (Lógica).
>
> Uma  {logic:relação} é dita ser _unária_ se ela depende de apenas uma {logic:variável}. Ao aturem, {logic:relações unárias} são normalmente denotadas sem o uso de {logic:delimitadores lógicos}: escreve-se :tex \varphi x: ou :tex x \varphi:.

(relacao-binaria)=
> [Relação Binária](#relacao-binaria) (Lógica).
> 
> Uma {logic:relação} é dita ser _binária_ se ela depende precisamente de duas {logic:variáveis}. Normalmente, a atuação de uma {logic:relação binária} é apresentada em {logic:notação infixa}: :tex x \varphi y:.

# S

(sequencia)=
> [Sequência](#sequencia) (Lógica).
> 
> Uma _sequência_ é uma lista {logic:ordenada} de {logic:símbolos}.

(simbolo)= 
> [Símbolo](#simbolo) (Lógica).
> 
> Um _símbolo_ é um elemento do {logic:alfabeto} de uma {logic:linguagem formal}.

(simbolo-funcional)= 
> [Símbolo Funcional](#simbolo-funcional) (Lógica).
> 
> Um _símbolo funcional_ é uma classe particular de {logic:símbolos} dentro do {logic:alfabeto} de uma {logic:linguagem formal} a qual, ao lado das {logic:relações lógicas}, depende de {logic:variáveis}. No entanto, diferentemente das {logic:relações lógicas}, os {logic:símbolos funcionais} retornam 

(string)= 
> [String](#string) (Lógica).
> 
> Uma _string_ (também chamada de _palavra_) é uma {logic:sequência} finita de {logic:símbolos} dentro do {logic:alfabeto} de uma {logic:linguagem formal}. Entre {logic:strings} há a {logic:operação} básica de {logic:concatenação}.


# T

(teoria-ingenua)=
> [Teoria Ingênua](#teoria-ingenua) (Lógica).
> 
> Uma {general:teoria} é dita ser _ingênua_ se seus {general:objetos de estudo} são {logic:conceitos primitivos}. 


# V

(valor-simbolo)=
> [Valor](#valor-simbolo) (Lógica).
> 
> O _valor_ de um {logic:símbolo} é o significado associado a ele, o qual pode (ou não) depender de um {logic:contexto}.


(variavel)=
> [Variável](#variavel) (Lógica).
> 
> Uma _variável_ é um {logic:símbolo} dentro do {logic:alfabeto} de uma {logic:linguagem formal}, o qual é distinto de uma {logic:constante}, e que tipicamente aparece entre {logic:delimitadores lógicos} de {logic:relações lógicas} ou {logic:símbolos funcionais}, ao qual está associado um {logic:valor} que depende do {logic:contexto} no qual está inserido.
