using Ingesta.Domain.Academico.Materias.Entities;
using Ingesta.Domain.Academico.Materias.ValueObjects;

namespace Ingesta.Domain.Academico.Materias.Repositories
{
    internal interface IMateriaRepository
    {
        // --- Carga inicial del catálogo ---
        // Debe leer TODAS las materias desde la infraestructura
        // y reconstruir correctamente los agregados.
        Task LoadCatalogAsync();

        // --- Consultas individuales ---
        Materia? GetByCodigo(CodigoMateria codigo);

        // --- Consultas masivas ---
        IReadOnlyCollection<Materia> GetAll();
        IReadOnlyCollection<Materia> GetBySemestre(int semestre);
        IReadOnlyCollection<Materia> GetByModulo(int modulo);

        // --- Relación de seriación ---
        // Devuelve la materia que es prerrequisito, o null si no hay seriación.
        Materia? GetPrerequisito(CodigoMateria codigoMateria);
    }
}
