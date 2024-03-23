import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tools.logger import Logger
from constants import MAIL_ADDRESS, MAIL_PASSWORD
from tools.utils import Status

def send_email(to_mail, result, text, unknowArtistSongs=[], songsWithoutCCLI=[]):
  from_mail = MAIL_ADDRESS
  password = MAIL_PASSWORD

  resultText = 'Suksess!' if result == Status.SUCCESS else 'Feilet'

  if from_mail == '' or password == '':
    Logger.log('Kan ikke sende mail. MAIL_ADDRESS eller MAIL_PASSWORD er ikke satt.')
    return

  statusEmoji = "✅" if result == Status.SUCCESS else "❌"

  unknowArtistSongsText = ''
  if len(unknowArtistSongs) != 0 and result == Status.SUCCESS:
    unknowArtistSongsText = '<br /><br />Sanger fra PCO som mangler låtskriver:'
    for song in unknowArtistSongs:
      unknowArtistSongsText += '<br /> - ' + song
    statusEmoji = "⚠️"
    resultText = "Suksess, men én eller flere sanger har ukjent låtskriver"

  unknowCcliText = ''
  if len(songsWithoutCCLI) != 0:
    unknowCcliText = '<br /><br />Sanger fra PCO som mangler CCLI:'
    for song in songsWithoutCCLI:
      unknowCcliText += '<br /> - ' + song

  msg = MIMEMultipart("alternative")

  msg['Subject'] = f'{statusEmoji} TonoBot har vært på jobb!'

  msg['From'] = from_mail
  msg['To'] = to_mail

  html = """\
  <html>
    <head>
      
    </head>
    <body>
      <h2>Hei!</h2>
      <p>
        Jeg har vært på jobb! Her er resultatet:
        <br /><br />
        <b>{resultText} {statusEmoji}</b>
        {unknowArtistSongsText}
        {unknowCcliText}
        <br /><br />
        <b>Logg:</b>
        <br /><br />
          <code>
          - {text}
          </code>
        <br /><br />
        <br /><br />
        Vi prates igjen neste uke!
      </p>
    </body>
  </html>
  """.format(**locals())

  part2 = MIMEText(html, "html")

  msg.attach(part2)

  server = smtplib.SMTP('smtp.gmail.com:587')
  server.starttls()
  server.ehlo()
  server.login(from_mail, password)
  Logger.log(f'Sender mail til {to_mail}')
  server.sendmail(from_mail, to_mail, msg.as_string())
  server.quit()
