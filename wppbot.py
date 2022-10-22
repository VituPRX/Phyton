from selenium import webdriver
import time

class WhatsAppBot:
    def __init__ (self):
        self.mensagem = "Bom Diaaaaa !!"
        self.contato = ["Minha Preta ❤️"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def EnviarMensagens(self):
         # <span dir="auto" title="Minha Preta ❤️" class="ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr i0jNr">Minha Preta <img crossorigin="anonymous" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" alt="❤️" draggable="false" class="b8 emoji apple i0jNr" style="background-position: -20px 0px;"></span>
         # <div class="_2lMWa">
         # <span data-icon="send" class="">
         self.driver.get('https://web.whatssapp.com')
         time.sleep(30)
         for contato in self.contatos:
             
             contato self.driver.find_element_by_xpath(f"//span[@title='{contato}]'")
             time.sleep(3)
             contato.click()
             chat_box = self.driver.find_elements_by_class_name('_2lMWa')
             time.sleep(3)
             chat_box()
             
                
         

