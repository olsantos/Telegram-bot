import requests
import time
import json
import os


class TelegramBot1:
    def __init__(self):
        token = '5597009870:AAGop3_cdTAbkHFyKlc41qqrjWU-U_MhS6Y'
        self.url_base = f'https://api.telegram.org/bot{token}/'

    def Iniciar(self):
        update_id = None
        while True:
            atualizacao = self.obter_novas_mensagens(update_id)
            dados = atualizacao["result"]
            if dados:
                for dado in dados:
                    update_id = dado['update_id']
                    mensagem = str(dado["message"]["text"])
                    chat_id = dado["message"]["from"]["id"]
                    eh_primeira_mensagem = int(
                        dado["message"]["message_id"]) == 1
                    resposta = self.criar_resposta(
                        mensagem, eh_primeira_mensagem)
                    self.responder(resposta, chat_id)

    # Obter mensagens
    def obter_novas_mensagens(self, update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=100'
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content)

    # Criar uma resposta
    def criar_resposta(self, mensagem, eh_primeira_mensagem):
        if eh_primeira_mensagem == True or mensagem in ('suporte', 'Suporte'):
            return f'''Olá Sou seu assistente virtual me chamo UiptvIA, Digite o número rerente a sua duvida:{os.linesep}1 - Canais Travando{os.linesep}2 - Canais Offline{os.linesep}3 - Aplicativo não abre{os.linesep}4 - Outros'''
        if mensagem == '1':
            return f'''Dica 1 
desligue tudo da tomada e religue 
( tv box/tv/modem e roteador ) 

Dica 2 
Observe que temos várias
categorias de canais  e todas elas são importantes !

Trata-se de fontes diferentes, 
Como se fosse vários sistemas dentro de 1 Só. 
Servem também como uma espécie de estepe um do outro.

Observe que além das categorias padrão
Temos a grade : 

*Canais / Alternativos*
*Canais / Full HD* 
*Canais / H.265 (1)*
*Canais / H.265 (2)*
*Canais / 4K*

Então, digamos que você queira assistir o canal *SPORTV* 

você vai encontrar este canal como padrão 
Na grade de Esportes 
*SporTV     ( SD )* 
*SporTV HD*

E dentro das outras categorias citadas 
Você encontrará
o mesma *Sportv*  em algum momento pode oscilar ou falhar na categoria padrão de esportes e estar perfeito na categoria *Alternativos* e/ou *H265 [1]* e/ou *H265[2]* e/ou *Full-hd* e/ou em *4K*.

Essa regra vale para
Praticamente todos os canais

*FILMES E SÉRIES*
*VAI COMO BRINDES PRA TODOS OS CLIENTES, FILMES E SÉRIES PODE HAVER PROBLEMAS POIS É MUITOS QUE TEM DISPONÍVEL.* 
*RECOMENDAMOS* 
*QUE USA A TV SMART , TVBOX. NO CABO DE REDE ASSIM CHEGA UM SINAL MELHOR E MAIS ESTÁVEL. !* 
{os.linesep}Seu problema foi resovido?(s/n)
            '''
        elif mensagem == '2':
            return f'''Deixe o nome do canal que estaremos verificando{os.linesep}Seu problema foi resovido?(s/n)
            '''
        elif mensagem == '3':
            return f'''desligue tudo da tomada e religue 
( tv box/tv/modem e roteador ) {os.linesep}Seu problema foi resovido?(s/n)'''

        elif mensagem.lower() in ('s', 'sim'):
            return ''' Obrigado, qualquer problema estaremos a disposição '''
        elif mensagem.lower() in ('n', 'não'):
            return ''' Desculpe o ocorrido entraremos em contato para resolver seu problema '''
        else:
            return 'Olá Sou seu assistente virtual me chamo UiptvIA, Gostaria de acessar o suporte? Digite "suporte"'

    # Responder
    def responder(self, resposta, chat_id):
        link_requisicao = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_requisicao)


bot = TelegramBot1()
bot.Iniciar()