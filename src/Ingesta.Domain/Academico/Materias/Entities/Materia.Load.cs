public static Materia Load(
    CodigoMateria codigo,
    string nombre,
    string clave,
    decimal creditos,
    int bloque,
    int semestre,
    int modulo,
    CodigoMateria? seriacion)
{
    return new Materia(
        codigo,
        nombre,
        clave,
        creditos,
        bloque,
        semestreOficial: semestre,
        moduloOficial: modulo,
        seriacion: seriacion
    );
}
