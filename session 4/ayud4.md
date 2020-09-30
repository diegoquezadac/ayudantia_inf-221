---
marp: true
size: 4:3
number: true
paginate: true
theme: default
style: |
    img[alt~="center"]{display:block;margin: 0 auto;}

---
Algoritmos y complejidad 
===
![center h:400](./images/trapecio2.png)
### Ayudantía 4
---
# Temario
### Cuadratura
- Regla del rectángulo
- Regla del Trapecio (primer grado)
- Regla de Simpson (segundo grado)
- Cuadratura Gaussiana

---
# Cuadratura
- Dada una función de interés $f(x)$ y un intervalo $[a,b]$, buscamos aproximar $\displaystyle \int_a^b f(x) dx$.

---
# Regla del rectángulo
- Aproximaremos la integral mediante un **número finito de rectángulos**.
- Considere un intervalo $[x_0, x_1, x_2 , \dots, x_n]$ donde $x_0 = a$, $x_n = b$.
- Podemos aproximar la integral mediante:
$$
\int_a^b f(x)dx \approx \sum_{i = 0}^n f(x_i) \cdot (x_{i+1} - x_i)
$$

---
- Es claro que si $x_{i+1} - x_i = \frac{b-a}{n} = h$ tenemos:
$$
\int_a^b f(x)dx \approx h\sum_{i = 0}^n f(x_i) 
$$
- Notar lo simple que sería programar este método.

---
- Si evaluamos en el punto medio del intervalo $x_{i+1} - x_i$ obtendremos generalmente mejores aproximaciones.

$$
\int_a^b f(x)dx \approx h\sum_{i = 0}^{n - 1} f (\frac{x_i + x_{i+1}}{2}) 
$$

![center h:250](./images/rectangulo_medio.png)


---
## Análisis error

### Caso general
- Al expandir $\displaystyle F(x) = \int_{x_i}^x f(t)dt$ mediante Taylor alrededor de $x_i$ se obtiene:
$$
\int_{x_i}^{x_{i+1}} f(x)dx = hf(x_i) + h^2\frac{f^\prime(c)}{2}
$$
- donde $h = x_{i+1} - x_i$ y $c \in [x_i, x_{i+1}]$.
- El error es $\displaystyle h^2 \frac{f^\prime(c)}{2}$, es decir $O(h^2)$ **para cada intervalo**.

---
- Considerando $h = \frac{b-a}{n}$, el error para $n$ intervalos de largo $h$ es $nO(h^2)$. 
- Aplicando **poderosas matemáticas** obtenemos:
$$
nO(h^2) = nO(\frac{(b-a)^2}{n^2}) = O(\frac{n(b-a)^2}{n^2}) \\ \qquad \qquad \quad  \space \space \space = O(\frac{(b-a)^2}{n}) = O((b-a)h) = O(h)
$$

---
### Variación Punto medio
- Evaluando en el punto medio de cada intervalo tenemos:
$$\int_{x_i}^{x_{i+1}} f(x) dx = hf(\frac{x_i + x_{i+1}}{2}) + \frac{1}{24} f^{\prime \prime}(a)h^3 + O(h^4)
$$
- El error es $O(h^3)$ **para cada intervalo**.
- Esto es mejor que el error $O(h^2)$ para el primer caso analizado.

---
# Regla del Trapecio
- Aproximaremos la integral $\displaystyle \int_a^b f(x) dx$ mediante un número finito de trapecios.
- Recordar que el área de un trapecio es $\frac{b_1 + b_2}{2} \cdot h$
  
![center h:180](./images/trapecio.png)

> Podemos ver el trapecio como si estuviera acostado, de forma que $b_1$ y $b_2$ los obtendremos como imágenes de $f$ y $h$ como $x_{i+1} - x_i$.

---
### Deducción
Sea $[x_0, x_1, x_2 , \dots, x_n]$, donde $x_{i+1} - x_i = \frac{b-a}{n} = h$, y $x_0 = a, x_n = b$.

:arrow_right: Para $n = 2$ tenemos:

$$ \int_a^b f(x)dx \approx \frac{h}{2}(f(a)
 + f(x_1)) + \frac{h}{2}(f(x_1) + f(b))
$$

:arrow_right: Para $n = 3$ tenemos:

$$ \int_a^b f(x)dx \approx \frac{h}{2}(f(a)
 + f(x_1)) + \frac{h}{2}(f(x_1) + f(x_2)) + \frac{h}{2}(f(x_2) + f(b))
$$

---
:arrow_right: De forma general: 
$$
\int_a^b f(x) dx \approx \frac{h}{2}(f(a) + 2f(x_1) + 2f(x_2)\dots + 2f(x_{n-1}) + f(b))
$$

:arrow_right: Esto se puede reescribir como:
$$
\int_a^b f(x) dx \approx \frac{h}{2}(f(a) + f(b) + 2\sum_{i = 1}^{n - 1} f(x_i))
$$


---
### Deducción mediante interpolación
- Trabajaremos en un intervalo $[x_0, x_1]$.
- Para aproximar $\displaystyle\int_{x_0}^{x_1} f(x) dx$, primero interpolaremos $f(x)$ mediante un polinomio $P(x)$ de grado 1, y luego integraremos $P(x)$. :thinking:
- ¿Cuál polinomio utilizamos?
$$
P(x) = y_0\frac{x - x_1}{x_0 - x_1} + y_1\frac{x - x_0}{x_1 - x_0}
$$
> Este es el **polinomio interpolador de Lagrange**.

---
- Integrando P$(x)$ obtenemos:
    $$
    \int_{x_0}^{x_1} P(x) dx= y_0 \int_{x_0}^{x_1}\frac{x - x_1}{x_0 - x_1} dx+ y_1 \int_{x_0}^{x_1} \frac{x - x_0}{x_1 - x_0}dx
    $$
    $$
    \qquad \qquad  \quad= y_0 \frac{x_1 - x_0}{2} + y_1 \frac{x_1 - x_0}{2} = \frac{h}{2} \cdot(y_0 + y_1)
    $$

- Notar que llegamos al área del trapecio presentada anteriormente. 


---
### Análisis error
- Al aproximar la integral $\displaystyle \int_a^b f(x)dx$ usando $n$ trapecios tenemos que:

$$E = -\frac{f^{\prime \prime}(c) \cdot (b-a)}{12}h^2$$
- Donde $c$ es un valor en $[a,b]$.
- Notar que es mejor que el método de los rectángulos pues el error es $O(h^2) = O((\frac{b-a}{n})^2) = O(\frac{1}{n^2})$ .
> Nuevamente podemos tomar el valor $c$ que maximiza $f^{\prime \prime}(c)$ y obtener una cota superior para el error.

--- 
### Regla compuesta
Para $n$ subintervalos, y asumiendo $f \in C^2[a,b]$:
$$ \int_a^b f(x)dx = \frac{h}{2} (f(a) + f(b) + 2 \sum_{i = 1}^{n - 1} f(x_i) )- \frac{f^{\prime \prime} (c) (b-a)}{12} h^2$$

Donde $h = \frac{b-a}{n}$ y $c \in [a,b]$.


---
# Regla de Simpson
- Similar a la regla del Trapecio, pero mejor aún.
- El polinomio a interpolar ahora será de **grado 2**  (parábola).
![center h:300](./images/simpson.png)
---
### Deducción mediante interpolación
- Trabajaremos en un intervalo $[x_0, x_1, x_2]$.
- Para aproximar $\displaystyle\int_{x_0}^{x_1} f(x) dx$, primero interpolaremos $f(x)$ mediante un polinomio, y luego integraremos el polinomio. :thinking:
- ¿Cuál polinomio utilizamos?
    $$
    P(x) = y_0\frac{(x - x_1)(x - x_2)}{(x_0 - x_1)(x_0 - x_2)} + y_1\frac{(x - x_0)(x - x_2)}{(x_1 - x_0)(x_1 - x_2)} + y_2\frac{(x - x_0)(x - x_1)}{(x_2 - x_0)(x_2 - x_1)}
    $$

---
Integrando cada término por separado:
$$
\int_{x_0}^{x_2} y_0\frac{(x - x_1)(x - x_2)}{(x_0 - x_1)(x_0 - x_2)} dx = y_0\frac{h}{3}
$$

$$
\int_{x_0}^{x_2} y_1\frac{(x - x_0)(x - x_2)}{(x_1 - x_0)(x_1 - x_2)} dx = y_1\frac{4h}{3}
$$

$$
\int_{x_0}^{x_2} y_2\frac{(x - x_0)(x - x_1)}{(x_2 - x_0)(x_2 - x_1)} dx = y_2\frac{h}{3}
$$
---
Así obtenemos:
$$\int_{x_0}^{x_2} P(x) dx = y_0\frac{h}{3} + y_1\frac{4h}{3} + y_2\frac{h}{3}$$

> Notar que las integrales son simples. Los términos $y_i$ y los denominadores son constantes. 
---
### Análisis error

- Al interpolar sabemos que $f(x) = P(x) + E(x)$.
- $\displaystyle \int_{x_0}^{x_2} E(x) dx = - \frac{h^5}{90} f^{(4)}(c)$.
- $\displaystyle \int_{x_0}^{x_2} f(x) dx = \frac{h}{3}(y_0 + 4y_1 + y_2) - \frac{h^5}{90} f^{(4)}(c)$.
- Donde $c \in [x_0, x_2]$
---
### Regla compuesta
Para $n$ subintervalos, con $n$ par y asumiendo $f \in C^4[a,b]$:

$$\int_a^b f(x) dx = \frac{h}{3}(f(a) + f(b) + 2\sum_{i=1}^{(n/2) - 1} f(x_{2i}) + 4\sum_{i=1}^{n/2} f(x_{2i - 1})) - \frac{(b-a)h^4}{180} f^{(4)}(c)$$

Donde $h =  \frac{b-a}{2}$ y $c \in [a,b]$.

---
# Grado de precisión
- El grado de precisión de un método de integración numérica el grado $k$ o menor del polinomio que se utiliza para integrar.
- Vimos que el error para la regla de trapecio es:
$$
-\frac{f^{\prime \prime} (c) (b-a)}{12} h^2 $$
¿Qué pasa cuando el polinomio es de grado 1 o menor?
* El término $f^{\prime \prime}(c)$ se hace cero y la aproximación es exacta.


---
# Cuadratura Gaussiana 
- Representa un enfoque distinto. 
- La idea es evitar tener tener que tomar tantos puntos para disminuir el error.
- Tomaremos pocos puntos, pero la elección debe ser inteligente.

---
- El objetivo es buscar valores $w_i, x_i$ tal que:
$$\int_{-1}^1 f(x)dx \approx \sum_{i=1}^n w_i \cdot f(x_i)
$$
- No tenemos restricciones sobre $w_i, x_i$, pero nos interesa que esta aproximación sea exacta para polinomios del mayor grado posible.
> No nos interesan las soluciones con $w_i = 0$ o $x_i = 0$.
- Motivación: Si es exacta para polinomio de grados alto, entonces **quizas** sea bastante precisa para funciones que son bien aproximadas por polinomios.

---
- Al aproximar con $n$ puntos de cuadratura el grado de precisión será $2n - 1$.
- Como aproximaremos con polinomios, usaremos $f(x) = x^k$.
- Al usar $n$ puntos de cuadratura deberemos resolver un sistema con $2n$ ecuaciones para encontrar $w_i, x_i$.
- Para $i = 0, \dots, 2n-1$ las ecuaciones serán:

$$ w_1 x_1^i + \cdots + w_n x_n^i = \int_{-1}^1 x^idx
$$

---
- Para cambiar el intervalo de integración usaremos:

$$\int_a^b F(x) dx = \frac{b-a}{2} \int_{-1}^1 F(\frac{b + a + t(b-a)}{2})dt$$

- Los valores $w_i$ cumplen $x_i > 0$.
---
### Análisis error
- El error cometido por esta estrategia viene dado por:

$$ E_n (f) = \int_{-1}^1 f(x)dx - \sum_{i=1}^n w_i \cdot f(x_i) =  e_n \frac{f^{(2n)}(c_n)}{2n!} $$

- Donde: $\displaystyle e_n = \frac{2^{2n + 1} (n!)^4}{(2n + 1) [(2n)!]^4} \approx \frac{\pi}{4^n}$ y $c_n \in [a,b]$.

---
### Ejemplo :smiley:
- Queremos valores $w_1, x_1$ tal que:
$$\int_{-1}^1 f(x)dx \approx w_1 f(x_1)$$
- Como debe ser exacto para polinomios de hasta grado $2n - 1 = 1$ tenemos:

$$ w_1 x_1^0 = \int_{-1}^1 x^0 dx \\ w_1x_1 = \int_{-1}^1 x^1 dx  $$

---
- Esto se resume a:

$$ w_1 = 2\\ w_1x_1 = 0  $$

- Por lo tanto $w_1 = 2$ y $x_1 = 0$.
- Así nuestra aproximación será:
$$\int_{-1}^1 f(x)dx \approx 2 f(0)$$

> Este resultado parece conocido...


---
# Ejercicios
1. Obtenga la expresión para el error de la regla del trapecio en un intervalo $[x_0, x_1]$.
2. Obtenga la regla de cuadratura Gaussiana para el cálculo de $\displaystyle \int_{-1}^1 f(x)dx$ con dos puntos de cuadratura.
3. Solucione con lo obtenido en 2: $\displaystyle \int_{-1}^1 \frac{dx}{3 + x}$.
**Hint**: El valor real es $ln \space 2$.

4. Programe la Regla del Rectángulo, Trapecio y Simpson.

---
# Recomendaciones
1. http://pages.cs.wisc.edu/~amos/412/lecture-notes/
2. https://personales.unican.es/segurajj/quad.pdf.