from flask import Flask, jsonify
from sqlalchemy import create_engine
import pandas as pd

SERVER = 'PARSLEY.arvixe.com'
DATABASE = 'SQL_Pruebas'
DRIVER = 'SQL Server Native Client 11'
USERNAME = 'giroadmin'
PASSWORD = 'gr_PW77'
DATABASE_CONNECTION = f'mssql+pymssql://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}'

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return ''' <h1> Hello World </h1>
    <p> this is the main apge <p>'''

@app.route('/v1/matchs', methods=['GET'])
def matchs():
    engine = create_engine(DATABASE_CONNECTION)
    connection = engine.connect()

    class Match():
        iid = ""
        date = ""
        home_team = ""
        away_team = ""
        home_ft = ""
        away_ft = ""
        tournament = ""
        city = ""
        country = ""

        def __init__(self, iid, date, home_team, away_team, home_ft, away_ft, tournament, city, country):
            self.iid = iid
            self.date = date
            self.home_team = home_team
            self.away_team = away_team
            self.home_ft = home_ft
            self.away_ft = away_ft
            self.tournament = tournament
            self.city = city
            self.country = country

        def serialize(self):
            return {"id":self.iid,
                    "date": self.date,
                    "home_team": self.home_team,
                    "away_team": self.away_team,
                    "home_ft": self.home_ft,
                    "away_ft": self.away_ft,
                    "tournament": self.tournament,
                    "city": self.city,
                    "country": self.country}

    data = pd.read_sql_query("select top 1000 * from dbo.results", connection)
    lts = list(map(lambda match: Match(match[0],
                                       match[1]['day'],
                                       match[1]['home_team'],
                                       match[1]['away_team'],
                                       match[1]['home_ft'],
                                       match[1]['away_ft'],
                                       match[1]['tournament'],
                                       match[1]['city'],
                                       match[1]['country']), data.iterrows()))
    return jsonify({'matchs':
                    list(map(lambda match: match.serialize(), lts))})

if __name__ == '__main__':
    app.run()
