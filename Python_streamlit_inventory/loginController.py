import bd;

def authenticate_user(name,senha):

    command = f'SELECT iduser, name, senha FROM user WHERE name = "{name}" and senha = "{senha}"'
    bd.cursor.execute(command)
    result = bd.cursor.fetchall()

    if result:
        return True
    else:
        return False

