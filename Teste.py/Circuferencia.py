def calcular_novo_salario(salario_atual, percentual_reajuste):
    if salario_atual < 0 or percentual_reajuste < 0:
        return None

    reajuste = salario_atual * (percentual_reajuste / 100)
    novo_salario = salario_atual + reajuste

    return novo_salario


salario_atual = float(input('Digite o valor do salário atual: R$ '))
percentual_reajuste = float(input('Digite o percentual de reajuste (%): '))

novo_salario = calcular_novo_salario(salario_atual, percentual_reajuste)

if novo_salario is not None:
    print(f'O novo salário após o reajuste de {percentual_reajuste}% é: R$ {novo_salario:.2f}')
else:
    print('Erro: O salário atual e o percentual de reajuste devem ser valores positivos.')