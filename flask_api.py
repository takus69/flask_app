from flask import Flask, jsonify, request
from sqlalchemy import create_engine, String, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from flask_cors import CORS
from db import Test


app = Flask(__name__)
CORS(app)
engine = create_engine('sqlite:///data.db', echo=True)


@app.route('/api/hello/')
def hello_world():
    return jsonify({'message': 'Hello World'})

@app.route('/api/get_test/', methods=['GET'])
def get_test():
    return request.args.get('query', '')

@app.route('/api/post_test/', methods=['POST'])
def post_test():
    return request.form['query']

@app.route('/api/select_test', methods=['GET'])
def select_test():
    name = request.args.get('name', '')
    try:
        with Session(engine) as session:
            stmt = select(Test).where(Test.name==name)
            t = session.scalars(stmt).one()
    except Exception as e:
        return jsonify({'error': 'エラー'}), 500
    return jsonify({'id': t.id, 'name': t.name})


if __name__ == '__main__':
    app.run()
