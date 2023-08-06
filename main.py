from datetime import date
import requests

#awesomeapi
def cotacoes():
    while(True):
        requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

        requisicao_dic = requisicao.json()

        dolar = requisicao_dic['USDBRL']['bid']
        euro = requisicao_dic['EURBRL']['bid']
        btc = requisicao_dic['BTCBRL']['bid']

        data_atual = date.today()

        opcao = input("""
DIGITE A MOEDA QUE DESEJA SABER A COTAÇÃO:
[1] DÓLAR
[2] EURO
[3] BTC
[4] Sair...
--> """)
    
        if opcao == "1":
            print(f"Dolár: {dolar} ({data_atual})")
    
        elif opcao == "2":
            print(f"Euro: {euro} ({data_atual})")
    
        elif opcao == "3":
            print(f"BTC: {btc} ({data_atual})")

        elif opcao == "4":
            print("Saindo...")
            break

        else:
            print("DIGITE UM VALOR VÁLIDO")

cotacoes()


