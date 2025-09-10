#esta funcion valida para el usuario y la contraseña cadena de string

def validar_login(usuario, contraseña):
    if not isinstance(usuario, str) or not isinstance(contraseña, str):
        raise TypeError("Usuario y contraseña deben ser cadenas de texto.")

    if len(usuario.strip()) == 0:
        raise ValueError("El nombre de usuario no puede estar vacío.")

    if len(contraseña) < 6:
        raise ValueError("La contraseña debe tener al menos 6 caracteres.")

    if " " in contraseña:
        raise ValueError("La contraseña no puede contener espacios.")

    return "Acceso concedido"