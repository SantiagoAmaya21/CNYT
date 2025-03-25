# CNYT


# Números Complejos
Los números complejos son una extensión de los números reales y se representan en la forma 𝑎+𝑏𝑖, donde 𝑎 y 𝑏 son números reales e 𝑖 es la unidad imaginaria que satisface la ecuación 𝑖²=−1. Estos números son fundamentales en la computación cuántica.

## Contenido de la Carpeta "NúmerosComplejos"
1. **Libcplx.py**: 
Este archivo contiene una biblioteca en Python con ocho operaciones esenciales para trabajar con números complejos:
* Suma: Realiza la adición de dos números complejos.
* Resta: Calcula la diferencia entre dos números complejos.
* Multiplicación: Multiplica dos números complejos.
* División: Divide un número complejo por otro.
* Módulo: Calcula la magnitud o módulo de un número complejo.
* Conjugado: Determina el conjugado de un número complejo.
* Conversión Polar y Cartesiana: Permite convertir entre las formas polar y cartesiana de un número complejo.
* Fase: Calcula el ángulo de fase de un número complejo.
2. **Testlibcpx.py**:
Este archivo proporciona pruebas unitarias para verificar el funcionamiento correcto de las funciones implementadas en Libcplx.py. Las pruebas aseguran que las operaciones con números complejos se realicen de manera precisa y confiable.

### Instrucciones
Para ejecutar los archivos Python proporcionados en este repositorio, sigue estos pasos: Asegúrate de que los archivos Libcplx.py y Testlibcpx.py estén en el mismo directorio para que el script pueda encontrar todos los recursos necesarios. Abre una terminal o línea de comandos y navega hasta la carpeta donde se encuentran los archivos. Luego, ejecuta el archivo Testlibcplx.py

# TalleresSemanales
Esta carpeta contiene los talleres semanales correspondientes a la materia de CNYT (Ciencias Naturales y Tecnologia). El propósito de estos talleres es proporcionar prácticas para mejorar el manejo de herramientas y conceptos clave en el campo de la computación cuantica.

## Contenido de la Carpeta "TalleresSemanales"
1. **ComplexIntro.ipynb**
Propósito: Practicar funciones básicas y operaciones con números complejos. Este archivo incluye ejercicios para operar y graficar números complejos en un plano complejo.
2. **Complex_Vector_Matrix_Operations_with_NumPy.ipynb**
Propósito: Realizar operaciones sobre matrices y vectores columna utilizando la biblioteca NumPy. Incluye ejercicios para la manipulación y cálculo de matrices y vectores.
3. **TallerEsp.Vect-ProdInterno-VectoPropios**
Propósito: Calcular productos internos, valores propios y vectores propios de matrices.
4. **TallerEsp.Vect-Hermitian-Unitary-Tensor-Circuits**
Propósito: Aplicar los conceptos anteriores en sistemas cuánticos. Incluye ejercicios sobre matrices Hermitianas, operaciones unitarias, y circuitos.

### Instrucciones
1. Configuración del Entorno: Asegúrate de tener un entorno virtual Python 3.12.0 configurado.
Activa el entorno virtual:
- En Windows:
```
.venv\Scripts\activate
```
- En macOS y Linux:
```
source .venv/bin/activate
```
2. Instalación de Dependencias: Una vez activado el entorno virtual, instala las dependencias necesarias usando el siguiente comando:
```
pip install numpy matplotlib ipywidgets
```

# ClassicToQuantum
Los sistemas discretos clásicos se caracterizan por tener un número finito de estados posibles, permitiendo el uso de herramientas estadísticas para predecir resultados. En contraste, el experimento de la doble rendija revela la naturaleza probabilística de las partículas

## Contenido de la Carpeta "ClassicToQuantum"
**TallerClasicToQuantum.ipynb**
Propósito: Implementar sistemas discretos en un problema de doble rendija probabilístico y calcular las probabilidades de cada estado.

### Instrucciones
1. Configuración del Entorno: Asegúrate de tener un entorno virtual Python 3.12.0 configurado.
Activa el entorno virtual:
- En Windows:
```
.venv\Scripts\activate
```
- En macOS y Linux:
```
source .venv/bin/activate
```
2. Instalación de Dependencias: Una vez activado el entorno virtual, instala las dependencias necesarias usando el siguiente comando:
```
pip install numpy matplotlib
```

# Basic Quantum Theory, Observables and Measurements
Los observables son magnitudes físicas que pueden medirse debido a su naturaleza probabilística, definición de estados e interacción con el entorno.

## Contenido de la Carpeta "TeoríaCuánticaBásicaObservablesYMedidas"
**Quantum.ipynb**
Propósito:Implementar conceptos de teoría cuántica enfocándose en el cálculo de observables, así como en el análisis del impacto de las mediciones en los estados cuánticos.

### Ejercicio 4.5.2
Escribe el vector de estado genérico para el sistema de dos partículas con espín. Generalízalo a un sistema con n partículas 
___
Los estados básicos de una partícula con spin son:

- $$\ | \uparrow \rangle \$$
- $$\ | \downarrow \rangle \$$

Al ensamblar un sistema cuántico de dos partículas, se obtiene el producto tensor entre cada estado:

- $$\ | \uparrow \rangle \otimes | \uparrow \rangle \$$
- $$\ | \uparrow \rangle \otimes | \downarrow \rangle \$$
- $$\ | \downarrow \rangle \otimes | \uparrow \rangle \$$
- $$\ | \downarrow \rangle \otimes | \downarrow \rangle \$$

Estos estados se pueden expresar como una combinación lineal con sus coeficientes:

$$\| \Psi \rangle = a_{11} | \uparrow \uparrow \rangle + a_{12} | \uparrow \downarrow \rangle + a_{21} | \downarrow \uparrow \rangle + a_{22} | \downarrow \downarrow \rangle\$$

Analizando esta ecuación, se puede inducir que se ajusta a la forma $$\ 2^n \$$, donde $$\ n \$$ es el número de partículas en el sistema.


### Ejercicio 4.5.3
Assume the same scenario as in Example 4.5.2 and let $$\| \Phi \rangle = |x_{0} \rangle \otimes |y_{1} \rangle + |x_1 \rangle \otimes |y_1 \rangle\$$
Is this state separable?
___
Un estado es separable si puede escribirse de la forma:

$$\| \phi\rangle = |A\rangle \otimes |B\rangle \$$

El producto tensor respeta adición en $$\ \mathbb{V} \$$ y en $$\ \mathbb{V}' \$$, esto significa que la formula puede expresarse de la forma:

$$\ |\phi\rangle = |y_1\rangle \otimes (|x_0\rangle + |x_1\rangle) \$$

Esto significa que este estado es separable en un sistema no trivial de dos particulas.

### Instrucciones
1. Configuración del Entorno: Asegúrate de tener un entorno virtual Python 3.12.0 configurado.
Activa el entorno virtual:
- En Windows:
```
.venv\Scripts\activate
```
- En macOS y Linux:
```
source .venv/bin/activate
```
2. Instalación de Dependencias: Una vez activado el entorno virtual, instala las dependencias necesarias usando el siguiente comando:
```
pip install numpy matplotlib
```
