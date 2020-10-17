# Pauta ayudantía 3

*Algoritmos y complejidad*

Diego Quezada; diego.quezadac@sansano.usm.cl

Kevin Lagos; kevin.lagos@sansano.usm.cl
<div style="page-break-after: always;"></div>

## Ejercicio 1

Interpole el siguiente conjunto de puntos mediante el Lagrange: $X = \{(1,1), (2, 5), (3, 4)\}$

##### Solución

Primero definamos los polinomios $L_k$:
$$
L_1 = \frac{(x-2)(x-3)}{(1-2)(1-3)} = \frac{1}{2}(x^2 - 5x + 6) \\
L_2 = \frac{(x-1)(x-3)}{(2-1)(2-3)} = - (x^2 - 4x + 3) \\
L_3 = \frac{(x-1)(x-2)}{(3-1)(3-2)} = \frac{1}{2}(x^2 - 3x + 2)
$$
Como sabemos que el polinomio interpolador es $P_{n-1} = \displaystyle \sum_{i=1}^n y_i L_i(x)$, solo nos falta sumar estas cositas:
$$
P_{n-1} = 1 \cdot \frac{1}{2}(x^2 - 5x + 6) - 5 \cdot (x^2 - 4x + 3) + \frac{4}{2}(x^2 - 3x + 2)
$$
Si se juega un poco con la expresión, llegamos al siguiente polinomio:
$$
P_{n-1} = \frac{-5}{2} x^2 + \frac{23}{2}x - 8
$$

<div style="page-break-after: always;"></div>

## Ejercicio 2

Interpole el mismo conjunto de puntos mediante **diferencias divididas**.

##### Solución

Recordar que este semestre no se estudió este método, de todas formas adjunto la pauta.

Primero calculemos los coeficientes del término $x^{n-1}$ de nuestro polinomio interpolador, estos vienen dado por $f[x_1 x_2 \dots x_n]$ :

| $x$  | $f[x_k] = y$ | $f[x_k x_{k+1}]$       | $f[x_k x_{k+1} x_{k+2}]$              |
| ---- | ------------ | ---------------------- | ------------------------------------- |
| 1    | 1            |                        |                                       |
|      |              | $\frac{5-1}{2-1} = 4$  |                                       |
| 2    | 5            |                        | $\frac{-1 - 4}{3 - 1} = \frac{-5}{2}$ |
|      |              | $\frac{4-5}{3-2} = -1$ |                                       |
| 3    | 4            |                        |                                       |

Nuestro polinomio interpolador de grado $3-1$ para las diferencias divididas viene dado por:
$$
P_{2} (x) = f[x_1] + f[x_1 x_2] (x - x_1) + f[x_1 x_2 x_3] (x - x_1) (x - x_2)
$$
Para este caso tenemos:
$$
P(x) = 1 + 4(x-1) - \frac{5}{2}(x-1) (x-2)
$$
Al jugar con la expresión final, obtenemos:
$$
P(x) = \frac{-5}{2}x^2 + \frac{23}{2}x - 8
$$
El mismo polinomio encontrado en 1. Recordar que por el **teorema principal de interpolación polinomial** para un conjunto de $n$ puntos, el polinomio interpolador $P_{n-1}$  de grado a lo más $n -1$ **es único**.

<div style="page-break-after: always;"></div>

## Ejercicio 3

Agregue los puntos $(4,6) \text{ y } (5,2)$ al conjunto $X$  e interpole nuevamente.

##### Solución

Tenemos $X = \{(1,1), (2, 5), (3, 4), (4,6), (5,2)\}$

Primero definamos los polinomios $L_k$:
$$
L_1 = \frac{(x-2)(x-3)(x-4)(x-5)}{(1-2)(1-3)(1-4)(1-5)} = \space \space \space  \frac{1}{24} (x-2)(x-3)(x-4)(x-5)\\
L_2 = \frac{(x-1)(x-3)(x-4)(x-5)}{(2-1)(2-3)(2-4)(2-5)} = -\frac{1}{6} (x-1)(x-3)(x-4)(x-5) \\
L_3 = \frac{(x-1)(x-2)(x-4)(x-5)}{(3-1)(3-2)(3-4)(3-5)} = \space \space \space \frac{1}{4} (x-1)(x-2)(x-4)(x-5)\\
L_4 = \frac{(x-1)(x-2)(x-3)(x-5)}{(4-1)(4-2)(4-3)(4-5)} = -\frac{1}{6} (x-1)(x-2)(x-3)(x-5) \\
L_5 = \frac{(x-1)(x-2)(x-3)(x-4)}{(5-1)(5-2)(5-3)(5-4)} = \space \space \space  \frac{1}{24} (x-1)(x-2)(x-3)(x-4)
$$
Nuestro polinomio viene dado por: 
$$
P_{4} = \sum_{i=1}^5 y_i L_i(x)
$$
Podemos dividir esta sumatoria en dos, digamos $P = Q + R$:
$$
Q = \displaystyle \sum_{i=1}^2 y_i L_i(x) = (x-3)(x-4)(x-5) \cdot (\frac{1}{24}(x-2) - \frac{5}{6} (x-1)) \\ \quad \quad = (x-3)(x-4)(x-5)(-\frac{19}{24}x + \frac{9}{12})
$$
Luego:
$$
R = \sum_{i=3}^5 y_i L_i(x) = (x-1)(x-2)(\frac{4}{4}(x-4)(x-5) - \frac{6}{6}(x-3)(x-5) + \frac{2}{24}(x-3)(x-4)) \\ = (x-1)(x-2)(\frac{1}{12}x^2 - \frac{19}{12}x + 6)  \quad \quad \quad \quad \quad \quad \space \quad \quad \quad \space 
$$
Y ya podemos parar de sufrir. Para verificar su respuesta puede definir $P(x) = Q(x) + R(x)$ en su lenguaje de programación preferido y verificar que $P(x_i) = y_i$ para $i = 1,2,\dots, 5$.

```python
def P(x):
	return (x-3)*(x-4)*(x-5)*((-19/24) * x + (9/12) ) + (x-1)*(x-2)*( (1/12) * x**2 - (19/12) * x + 6)

points = [(1,1), (2,5), (3,4), (4, 6), (5,2)]

for point in points:
    print(P(point[0]))
```

<div style="page-break-after: always;"></div>

## Ejercicio 4

Se quiere interpolar, utilizando puntos de Chebyshev la función $f(x) = e^{2x}$ en el intervalo $[0,r]$, encuentre una cota para el número mínimo de puntos necesarios para que el error sea menor que $\varepsilon$ en dicho intervalo

##### Solución

Contamos con la siguiente cota para el error de nuestra interpolación:
$$
f(x) - P(x) = \frac{(x-x_1)(x-x_2)\cdots(x-x_n)}{n!}f^{(n)}(c)
$$
La estrategia será acotar el producto de diferencias, acotar la derivada n-ésima de $f$ tomando un $c \in [0,r]$ adecuado para luego multiplicar estas dos cotas agregando el $n!$ para obtener la cota pedida.

Al utilizar los puntos de Chebyshev sabemos que tenemos acotado superiormente el producto de diferencias como:
$$
|(x - x_1) \dots (x - x_n)| \leq\frac{(\frac{b-a}{2})^n}{2^{n-1}}
$$
Para este caso la **cota superior del producto de diferencias** será:
$$
\frac{(\frac{b-a}{2})^n}{2^{n-1}} = \frac{(\frac{(r-0)}{2})^n}{2^{n-1}} = \frac{r^n}{2^{2n-1}}
$$
Luego, debemos acotar $(e^{2x})^{(n)}$. Sabemos que la derivada n-ésima de esta función viene dada por:
$$
f^{(n)}(x) = (e^{2x})^{(n)} = 2^n e^{2x}
$$
 Como estamos interesados en una cota para el intervalo $[0,r]$ debemos notar que la expresión recién obtenida es creciente, por lo que obtendra su máximo valor al evaluarla en $r$. Así, la **cota superior para la derivada n-ésima** es $2^n e^{2r}$.

Finalmente, debemos multiplicar estas dos cotas y dividir por $n!$ para obtener la **cota superior del error** $f(x) - P(x)$:
$$
\frac{r^n}{2^{2n-1}} \cdot 2^n e^{2r} \cdot \frac{1}{n!} = \frac{r^n e^{2r}}{n! \cdot 2^{n-1}}
$$
Nos interesa que esto sea menor a un $\varepsilon$, por lo que basta tomar el primer $n$ que cumpla la siguiente restricción para obtener la cota inferior pedida:
$$
\frac{r^n e^{2r}}{n! \cdot 2^{n-1}} < \varepsilon
$$
Notar que también podemos despejar $n$, pero queda una expresión más compleja. 