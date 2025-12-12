# Instrumento  de Gestión de Trayectoria Académica (INGESTA)

## Visión del Producto

INGESTA es una solución de software diseñada para asegurar el egreso exitoso de estudiantes en programas de educación superior de la UnADM con reglamentos de permanencia estrictos. Su objetivo principal es mitigar el riesgo de deserción académica mediante la proyección, monitoreo y gestión en tiempo real del avance curricular, centralizando la "Malla Curricular" como la fuente de verdad inmutable y contrastándola contra el desempeño dinámico del alumno.

## Definición de Bounded Contexts (Contextos Delimitados)

El dominio se divide en tres contextos fundamentales que encapsulan reglas de negocio específicas:

### 1. Contexto de Definición Curricular (El "Deber Ser")

Este contexto modela la estructura estática e invariable del programa educativo, basándose en la Ingeniería en Desarrollo de Software de la UnADM.

#### Responsabilidad
Proveer la topología del mapa curricular2, garantizando la integridad de las relaciones de dependencia (seriación) y la correcta ubicación temporal de las asignaturas.

#### Reglas de Negocio Críticas

- _Preminencia de la Malla_
: La ubicación visual de la asignatura en el mapa curricular dicta su Semestre y Módulo oficial, sobreescribiendo cualquier inconsistencia en la codificación de la clave (e.g., asignaturas visualmente en 4º semestre que poseen claves de 2º semestre).
- _Grafo de Dependencias_
: Una asignatura puede desbloquear múltiples rutas curriculares simultáneamente (relación 1:N). Ejemplo: Bases de Datos desbloquea tanto Estructura de Datos como Programación Orientada a Objetos I.
- _Estructura Modular_
: El plan se organiza jerárquicamente en Módulos, Semestres y Bloques.

### 2. Contexto de Trayectoria Académica (El "Ser")
Este es el _Core Domain_. Administra el ciclo de vida del estudiante a través del tiempo, gestionando la instanciación de las asignaturas en ciclos lectivos (Cursadas).

#### Responsabilidad
Mantener el estado histórico y actual del avance ("Kardex Vivo").
Reglas de Negocio Críticas:

#### Regla de Permanencia (Invariante de Riesgo)
Una asignatura posee un contador de intentos de cursada. Si el contador de intentos fallidos llega a 3, el sistema debe emitir una alerta crítica de riesgo de expulsión (Baja Definitiva).

#### Validación de Prerrequisitos
No es posible inscribir una cursada si las asignaturas seriadas previas no tienen estado "Aprobado" en el historial.

### 3. Contexto de Evaluación Continua (El "Hacer")

Motor de cálculo que opera dentro de una Cursada activa.

#### Responsabilidad
Proyectar y calcular la calificación final basándose en el cumplimiento de un "Plan de Evaluación".

#### Reglas de Negocio Críticas

##### Promedio Diluido
La calificación no es un promedio de lo entregado, sino una acumulación de puntos sobre un TotalActividadesPlanificadas. Esto permite visualizar el impacto real de una tarea no entregada (calificación 0 implícita) sobre la nota final.

##### Umbral de Aprobación
La cursada cambia su estado a "Aprobada" si y solo si la calificación acumulada es $\ge 7.0$ al cierre del ciclo lectivo.
