total_alunos = 18
portugues_ciencias = 6
portugues_matematica = 5
matematica_ciencias = 9
todas_tres = 2

apenas_matematica = total_alunos - (
    portugues_ciencias + portugues_matematica + matematica_ciencias - 2 * todas_tres
)

print(f"Alunos em recuperação apenas em Matemática: {apenas_matematica}")
