# validaCadenasConGramatica

Valida una cadena con base en una gramática independiente del contexto. La gramática es:

$$ L = \{ i (w)^n i (w^I)^{2n} j^2 \} $$

tal que:

- $w$: Iniciales de los apellidos.
- $i$: Todos los dígitos de la matrícula.
- $w^I$: $w$ inversa.
- $j$: Primer nombre.

Si la matrícula es 0123456 y el nombre es Yozedh Jahday Guerrero Ceja, entonces, algunas cadenas válidas son:

- 0123456gc0123456cgcgyozedhyozedh
- 0123456gcgc0123456cgcgcgcgyozedhyozedh
