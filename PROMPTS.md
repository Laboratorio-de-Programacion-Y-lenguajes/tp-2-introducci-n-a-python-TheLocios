# Registro de Prompts

En este archivo debés documentar los prompts que usaste con herramientas de IA
(GitHub Copilot, ChatGPT, etc.) durante el desarrollo del TP.

**¿Por qué?** Queremos que aprendas a trabajar con IA de forma reflexiva:
que sepas qué le pediste, qué obtuviste, y si tuviste que corregirlo.

---

## Formato para cada entrada

```
### [Número] - [Módulo]

**Herramienta**: GitHub Copilot / ChatGPT / otra

**Prompt usado**:
> Escribí acá exactamente lo que le pediste a la IA

**Resultado obtenido**:
Describí brevemente qué generó (código, explicación, etc.)

**¿Lo usaste tal cual o lo modificaste?**
Explicá qué cambios hiciste y por qué (o por qué no cambiaste nada).
```

---

## Mis prompts

### 1 - variables.py (Patrón: Receta)

**Herramienta**: gemini

**Prompt usado**:
> actua como tutor de Python 3.13. Dame una receta paso a paso para:
> 1. pedir por consola nombre (str), edad (int) y ciudad (str),
> 2. validar que edad sea un entero,
> 3. devolver un string usando f-strings con el formato: "Soy {nombre}, tengo {edad} años y vivo en {ciudad}."
> No uses librerías externas. Mostrá una función armar_mensaje(nombre, edad, ciudad) con docstring.

**Resultado obtenido**:
Genero el codigo de la función `armar_mensaje` que pide el README, explicando como usar f-strings y validación tipos de datos.

**¿Lo usaste tal cual o lo modificaste?**
Lo modifique. Tuve que integrar esta función nueva al final del archivo `src/variables.py`, el cual ya traia otras 5 funciones (`crear_saludo`, `suma_enteros`, etc.) que tambien complete manual. De esta forma, me asegure de que el modulo pase los tests

---

### 2 - condicionales.py (Patrón: Interacción invertida)

**Herramienta**: Gemini

**Prompt usado**:
> Quiero implementar 4 funciones en Python: clasificar_numero, mayor_de_tres, clasificar_nota y es_bisiesto.
> Antes de escribir el codigo haceme 3 preguntas para confirmar:
> - qué mensajes exactos debo devolver en las notas,
> - como tratar los casos de números iguales en "mayor_de_tres",
> - y cómo es exactamente la regla matemática del año bisiesto.
> Despues de mis respuestas, recién ahí propone el codigo con if/elif/else.
> A su vez hazme una breve descripcion por fuera del codigo explicandome para que sirve cada parte del codigo y los resultados que otorga.

**Resultado obtenido**:
La IA me hizo las tres preguntas correspondientes. Luego de responderle, genero las funciones con la estructura condicional correcta y me agregó una explicación detallada de como funciona el flujo de los `if/elif/else` y la logica de los operadores logicos (`and`, `or`) en el caso del año bisiesto.

**¿Lo usaste tal cual o lo modificaste?**
Lo usé tal cual. La explicación extra me sirvio para ver como son multiples condiciones simultáneas antes de pegar el codigo.

---

### 3 - listas.py (Patrón: Verificador cognitivo)

**Herramienta**: Gemini

**Prompt usado**:
> Estoy resolviendo un ejercicio de listas en Python con estas reglas en mente para 5 funciones:
> 1. `suma_lista`: pienso usar la función nativa sum().
> 2. `filtrar_pares`: pienso usar una comprensión de listas (list comprehension) con n % 2 == 0.
> 3. `invertir_lista`: pienso usar slicing [::-1] para asegurar que se crea una nueva lista y no se modifica la original.
> 4. `eliminar_duplicados`: pienso iterar y agregar a una nueva lista solo si el elemento "not in" la nueva lista.
> 5. `aplanar_lista`: pienso usar un for y el metodo .extend() para unir las sublistas.
> 
> ¿Podes revisar mi lógica como verificador cognitivo?
> 1. Enumera casos borde que deberia testear.
> 2. Decime errores tipicos.
> 3. Propone 3 tests con entradas y salidas esperadas.
> Despues de eso, proponé el codigo final. A su vez hazme una breve descripcion por fuera del codigo explicandome para que sirve cada parte del codigo y los resultados que otorga.

**Resultado obtenido**:
La IA valido mi logica diciendo que las elecciones (como el slicing o el metodo extend) eran las mas eficientes y correctas. Me advirtio sobre casos borde (como recibir listas vacías o listas anidadas de forma irregular). Finalmente me dio el codigo y me explico línea por linea como el slicing crea una copia en memoria y por qué `.extend()` es mejor que `.append()` para aplanar listas.

**¿Lo usaste tal cual o lo modificaste?**
Lo usé tal cual. El analisis de la IA confirmo que mi codigo era correcto y la explicación extra sobre la diferencia entre `append` y `extend` me ayudó a entender mejor las listas.


---

### 4 - diccionarios.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 5 - loops.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 6 - funciones.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 7 - operaciones.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

## Reflexión final

Respondé brevemente (3-5 oraciones):

- ¿Qué aprendiste sobre cómo formular buenos prompts?
- ¿En qué casos la IA fue útil y en cuáles no?
- ¿Qué harías diferente la próxima vez?
