"""
   * [Passo 1]: Importar as bibliotecas "feedparser", "validators" e "flet".
      - feedparser: ()=> Carregar feeds do Website
      - validators: ()=> Validar URl
      - flet: ()=> Criar a Interface da Aplicação Web
      
   * [Passo 2]: Criar a interface:
      - Passo 2.1: Título.
      - Passo 2.2: Campo de inserção de URL e botão para carregar os feeds.

   * [Passo 3]: Criar funções para o carregamento de conteúdo ao clicar no botão:
      - Passo 3.1: Validar URL.
      - Passo 3.2: Carregar o feed ou novos Feeds em seguida.

   * (Cassos Testes):
      - https://www.descomplicandotech.com/feeds/posts/default
      - https://www.newsbtc.com/feed/
      - https://www.cryptoninjas.net/feed/
      - https://cointelegraph.com/rss/
"""

import feedparser as fdp
import validators
import flet as ft

def main(page):
   # Estilo
   page.padding = 40
   page.title = 'RSS Feed Reader'
   page.scroll = True

   # Passo (3)
   def load_feed(event):
      url = input_url.value
      
      # Validando a URL
      if validators.url(url):
         
         # Recebendo os Feeds e Atribuindo eles á "datas"
         datas = fdp.parse(url)
         
         feeds = [] # Lista onde sera Armazenado os feeds
         container_feeds = ft.Column(feeds) # Coluna onde será exibido os feeds

         for data in datas['entries']:
            # Verificar diferentes possíveis chaves para a imagem
            image_src = None
            if 'media_thumbnail' in data: image_src = data['media_thumbnail'][0]['url']
            elif 'media_content' in data: image_src = data['media_content'][0]['url']
            elif 'gd_image' in data: image_src = data['gd_image']
            else: image_src = "https://via.placeholder.com/100"

            photo_feed = ft.Image(src=image_src, width=100, height=100, fit=ft.ImageFit.CONTAIN)
            title_feed = ft.Text(data["title"], weight="bold")
            link_feed = ft.TextButton(data["link"], on_click=lambda e, link=data["link"]: page.launch_url(link))
            content_feed = ft.Column([title_feed, link_feed])
            line_feed = ft.Row([photo_feed, content_feed])
            feeds.append(line_feed)
            
         page.add(container_feeds)
            
      else:
         alert = ft.SnackBar(
               content=ft.Text('URL Inválida', color='white'),
               bgcolor=ft.colors.RED_500,
               duration=3000
         )
         page.show_snack_bar(alert)

   # Passo (2.1)
   title = ft.Text('RSS Feed Reader\n')
   page.add(title)

   # Passo (2.2)
   input_url = ft.TextField(label='Url', border_color=ft.colors.GREY_800, border_width=1, focused_border_color=ft.colors.GREY_700)
   btn_send = ft.ElevatedButton(text='Carregar', width=110, height=50, on_click=load_feed)
   line_url_send = ft.Row([input_url, btn_send])
   page.add(line_url_send)

# Executar App
ft.app(main)
