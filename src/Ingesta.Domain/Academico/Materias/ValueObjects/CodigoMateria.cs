namespace Ingesta.Domain.Academico.Materias.ValueObjects;

public sealed record CodigoMateria
{
    // -- [[ Propiedades ]] --
    public string Valor { get; }

    // - Componentes del Código de Materia
    public int Modulo { get; }
    public int Semestre { get; }
    public int Consecutivo { get; }

    // -- [[ Constructor ]] --
    public CodigoMateria(string valor)
    {
        // -- [[ Validaciones de Formato ]] --
        // - null/empty/whitespace
        if (string.IsNullOrWhiteSpace(valor))
            throw new ArgumentException("El código de materia no puede estar vacío.", nameof(valor));
        
        // - longitud
        if (valor.Length != 8)
            throw new ArgumentException("El código debe tener exactamente 8 caractéres");

        // - carrera
        if (!valor.StartsWith("1514"))
            throw new ArgumentException("El código de la materia debe comenzar con 1514");


        // -- [[ Validaciones de parsing ]] --
        // - módulo
        int modulo = ConvierteInt(valor.Substring(4, 1));
        int semestre = ConvierteInt(valor.Substring(5, 1));
        int consecutivo = ConvierteInt(valor.Substring(6, 2));


        // -- [[ Lógica de negocios ]] --
        // - Módulo
        if (modulo < 1 || modulo > 4)
            throw new ArgumentException($"Módulo incorrecto: {modulo}. Módulo debe ser un número entre 1 y 4");

        // - Semestre
        if (semestre < 1 || semestre > 8) 
            throw new ArgumentException($"Semestre {semestre} es incorrecto. Debe estar entre 1 y 8");

        // - Consecutivo
        if (consecutivo < 1 || consecutivo > 46)
            throw new ArgumentException($"El consecutivo {consecutivo} es incorrecto. Los valores aceptados van del 1 al 46");

        // -- [[ Asignación de propiedades ]]
        Valor = valor;
        Modulo = modulo;
        Semestre = semestre;
        Consecutivo = consecutivo;  
    }

    private int ConvierteInt(string valor)
    {
        int val = 0;
        if (!int.TryParse(valor, out val))
            throw new ArgumentException($"El valor {valor} no es un entero válido");
        return val;
    }
}
