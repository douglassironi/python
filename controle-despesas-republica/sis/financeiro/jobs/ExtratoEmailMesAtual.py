from django.db.models import Sum
from financeiro.models import Extrato
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from datetime import date



html_template = """
  <html>
  <head>
  <!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

<!-- Optional theme -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">

<!-- Latest compiled and minified JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
  </head>
    <body>
       Ola querido usuario do Farofas House,
       [#usuario]
       <h1> Valores Farofas House </h1>
       <table class="table">

        <td>
        <th>Mes</th>
        <th>Valor</th>
        </tr>
        #table
      </table>
    </body>
  </html>

"""


usr= User.objects.all();
for u in usr:
    html = html_template
    tb=" "
    for x in range(1,date.today().month ):
        ex = Extrato.objects.filter(usuario=u.id, data__month = x, data__year=date.today().year).aggregate(Sum('valor')).get('valor__sum')
        tb+="<tr><td>"+str(x)+"</td><td>"+str(ex)+"</td></tr>"
    html=html.replace("#table",tb)
    html=html.replace("#usuario",u.first_name+" "+u.last_name)
    text_content = "email"
    msg = EmailMultiAlternatives('Farofas House', text_content, 'farofashouse@douglassironi.com', ['douglassironi@gmail.com',u.email])
    msg.attach_alternative(html, "text/html")
    print "Enviando email para "+ u.email
    msg.send()
