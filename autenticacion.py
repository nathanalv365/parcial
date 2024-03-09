usuarios_registrados = {}

def validar_credenciales(usuario, contrasena):
    return usuarios_registrados.get(usuario) == contrasena

def registrar_usuario(usuario, contrasena):
    if usuario not in usuarios_registrados:
        usuarios_registrados[usuario] = contrasena
        return True
    else:
        return False

