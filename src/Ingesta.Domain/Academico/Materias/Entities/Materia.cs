using Ingesta.Domain.Academico.Materias.ValueObjects;

namespace Ingesta.Domain.Academico.Materias.Entities;

public sealed class Materia
{
    // -- [[ 1. Propiedades Públicas ]] --

    // - Identificación de la materia
    public Guid Id { get; private set;  }
    public CodigoMateria Codigo { get; private set; }
    public string Nombre { get; private set; }
    public decimal Creditos { get; private set; }

    // - Ubicación en el Mapa Curricular
    public int Semestre { get; private set; }
    public int Modulo { get; private set; }

    // - Seriación
    public CodigoMateria? Seriacion { get; private set; }


    // -- [[ 2. Constructor ]] --
    public Materia(
        CodigoMateria codigo,
        string nombre,
        decimal creditos,
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

        // - Validación de créditos
        if (creditos <= 0)
            throw new ArgumentException("Los créditos deben ser mayor que cero");

        // - Identificación de la materia
        Id = Guid.NewGuid();
        Codigo = codigo;
        Nombre = nombre;
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
