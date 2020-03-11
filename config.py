import os
basedir = os.path.abspath(os.path.dirname(__file__))

SERVER = 'PARSLEY.arvixe.com'
DATABASE = 'SQL_Pruebas'
DRIVER = 'SQL Server Native Client 11'
USERNAME = 'giroadmin'
PASSWORD = 'gr_PW77'
SQLALCHEMY_DATABASE_URI = f'mssql+pymssql://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}?driver={DRIVER}'
