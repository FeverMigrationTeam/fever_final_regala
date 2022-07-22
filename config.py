db = {
    'user': 'fever',
    'password': 'fever2022',
    'host': 'fever-final-testdb.cy76xlw8fwhe.ap-northeast-2.rds.amazonaws.com',
    'port': '3306',
    'database': 'fever'
}

DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"
