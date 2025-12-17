using Ingesta.Domain.Academico.Materias.ValueObjects;

namespace Ingesta.Domain.Academico.Materias.Entities;

public sealed class Materia
{
    // -- [[ 1. Propiedades Públicas ]] --

    // - Identificación de la materia
    public CodigoMateria Codigo { get; private set; }
    public string Nombre { get; private set; }
    public string Clave { get; private set; }
    public decimal Creditos { get; private set; }

    // - Ubicación en el Mapa Curricular
    public int Semestre { get; private set; }
    public int Modulo { get; private set; }
    public int Bloque { get; private set; }

    // - Seriación
    public CodigoMateria? Seriacion { get; private set; }


    // -- [[ 2. Constructor ]] --
    public Materia(
        CodigoMateria codigo,
        string nombre,
        string clave,
        decimal creditos,
        int bloque,
        int? semestreOficial = null,
        int? moduloOficial = null,
        CodigoMateria? seriacion = null)
    {
        // - Validación de código
        if (codigo is null)
            throw new ArgumentNullException(nameof(codigo));

        // - Validaciones de nombre
        if (string.IsNullOrWhiteSpace(nombre))
            throw new ArgumentException("El nombre de la materia es obligatorio.");
        if (nombre.Length < 10 || nombre.Length > 85)
            throw new ArgumentException("La longitud del nombre no es correcta");

        // - Validaciones de clave
        if (string.IsNullOrWhiteSpace(clave))
            throw new ArgumentException("La clave de la materia es obligatoria");
        if (clave.Length != 4)
            throw new ArgumentException("La clave tiene exactamente cuatro caracteres");

        // - Validación de créditos
        if (creditos <= 0)
            throw new ArgumentException("Los créditos deben ser mayor que cero");

        // - Validación de bloque
        if (bloque != 1 && bloque != 2)
            throw new ArgumentException("El bloque solo puede ser 1 o 2");

        // - Identificación de la materia
        Codigo = codigo;
        Nombre = nombre;
        Clave = clave;
        Creditos = creditos;

        // - Semestre en la malla vs Semestre en el código de la materia
        // - Lo que venga en la malla curricular tiene prioridad pero el código académico suple la carencia
        Semestre = semestreOficial ?? codigo.Semestre;
        if (Semestre < 1 || Semestre > 8)
            throw new ArgumentException("El semestre debe estar entre 1 y 8.");

        // - Modulo en la malla vs Malla en el código de la materia
        Modulo = moduloOficial ?? codigo.Modulo;
        if (Modulo < 1 || Modulo > 4)
            throw new ArgumentException("El módulo debe estar entre 1 y 4.");


        // - Validaciones de seriacion
        Seriacion = seriacion;
        // - idempotencia
        if (Seriacion != null && Seriacion.Valor == Codigo.Valor)
            throw new ArgumentException("Una materia no puede ser requisito de si misma");
        // - semestre anterior
        if (Seriacion != null && Seriacion.Semestre >= Semestre)
            throw new ArgumentException("Una materia no puede tener un requisito de un semestre igual o posterior");
    }
}
