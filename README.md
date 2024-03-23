# TonoBot

> TonoBot henter automatisk sanger fra din gudstjenesteplan og rapporterer til Tono.

## Features

- Ukentlig rapportering (her anbefales det å kjøre programvaren på en Raspberry Pi eller lignende)
- Rapporter flere gudstjenester tilbake i tid

## Komatibel software

Per dags dato er TonoBot kun kompatibel med [Planning Center](https://www.planningcenter.com/). Vi håper å kunne støtte flere tjenester i fremtiden.

Føl deg fri til å bidra med videreutvikling av TonoBot gjennom Pull Requests.

## Hvordan bruke TonoBot

### Oppsett av Planning Center

1. Du trenger en utviklerkonto hos Planning Center. [Her](https://api.planningcenteronline.com/oauth/applications) kan du aktivere utviklermodus for din bruker.
2. Lag en ny **Personal Access Token**. Velg **2018-11-01** under **Services**.
3. Du har nå en access token som du vil trenge i neste steg.

### Oppsett av applikasjon

1. <code>git clone https://github.com/rune-m/tono-bot.git</code>
2. Naviger til mappen

```
$ cd tono-bot
```

1. Dupliser og rename **constants_template.py** til **constants.py**. (Må ligge i **src/**-mappen).

2. [Installer Python](https://www.python.org/downloads/). Jeg har brukt Python 3.10. Python 3.8-3.11 vil mest sannsynlig fungere.
3. Installer virtualenv-pakken (med pip eller pip3):

```
$ pip3 install virtualenv
```

6. Opprett et Python environment (med python/python3)

```
$ python3 -m venv env
```

7. Aktiver Python-miljøet

```
$ source env/bin/activate
```

8. Installer pakker

```
$ pip3 install -r requirements.txt
```

### Kjør applikasjonen (fra root)

```
$ env/bin/python src/main.py
```

### (Optional) Kjør på en Raspberry Pi

Her kan du bruke Python-pakken **pyvirtualdisplay**.

Mer info kommer etterhvert

## License

See the [LICENSE](https://github.com/rune-m/tono-bot/blob/main/LICENSE) file for license rights and limitations (MIT).
