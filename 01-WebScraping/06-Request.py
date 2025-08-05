import requests

url = "https://public.tableau.com/app/sample-data/TB_Burden_Country.csv?_gl=1*r2p9ye*_ga*NzA1NDM5NTIwLjE3NTM5MTEyNDY.*_ga_8YLN0SNXVS*czE3NTM5MTEyNDQkbzEkZzEkdDE3NTM5MTEyNjAkajYwJGwwJGgw*_gcl_au*MTU4MzAwNzIxMC4xNzUzOTExMjQ2"

data = requests.get(url).content
with open("./06-RequestsOutputs/data.csv", "wb") as file:
    file.write(data)

