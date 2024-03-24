def constant_not_initialized_error(variable_name):
  raise Exception(f'Konstanten {variable_name} er ikke satt.')

# Planning Center
PCO_APP_ID = constant_not_initialized_error('PCO_APP_ID') # Application ID (ligger under din access token hos Planning Center)
PCO_SECRET = constant_not_initialized_error('PCO_SECRET') # Secret (ligger under din access token hos Planning Center)
PCO_PLAN_SERVICE_TYPE_ID = constant_not_initialized_error('PCO_PLAN_SERVICE_TYPE_ID') # Service ID for planene du ønsker å hente fra Planning Center

# Tono
TONO_MAIL = constant_not_initialized_error('TONO_MAIL') # E-post for din Tono-bruker
TONO_PASSWORD = constant_not_initialized_error('TONO_PASSWORD') # Passord for din Tono-bruker

# OPTIONAL
# Om man ønsker en tilbakemelding fra TonoBot etter at den har kjørt kan man legge til en avsender mail her. For å få dette til å fungere med f.eks. Gmail må man bruke et App Password som passord. Kan opprettes her https://myaccount.google.com/apppasswords
MAIL_ADDRESS = '' # Avsender mailadresse
MAIL_PASSWORD = '' # Avsender mail passord (app password)
MAIL_TO_RECIEVE_STATUS_MAIL = [] # Liste med mailadresser som skal motta statusmail

# Info om kirken
CHURCH_INFO = {
  'navn': constant_not_initialized_error('navn'),
  'adresse': constant_not_initialized_error('adresse'),
  'postnummer': constant_not_initialized_error('postnummer'),
  'poststed': constant_not_initialized_error('poststed'),
  'tlf': constant_not_initialized_error('tlf'),
  'hjemmeside': constant_not_initialized_error('hjemmeside'),
}
