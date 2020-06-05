from jwt import decode, encode, DecodeError

# global variables
data = {'language': 'Python'}
secret = 'acelera'


def create_token(data, secret):
    """ Create new Hs256 token """
    return encode(data, secret, algorithm='HS256')


def verify_signature(token):
    """ Verify signature from Hs256 token """
    try:
        return decode(token, secret, algorithm='HS256')
    except DecodeError:
        return {'error': 2}
    except:
        print('Error not recognize!')
