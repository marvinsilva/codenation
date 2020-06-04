import jwt
from jwt import DecodeError

# global variables
secret = 'acelera'
payload = {'language': 'Python'}


def create_token(data, secret):
    return jwt.encode(data, secret, algorithm='HS256')


def verify_signature(token):
    try:
        decode_info = jwt.decode(token, secret, algorithm='HS256')
    except DecodeError:
        return {'error': 2}
    except:
        print('Erro desconhecido!')
    else:
        return decode_info
