---
marp: true
size: 4:3
number: true
paginate: true
theme: default
---
Algoritmos y complejidad :alien:
===
### Ayudantía 1
###### Diego Quezada Campos :smiley:
---
# Temario
### Algoritmos de búsqueda de raíces
- Método de la bisección.
- Iteraciones de punto fijo.
- Método de Newton. :alien:
- Backward y Forward error.

---
# Método de la bisección
#### Implementación en Python

```python
def biseccion(f,a,b,epsilon):
    while( (b-a)/2 > epsilon):
        c = (a + b)/2
        if f(c) == 0: break
        if f(a)*f(c) < 0:
            b = c
        else:
        	a = c
    return (a+b)/2
```
---
# Método de la bisección 
- Luego de $n$ iteraciones, tenemos un intervalo [$a_n$,$b_n$] de longitud $\frac{b-a}{2^n}$.
- El error está acotado: $|x_i - r| < \frac{b-a}{2^{n+1}}$
- Garantiza convergencia lineal con razón 1/2.
 ---
# Recordar
Una solución **es correcta en $p$ posiciones decimales** si el error relativo es menor que $0.5 \cdot 10^{-p}$.

---
# Pregunta salvaje :smile:
¿Cuántas iteraciones se necesitan para obtener una raiz de $f(x) = cos(x) - x$ en [0,1] con 6 posiciones correctas?
### Respuesta
* Acotar error: $\epsilon < \frac{b-a}{2^{n+1}} = \frac{1}{2^{n+1}}$
* Aplicar definición slide anterior: $\frac{1}{2^{n+1}} < \frac{1}{2} \cdot 10^{-6}$
* Despejar $n$: $n > \frac{\ln 10^6}{\ln  2} \approx 19.9$

---

# Iteración punto fijo (IPF)
Dada una función $f(x)$:
- $c$ es un punto fijo de $f(x)$ ssi $f(c) = c$.
- Construiremos $g(x) = x$ a partir de $f(x) = 0$.
- Al encontrar un punto fijo para $g(x)$ se encontrará una raíz para $f(x)$ .

---

# Ejemplo IPF
- Sea $f(x) = x^2$ con puntos fijos $0, 1$ y $-1$. 

- Al iterar con un **initial guess** de $0.9$ tenemos:.
> $f(0.9) = 0.81$
> $f(0.81) \approx 0.656$
> $f(0.0656) \approx 4.3034 \cdot 10^{-3} \dots$
> $f(4.3034 \cdot 10^{-3}) = 1.852 \cdot 10^{-5}$

---
# Iteración punto fijo (IPF) 
- La iteración **puede o no converger** (:cry:), pero si la función es continua y converge a $r$, $r$ es un punto fijo.
- El error en la iteración i-ésima es: $e_i = |r - x_i|$ donde $r$ es el punto fijo de interés.

---
# Convergencia lineal
- Supongamos un método iterativo que cumple: $\lim_{n \rightarrow \infty} \frac{e_{i+1}}{e_i} = S$

- Si $S < 1$, entonces el **método converge linealmente** con razón $S$.

:warning: Esta convergencia es **local**.

---
# Convergencia IPF
Si tenemos:
- $g$ diferenciable continuamente.
- $g(r) = r$.
- S = $|g^\prime (r)| < 1$.

Entonces la IPF converge linealmente con razón $S$ hacia $r$ para estimaciones iniciales **lo suficientemente cerca** de $r$.

---
# Convergencia IPF
- Notar que una IPF puede ser más lenta o más rápida que el método de la bisección dependiendo de si $S$ es mayor a $\frac{1}{2}$.
-  Si $S = 1$ nos quedaremos siempre en el mismo punto :cry:.
---
# Método de Newton
- Es un método basado en la IPF de $g(x) = x - \frac{f(x)}{f^\prime (x)}$.
- La iteración es: $x_{i+1} = x_i - \frac{f(x_i)}{f^\prime(x_i)}$.
- Generalmente **converge más rápido** que bisección e IPF.

---
# Convergencia cuadrática

Sea $e_i$ el error después del paso $i$ de un método iterativo. La iteración es cuadráticamente convergente si:
- $M = \lim_{n\rightarrow \infty}   \frac{e_{i+1}}{e_i^2} < \infty$
 
---

# Convergencia cuadrática Newton
- Sea $f$ dos veces continuamente diferenciable y con $f(r) = 0$. Si $f^\prime(r) \neq 0$, Newton es **local y cuadraticamente convergente** a $r$.
- Para Newton $M = \frac{f^{\prime \prime}(r)}{2f^\prime(r)}$.
- Notar que la convergencia de Newton, al igual que la de IPF, **depende de la función**. Esto no ocurre para la bisección.:warning:

---

# Convergencia lineal Newton
- Si tenemos $f^\prime(r) = 0$, el método de Newton no converge cuadraticamente, sino que **linealmente**.
- Dada una función $f$ continuamente diferenciable $m  + 1$ veces con una raiz $r$ de multiplicidad $m$. Entonces Newton converge localmente a $r$ y se cumple:
$\lim_{i \rightarrow \infty} \frac{e_{i+1}}{e_i} = S = \frac{m-1}{m}$.




---

# Error
## Backward error en Búsqueda de raíces
Suponga una aproximación $x_a$ para el cero $c$ de una función $f(x)$. Tenemos que:
- El backward error es la cantidad que debería cambiar la ecuación $f(x_a)  = 0$ para que se cumpla.
- Viene dado por: $\epsilon_b = |f(x_a) -0| = |f(x_a)|$.
- Graficamente se mide de forma vertical.

---
# Error
## Forward error en Búsqueda de raíces
Suponga una aproximación $x_a$ para el cero $c$ de una función $f(x)$. Tenemos que:
- El forward error es la cantidad que debería cambiar $x_a$ para que sea correcta.
- Viene dado por $|c - x_a|$.
- Graficamente se mide de forma horizontal.

---
# Meme section
![center h:400](./images/meme1.jpg)

---
# Ejercicios
:warning: Work in progress :warning: