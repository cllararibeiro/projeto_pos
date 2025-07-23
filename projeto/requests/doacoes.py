import requests

url = "http://127.0.0.1:8000"

def menu():
    print("\nMenu - Escolha uma opção:")
    print("1 - Listar todas as doações")
    print("2 - Criar doação")
    print("3 - Listar doações por nome do doador")
    print("4 - Sair")
    return input("Opção: ")

while True:
    opcao = menu()

    if opcao == "1":
        r = requests.get(f"{url}/doacoes")
        if r.status_code == 200:
            print("\nLista de doações:")
            for doacao in r.json():
                print(doacao)
        else:
            print("Erro ao buscar doações:", r.text)

    elif opcao == "2":
        nome_doador = input("Nome do doador: ")
        titulo_campanha = input("Título da campanha: ")
        tipo_doacao = input("Tipo de doação (ex: dinheiro, item): ")
        tipo_item = input("Tipo do item (se aplicável): ")
        quantidade = int(input("Quantidade: "))
        valor = float(input("Valor: "))
        data_doacao = input("Data da doação (YYYY-MM-DD):")

        doacao = {
            "nome_doador": nome_doador,
            "titulo_campanha": titulo_campanha,
            "tipo_doacao": tipo_doacao,
            "tipo_item": tipo_item,
            "quantidade": quantidade,
            "valor": valor,
            "data_doacao": data_doacao
        }

        r = requests.post(f"{url}/doacoes", json=doacao)
        if r.status_code in [200, 201]:
            print("\nDoação cadastrada com sucesso!")
            print(r.json())
        else:
            print("Erro ao cadastrar doação:", r.text)

    elif opcao == "3":
        nome = input("Digite o nome do doador para buscar as doações: ")
        r = requests.get(f"{url}/doacoes/por-nome/{nome}")
        if r.status_code == 200:
            print(f"\nDoações encontradas para {nome}:")
            for doacao in r.json():
                print(doacao)
        else:
            print("Nenhuma doação encontrada para esse nome.")

    elif opcao == "4":
        print("Saindo...")
        break

    else:
        print("Opção inválida, tente novamente.")
