from flask import Flask, request, Response, Blueprint
from flask_cors import CORS
from werkzeug.serving import run_simple
from werkzeug.middleware.dispatcher import DispatcherMiddleware
import json

from mysql_db import AccountDAO, EmailDao, PhoneDao

bp = Blueprint('burritos', __name__,
               template_folder='templates')

accountDao = AccountDAO()
emailDao = EmailDao()
phoneDao = PhoneDao()


@bp.route('/page', methods=['POST', 'GET'])
def page():  # put application's code here
    args = request.args
    pageNum = int(args.get('pageNum')) if args.get('pageNum') != None else 1
    pageSize = int(args.get('pageSize')) if args.get('pageSize') != None else 10
    q = args.get('q') if args.get('q') != None else ''
    responseData = {
        "pageSize": pageSize,
        "pageNum": pageNum,
        "pageTotal": accountDao.count(q),
        "data": accountDao.selectPage((pageNum - 1) * pageSize, pageSize, q)
    }
    response = {
        "code": 200,
        "data": responseData
    }
    return Response(json.dumps(response), mimetype='application/json')


@bp.route('/add', methods=['POST', 'GET'])
def add():
    args = request.args
    obj = {
        'info': args.get('info'),
        'nickname': args.get('nickname'),
        'account': args.get('account'),
        'password': args.get('password'),
        'website': args.get('website'),
        'bind_email': args.get('bind_email'),
        'bind_phone': args.get('bind_phone'),
        'comment': args.get('comment')
    }
    accountDao.insert(obj)
    response = {
        "code": 200,
        "data": ""
    }
    return Response(json.dumps(response), mimetype='application/json')


@bp.route('/update', methods=['POST', 'GET'])
def update():
    args = request.args
    obj = {
        'id': args.get('id'),
        'info': args.get('info'),
        'nickname': args.get('nickname'),
        'account': args.get('account'),
        'password': args.get('password'),
        'website': args.get('website'),
        'bind_email': args.get('bind_email'),
        'bind_phone': args.get('bind_phone'),
        'comment': args.get('comment')
    }
    accountDao.update(obj)
    response = {
        "code": 200,
        "data": ""
    }
    return Response(json.dumps(response), mimetype='application/json')


@bp.route('/delete', methods=['POST', 'GET'])
def delete():  # put application's code here
    id = int(request.args.get('id'))
    accountDao.deleteById(id)
    response = {
        "code": 200,
        "data": ""
    }
    return Response(json.dumps(response), mimetype='application/json')


@bp.route('/emailList', methods=['POST', 'GET'])
def emailList():
    response = {
        "code": 200,
        "data": emailDao.list()
    }
    return Response(json.dumps(response), mimetype='application/json')
@bp.route('/emailName', methods=['POST', 'GET'])
def emaiName():
    response = {
        "code": 200,
        "data": emailDao.list()
    }
    return Response(json.dumps(response), mimetype='application/json')


@bp.route('/emailAdd', methods=['POST', 'GET'])
def emailAdd():
    args = request.args
    obj = {
        'info': args.get('info'),
        'email_name': args.get('email_name'),
        'account': args.get('account'),
        'password': args.get('password'),
        'website': args.get('website'),
        'comment': args.get('comment')
    }
    response = {
        "code": 200,
        "data": emailDao.insert(obj)
    }
    return Response(json.dumps(response), mimetype='application/json')


@bp.route('/emailDel', methods=['POST', 'GET'])
def emailDel():
    id = int(request.args.get('id'))
    response = {
        "code": 200,
        "data": emailDao.deleteById(id)
    }
    return Response(json.dumps(response), mimetype='application/json')


@bp.route('/phoneList', methods=['POST', 'GET'])
def phoneList():
    response = {
        "code": 200,
        "data": phoneDao.list()
    }
    return Response(json.dumps(response), mimetype='application/json')


@bp.route('/phoneAdd', methods=['POST', 'GET'])
def phoneAdd():
    args = request.args
    obj = {
        'type': args.get('type'),
        'account': args.get('account'),
        'comment': args.get('comment')
    }
    response = {
        "code": 200,
        "data": phoneDao.insert(obj)
    }
    return Response(json.dumps(response), mimetype='application/json')


@bp.route('/phoneDel', methods=['POST', 'GET'])
def phoneDel():
    id = int(request.args.get('id'))
    response = {
        "code": 200,
        "data": phoneDao.deleteById(id)
    }
    return Response(json.dumps(response), mimetype='application/json')


app = Flask(__name__, static_url_path="/")
# CORS configuration
CORS(app, supports_credentials=True)
app.register_blueprint(bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8900)
