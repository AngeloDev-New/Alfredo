

from aux_seleniun import chrome_driver
from time import sleep
from datetime import datetime
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By


menu_itens = 'Rota','Trajetoria','Sair'
class Alfredo:
    def __init__(self,AlfredoName = 'Alfredo',initial_mensage = 'Initializing DATE',end_mensage = 'bye DATE'):

        self.end_mensage = end_mensage
        self.driver = chrome_driver()

        self.output_xpath = '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div/div[3]/div[1]/p'
        self.driver.get('https://web.whatsapp.com/')
        XPATH = '/html/body/div[1]/div/div/div[3]/div/div[3]/div/div[1]/div/div[2]/div/div/div[1]/p'
        self.driver.EscrevaAqui(XPATH,AlfredoName,enviar_enter=True)
        self.initial_time = str(datetime.now())
        print(self.initial_time)
        self.driver.EscrevaAqui(self.output_xpath,'Alfredo: '+initial_mensage.replace('DATE',self.initial_time),enviar_enter=True)
        milicode = self.initial_time.split('.')[-1]
        print(milicode)
        # print(self.driver.getXpath(milicode))



    def __del__(self):
        self.driver.EscrevaAqui(self.output_xpath,self.end_mensage.replace('DATE',str(datetime.now())),enviar_enter=True)
        sleep(3)

    def mensagen(self,mensagen):
        mensagen = 'Alfredo: '+mensagen
        self.driver.EscrevaAqui(self.output_xpath,mensagen,enviar_enter=True)

    def menu(self,* itens):
        for i,iten in enumerate(itens):
            self.mensagen(str(i+1)+') '+iten)
    def listen(self, xpath_base="/html/body/div[1]/div/div/div[3]/div/div[4]/div/div[2]/div/div[2]/*"):
        old_html = ''
        while True:
            try:
                elementos = self.driver.find_elements(By.XPATH, xpath_base)
                conteudo_texto = "\n".join([el.text for el in elementos])
                if conteudo_texto != old_html and not conteudo_texto.split('\n')[-3].startswith('Alfredo: '):
                    old_html = conteudo_texto
                    yield conteudo_texto.split('\n')[-3]
                sleep(0.5)  # evita loop agressivo
            except WebDriverException:
                print("Driver foi encerrado ou navegador fechado.")
                yield "sair"
                break
alfredo = Alfredo()
def google_maps(mensagen):
    if mensagen == 'Rota':
        return 'Modo rotas Iniciado:'
    pesquisa = 'https://www.google.com/maps/search/PESQUISA'
    return pesquisa.replace('PESQUISA',mensagen).replace(' ','+')

def get_rota(it):
    for mensagen in it:
        if mensagen == 'Sair':
            alfredo.mensagen('Retornando ao menu principal')
            alfredo.menu(* menu_itens)
            break
        alfredo.mensagen(google_maps(mensagen))

def get_trajetoria(it):
    points = []
    base = "https://www.google.com/maps/dir/"
    for mensagen in it:
        if mensagen == 'Trajetoria':
            alfredo.mensagen('Modo trajetoria iniciado')
            continue
        if mensagen == 'Sair':
            alfredo.mensagen('Retornando ao menu principal')
            alfredo.menu(* menu_itens)
            break
        if mensagen == 'Start':
            traject = base+'current+location/'
            for point in points:
                if point == 'Trajetoria':
                    continue
                traject+=point.replace(' ','+')+'/'
            traject+='current+location/'
            alfredo.mensagen(f'O trajeto foi definido-> {traject}')
            points = []
            continue
        points.append(mensagen)
        alfredo.mensagen(f'Ponto n {len(points)} adicionado')
        

                 
if __name__=='__main__':
    listen = alfredo.listen()
    alfredo.menu(* menu_itens)
    for mensagen in listen:
        print("New message:",mensagen)

        if mensagen == 'Sair':
            del alfredo
            break
        elif mensagen == 'Rota':
            get_rota(alfredo.listen())

        elif mensagen == 'Trajetoria':
            get_trajetoria(alfredo.listen())

        else:
            alfredo.menu(* menu_itens)
        
        
