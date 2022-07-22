# coding: utf-8
import json
import datetime
from flask import Flask, jsonify, request
from sqlalchemy import create_engine, text
from flask_cors import CORS
import pytz

app = Flask(__name__)
CORS(app)  # Cors 설정


# app.config.from_pyfile('config.py')
# database = create_engine(app.config['DB_URL'], encoding='utf-8')
# app.database = database


@app.route('/regala', methods=['POST'])
def start_regala():  # 함수로 정의하여 return 한 코드
    regala = request.json
    userId = regala.get('userId')
    regalaId = regala.get('regalaId')
    stadiumName = regala.get('stadiumName')
    ticketType = regala.get('ticketType')

    # 1. 촬영타입에따라 촬영 시작동작에 넘겨줘야할 파라미터가 달라짐.
    if ticketType == "SHORT":
        print("SHORT TYPE")  # 촬영 시간 30분
    elif ticketType == "MEDIUM":
        print("MEDIUM TYPE")
    elif ticketType == "LONG":
        print("LONG TYPE")
    else :
        return 4507 # error : TICKET_REGALA_INVALID_TICKET_TYPE

    # 동영상 업로드 api 호출시 body로 넘겨야하는 userId , stadiumName, regalaId
    # print(type(userId)) # int
    # print(type(stadiumName)) # str
    # print(type(regalaId)) # int
    # print(type(ticketType)) # str : SHORT , MEDIUM , LONG

    # 2. 촬영시작 로직 호출
    # if 촬영로직 실패 :
    #     return 4506 # error : TICEKT_REGALA_ALREADY_INUSE
    # 멀티 스레딩처리
            # 3. 촬영 시작과 동시에 리갈라 상태변경 api 호출 (명세서 R2) : 촬영가능으로 전환
            # 4. 촬영로직 끝나면 동영상 업로드 api 호출

    return str(2000)  # 정상 작동시 성공코드 return

if __name__ == "__main__":  # flask 마지막에 들어가는 기본
    app.run()
