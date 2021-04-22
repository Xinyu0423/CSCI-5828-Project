from authlib.integrations.flask_oauth2 import (
    AuthorizationServer, ResourceProtector)
from authlib.integrations.sqla_oauth2 import (
    create_query_client_func,
    create_save_token_func,
    create_bearer_token_validator,
)
from authlib.oauth2.rfc6749.grants import (
    AuthorizationCodeGrand as _AuthorizationCodeGrant,
)
from authlib.oidc.core.grants import(
    OpenIDCode as _OpenIDCode,
    OpenIDImplicitGrant as _OpenIDImplicitGrant,
    OpenIDHybridGrant as _OpenIDHybridGrant,
)
from authlib.oidc.core import UserInfo
from werkzeug.security import gen_salt
from .models import db, Account
from .models import OAuth2Client, OAuth2AuthorizationCode, OAuth2Token

DUMMY_JWT_CONFIG = {
    'key': 'secret-key',
    'alg': 'HS256', 
    'iss': 'https://project.com',
    'exp': 3600,
}

def exists_nonce(nonce, req):
    exists = OAuth2AuthorizationCode.query.filter_by(
        client_id=req.client_id, nonce=nonce
    ).first()
    return bool(exists)

def generate_user_info(account, scope):
    return UserInfo(sub=str(account.id), name=user.username)

def create_authorization_code(client, grant_user, request):
    code = gen_salt(48)
    nonce = request.data.get('nonce')
    item = OAuth2AuthorizationCode(
        code = code,
        client_id = client.client_id, 
        redirect_uri = request.redirect_uri, 
        scope = request.scope,
        user_id = grant_user.id,
        nonce = nonce,
    )
    db.session.add(item)
    db.session.commit()
    return code 

class AuthorizationCodeGrand(_AuthorizationCodeGrant):
    