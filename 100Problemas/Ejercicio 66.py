def reprobado():
    nombres = ["Lulu", "Juan", "Ana", "Luisa"]
    calif = [60, 87, 98, 69]
    reprobados = []
    for i in range (len(calif)):
        if calif[i]<70:
            reprobados.append(nombres[i])
    print(f"Los reprobados son: {reprobados}")
    return reprobados
reprobado()