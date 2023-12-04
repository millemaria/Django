from django.http import HttpResponse

def primeirapagina(request):
    return HttpResponse('''
    <!DOCTYPE html>
<html>
  <head>
    <title>Título da página exemplo</title>
  </head>
  <body>
    <h1>Um cabeçalho de nível 1</h1>
    <p>Primeiro parágrafo. Veja <a href="http://pt.lipsum.com/">Lorem Ipsum</a> para
    mais texto</p>
    <ul>
      <li>Um item de uma lista não ordenada</li>
      <li>Um item</li>
    </ul>
  </body>
</html>
''')