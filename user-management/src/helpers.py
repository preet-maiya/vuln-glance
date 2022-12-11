import config
from keycloak import KeycloakAdmin, KeycloakOpenID
import keycloak

keycloak_openid = KeycloakOpenID(server_url=config.keycloak_url,
                                client_id="admin-cli",
                                realm_name="master",
)

def create_new_user(username, password, email=None, first_name=None, last_name=None):
    keycloak_admin = KeycloakAdmin(server_url=config.keycloak_url,
                                username='admin',
                                password='admin',
                                realm_name="master",
                                verify=True)
    
    new_user = keycloak_admin.create_user({"email":email,
                                       "username": username,
                                       "enabled": True,
                                       "firstName": first_name,
                                       "lastName": last_name,
                    "credentials": [{"value": password, "type": "password",}]})

    return new_user

def user_login(username, password):
    return keycloak_openid.token(username, password)

def user_logout(token):
    return keycloak_openid.logout(token)

def check_userinfo(token):
    try:
        keycloak_openid.userinfo(token['access_token'])
    except keycloak.exceptions.KeycloakAuthenticationError:
        return False

    return True


# keycloak_openid = KeycloakOpenID(server_url="http://localhost:8080/",
#                                 client_id="test",
#                                 realm_name="master",
#                                 client_secret_key="y0I8H03N8Sfil0mv5xPkZ7vGKJtXIfKk"
# )




# keycloak_admin = KeycloakAdmin(server_url="http://localhost:8080/",
#                             username='admin',
#                             password='admin',
#                             realm_name="master",
#                             verify=True)

# new_user = keycloak_admin.create_user({"email": "example@example.com",
#                                     "username":  "example@example.com",
#                                     "enabled": True,
#                                     "firstName": "example",
#                                     "lastName":  "example",
#                 "credentials": [{"value": "secret", "type": "password",}]})