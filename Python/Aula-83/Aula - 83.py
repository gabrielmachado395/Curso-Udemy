from string import Template
from datetime import datetime
from dados_email import meu_email, minha_senha
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

meu_email = 'gabrielmachado.emp@gmail.com'
minha_senha = 'OVERHAUL'

with open(r'Aula-83\Aula - 83.html' , 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Otta', data=data_atual)

msg = MIMEMultipart()
msg['from'] = 'Gabriel'
msg['to'] =   'gabrielryuzaki@gmail.com'
msg['subject'] = 'Teste.'

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(meu_email, minha_senha)
        smtp.send_message(msg)
        print('E-mail enviado com sucesso.')
    except Exception as e:
        print('E-mail não enviado')
        print('Erro:', e)