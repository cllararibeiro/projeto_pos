# para rodar tem que rodar a API e dentro de requests tem que criar outro env e rodar os arquios em outro cmd 

import requests

def menu():
    print("\nMenu - Escolha uma opção:")
    print("1 - Listar todas as campanhas")
    print("2 - Buscar campanha pelo título")
    print("3 - Cadastrar campanha")
    print("4 - Editar campanha")
    print("5 - Excluir campanha")
    print("6 - Sair")
    return input("Opção: ")

if __name__ == "__main__":
    url = "http://127.0.0.1:8000"

    while True:
        opcao = menu()

        if opcao == "1":
            r = requests.get(f"{url}/campanhas")
            if r.status_code == 200:
                print("\nLista de campanhas:")
                for c in r.json():
                    print(c)
            else:
                print("Erro ao buscar campanhas:", r.text)

        elif opcao == "2":
            titulo = input("Digite o título da campanha que deseja buscar: ")
            r = requests.get(f"{url}/campanhas/{titulo}")
            if r.status_code == 200:
                print("\nCampanha encontrada:")
                print(r.json())
            else:
                print("Campanha não encontrada!")

        elif opcao == "3":
            titulo = input("Digite o título da campanha: ")
            descricao = input("Digite a descrição da campanha: ")
            meta_financeira = input("Digite a meta financeira (ex: 1000): ")  
            meta_itens = input("Digite a meta de itens (ex: 20): ")          
            data_inicio = input("Digite a data de início (YYYY-MM-DD): ")
            data_fim = input("Digite a data de fim (YYYY-MM-DD): ")
            status_input = input("Digite o status da campanha (True/False): ")
            status = status_input.lower() in ['true', '1', 'sim', 's']

            campanha = {
                "titulo": titulo,
                "descricao": descricao,
                "meta_financeira": meta_financeira,
                "meta_itens": meta_itens,
                "data_inicio": data_inicio,
                "data_fim": data_fim,
                "status": status
            }

            r = requests.post(f"{url}/campanhas", json=campanha)
            if r.status_code in [200, 201]:
                print("\nCampanha cadastrada com sucesso!")
                print(r.json())
            else:
                print("Erro ao cadastrar campanha:", r.text)


        elif opcao == "4":
            #editar campanha
            titulo_editar = input("Digite o título da campanha que deseja editar: ")
            novo_titulo = input("Novo título: ")
            nova_descricao = input("Nova descrição: ")
            nova_meta_financeira = input("Nova meta financeira (ex: 2000): ")  
            nova_meta_itens = input("Nova meta de itens (ex: 100): ")          
            nova_data_inicio = input("Nova data de início (YYYY-MM-DD): ")
            nova_data_fim = input("Nova data de fim (YYYY-MM-DD): ")
            status_input = input("Status da campanha (True/False): ")
            status = status_input.lower() in ['true', '1', 'sim', 's']

            novos_dados = {
                "titulo": novo_titulo,
                "descricao": nova_descricao,
                "meta_financeira": nova_meta_financeira,
                "meta_itens": nova_meta_itens,
                "data_inicio": nova_data_inicio,
                "data_fim": nova_data_fim,
                "status": status
            }

            r = requests.put(f"{url}/campanhas/{titulo_editar}", json=novos_dados)
            if r.status_code == 200:
                print("Campanha editada com sucesso!")
                print(r.json())
            else:
                print("Erro ao editar campanha:", r.text)


        elif opcao == "5":
            # excluir campanha 
            titulo_excluir = input("Digite o título da campanha que deseja excluir: ")
            r = requests.delete(f"{url}/campanhas/{titulo_excluir}")
            if r.status_code == 200:
                print("\nCampanha excluída com sucesso!")
                print(r.json())
            else:
                print("Campanha não encontrada!")

        elif opcao == "6":
            print("Saindo...")
            break
