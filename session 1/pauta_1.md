# Pauta ayudantía 1

*Algoritmos y complejidad.*

*Diego Quezada; diego.quezadac@sansano.usm.cl*

*Kevin Lagos; kevin.lagos@sansano.usm.cl*

*9 de Septiembre, 2020.*

### Ejemplos

Acote superiormente las siguientes funciones definidas con dominio $\N$ utilizando la notación $O(g(n))$:

- $f(n) = 10^{80}$ 

$$
f(n) = O(10^{80}) = O(1)
$$

- $f(n) = (20 \cdot n)^7$

$$
f(n) = O(20^{7}n^7) = O(n^7)
$$

- $f(n) = log(n^{100})$
  $$
  f(n) = O(log (n^{100}) = O(100\cdot log(n)) = O(log(n))
  $$
  
- $f(n) = n^2 + 2n$

$$
f(n) = O(n^2 + 2n) = O(n^2(1 + \frac{2}{n})) = O(n^2)
$$

- $f(n) = \sqrt{n + 1}$

$$
f(n) = O(\sqrt{n+1})= O(\sqrt{n(1 + \frac{1}{n})}) = O(\sqrt{n}\sqrt{1 + \frac{1}{n}}) = O(\sqrt{n})
$$



- $f(n) = log(n)$

  Podríamos intentar con $g(n) = n$:

$$
\lim \limits_{n \rightarrow \infty} \frac{log(n)}{n} = \lim \limits_{n \rightarrow \infty} \frac{1}{n} = 0
$$

​		Efectivamente $log(n) = O(n)$. De hecho, podríamos ser más precisos e indicar $log(n) = o(n)$ pues el 		límite es 0.

- $f(n) = sin(n)$

  Sabemos que $-1 \leq sin(n) \leq 1$. Esto lo podemos traducir directamente como $sin(n) = O(1)$

### Ejercicios

Encuentre cotas superiores ajustadas para:

- $f(n) = log(log(n^n))$

$$
f(n) = O(log(log(n^n))) =  O(log(n \cdot log(n))) = O(log(n) + log(log(n))) = O(log(n))
$$

- $f(n) = \sum \limits_{k=1}^n k^2$
  
  Usando la querida fórmula de la sumatoria de cuadrados:
  $$
  f(n)  = \frac{n(n+1)(2n + 1)}{6} = \frac{(n^2 + n)(2n +  1)}{6} = \frac{2n^3 + 3n^2  + n}{6} = \frac{2n^3}{6} + \frac{3n^2}{6} + \frac{n}{6} = O(n^3)
  $$
  Alternativamente, podríamos utilizar la técnica de multiplicar $n$ por el mayor término que estamos sumando. En este caso obtenemos $O(n \cdot n^2) = O(n^3)$ directamente.
  
- $f(n) = \sum \limits_{k = 1}^n \sqrt{log \space k}$

  Podríamos usar nuevamente la técnica de multiplicar $n$ por el mayor término que estamos sumando, en este caso el mayor término será $\sqrt{log \space n}$ , pues sabemos que $log(n)$ es creciente. Así podemos concluir  $O(n\sqrt{log \space n})$.

---

- Encuentre cotas ajustadas para $f(x) = x + xsin(x)^2$.

$$
f(x) = O(x + xsin(x)^2) = O(x(1 + sin(x)^2)) = O(x)
$$

​		De hecho, podemos notar que $1 + sin(x)^2$ a lo más será 2, y como mínimo será 1. Así podemos decir 		concluir que $f(x) \leq 2x$ y $f(x) \geq x$ al menos para los valores positivos de $x$.

- Demuestre $log(n^2 + 1) = O(log(n))$. 

$$
\lim \limits_{x \rightarrow \infty} \frac{log(n^2 + 1)}{log(n)} = \lim \limits_{x \rightarrow \infty} \frac{n}{n^2 + 1} = \lim \limits_{x \rightarrow \infty} \frac{1}{n + \frac{1}{n}} = 0
$$

​		Nuevamente, podemos decir $log(n^2 + 1) = o(log(n))$.

- Simplifique $(1 + \frac{1}{x} + O(\frac{1}{x^2}))^2$.

$$
(1 + \frac{1}{x} + O(\frac{1}{x^2})) \cdot (1 + \frac{1}{x} + O(\frac{1}{x^2}))
$$

$$
= 1 + \frac{1}{x} + O(\frac{1}{x^2}) + \frac{1}{x} + \frac{1}{x^2} + O(\frac{1}{x^3}) +  O(\frac{1}{x^2}) +  O(\frac{1}{x^3}) +  O(\frac{1}{x^4}) = 1 + \frac{2}{x} + O(\frac{1}{x^2})
$$

​		Notar que también podríamos concluir $1 + \frac{2}{x} + \frac{1}{x^2} + O(\frac{1}{x^3})$, o $1 + O(\frac{1}{x})$, o bien $O(1)$.  No hay una 		forma más correcta que la otra, todo depende de cuán preciso queremos ser. 

- Determine en qué parte de la fórmula para resolver ecuaciones de segundo grado podrían generarse problemas. Reestructure la ecuación para evitar la pérdida de significancia.

  Para el caso de la resta no hay mayor problema. Para la resta, si $b^2 >>> 4ac$  tendremos que $\sqrt{b^2 - 4ac} \approx \sqrt{b^2} = b$. En este caso estaremos realizando una **peligrosa resta** en el numerador. Debemos multiplicar por el conjugado de la expresión del numerador:

  

$$
x = \frac{-b+ \sqrt{b^2 - 4ac}}{2a} \cdot \frac{b+ \sqrt{b^2 - 4ac}}{b+ \sqrt{b^2 - 4ac}} = \frac{b^2 - b^2 - 4ac}{2a (b+ \sqrt{b^2 - 4ac})} =  \frac{-4ac}{2a(b+ \sqrt{b^2 - 4ac})}
$$

