import requests
import lxml.html as html
import datetime

FIX_URL = 'https://www.banxico.org.mx/tipcamb/llenarTiposCambioAction.do?idioma=en'
DOLAR_FIX_VALUE = '//td[@class="b5"]//div[@id="tdSF43718"]/text()'
DOLAR_FIX_DATE = '//div[@id="fechaSF43718"]/text()'

def get_dolar_fix():
    try:
        response = requests.get(FIX_URL)
        if response.status_code == 200:
            site = response.content.decode('latin-1')
            parse = html.fromstring(site)
            dolar_value = parse.xpath(DOLAR_FIX_VALUE)
            dolar_date = parse.xpath(DOLAR_FIX_DATE)
            dolar_value = [x.strip() for x in dolar_value]
            dolar_date = [x.strip() for x in dolar_date]
            print("\t\t VALOR DEL DOLAR \n")
            print("Fix: $"+dolar_value[0])
            print("Date: "+dolar_date[0])
        else:
            raise ValueError(f'Error:  {response.status_code}')
    except ValueError as ve:
        print(ve)


def run():
    get_dolar_fix()

if __name__ == ('__main__'):
    run()