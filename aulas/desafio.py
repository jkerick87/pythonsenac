while True:
    salario = int(input("DIGITE O SALARIO:"))
    emprestimo = int(input("DIGITE O VALOR DO EMPRESTIMO:"))

    percentual = int((emprestimo/salario)*100)

    if percentual <= 75:
        if percentual <= 50:
            print(f"APROVAR O EMPRESTIMO!!! PERCENTUAL DE: {percentual}%")
        else:
            print(f"EM ANALISE!!! PERCENTUAL DE: {percentual}%")
    else:
        print(f"NAO APROVAR!!!PERCENTUAL DE: {percentual}%")