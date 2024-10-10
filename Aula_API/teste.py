import requests
import openpyxl

# url = "https://jsonplaceholder.typicode.com/users"

# response = requests.get(url)

# if response.status_code == 200:
#     users = response.json()
#     workbook =openpyxl.Workbook()
#     sheet = workbook.active
#     sheet.title = "Dados da API"
#     sheet.append(["Nome", "Email", "Telefone"])
    
#     for i in users:
#         sheet.append([i["name"], i["email"], i["phone"]])
    
#     workbook.save("dados_api.xlsx")
#     print("Dados salvos no arquivo dados_api.xlsx")
        
# else:
#     print(f"Erro ao obter os dados da API, Status code: {response.status_code}")

url = "https://loteriascaixa-api.herokuapp.com/api/megasena"

response = requests.get(url)

if response.status_code == 200:
    concurso = response.json()
    for i in concurso:
        #print(i)
        if i['data'].endswith("08/10/2024"):
            #print(f"Concurso: {i['concurso']}, Data: {i['data']}, Números: {i['dezenas']}")
            #print(f"Concurso:{i['concurso']}, Data:{i['data']}, Números:{i['dezenas']}")
            print(i)
    
    
    # workbook =openpyxl.Workbook()
    # sheet = workbook.active
    # sheet.title = "Dados da API"
    # sheet.append(["Número do Concurso", "Data do Concurso", "Números Sorteados"])

    # for i in concurso:
    #     sheet.append([i["numero"], i["data"], i["numeros"]])

    # workbook.save("dados_api.xlsx")
    # print("Dados salvos no arquivo dados_api.xlsx")

else:
    print(f"Erro ao obter os dados da API, Status code: {response.status_code}")