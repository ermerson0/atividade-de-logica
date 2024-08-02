total_alunos = 36
erraram_todas = 4
apenas_segunda = 5
apenas_terceira = 7
primeira_e_segunda = 9
primeira_e_terceira = 10
segunda_e_terceira = 7

acertaram_alguma = total_alunos - erraram_todas

exatamente_duas = (primeira_e_segunda - apenas_segunda - apenas_terceira) + \
                  (primeira_e_terceira - apenas_segunda - apenas_terceira) + \
                  (segunda_e_terceira - apenas_segunda - apenas_terceira)

acertaram_todas = acertaram_alguma - (apenas_segunda + apenas_terceira + exatamente_duas)

print(f"Alunos que acertaram todas as questões: {acertaram_todas}")
