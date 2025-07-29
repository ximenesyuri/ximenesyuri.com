# Conjuntos

Para nós, _conjuntos_ serão símbolos :tex x, y, ...: entre os quais há uma relação binária pré-definida: a de _pertinência_. Tal relação é denotada por :tex\in:. Se :tex x: e :tex y: são conjuntos tais que :tex x \in y:, fala-se que :tex x: é um _elemento_ de :tex y:.

Partindo-se da relação básica de pertinência, pode-se derivar outras relações entre conjuntos, como a de _igualdade_ e a de _continência_. 

(def-1)=
> [Definition 1](#definition-1). Dois conjuntos :tex x: e :tex y: são ditos serem _iguais_ se ambos possuem os mesmos elementos. Neste caso, escreve-se :tex x=y:. 

Dessa forma, :tex x=y: se, para qualquer outro conjunto :tex z:, tem-se que:
1. :tex z\in x: implica :tex z\in y:
2. :tex z\in y: implica :tex z\in x:.

(def-2)=
> [Definition 2](#definition-2). Um conjunto :tex x: é dito _estar contido_ em um conjunto :tex y: se todo elemento de :tex x: é também um elemento de :tex y:. Escreve-se, então, :tex x\sub y:.

Se :tex x\sub y:, fala-se, também, que :tex x: é um _subconjunto_ de :tex y:.

# Compreensão

Ao se estudar conjuntos, normalmente se introduz uma _hipótese_ a qual relaciona _fórmulas_ com a relação básica de _pertinência_. Tal hipótese é conhecida como _hipótese da compreensão_, pois nos ensina como construir conjuntos a partir de uma fórmula.

(hyp-1)=
> [Hypothesis 1](#hyp-1) Para toda fórmula :tex \varphi: existe um conjunto cujos elementos são os conjuntos que se relacionam através :tex \varphi:.

Em outras palavras, existe um conjunto :tex x: tal que:
1. se :tex y\in x:, então :tex \varphi(y): (isto é, se :tex y: é um elemento de :tex x:, então )

