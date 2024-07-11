import bcrypt


def criptografar_senha(senha):
    salt = bcrypt.gensalt()
    hashed_senha = bcrypt.hashpw(senha.encode("utf-8"), salt)
    return hashed_senha


def verificar_senha(senha, hashed_password):
    return bcrypt.checkpw(senha.encode("utf-8"), hashed_password)




