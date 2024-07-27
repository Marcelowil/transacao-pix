from validate_docbr import CPF

def formatar_chaves(tipo, chave):
    if len(chave) == 11:
        if tipo == 'cpf':
            chave = CPF().mask(chave)
        else:
            ddd = chave[:2]
            primeira_parte = chave[2:7]
            segunda_parte = chave[7:]
            chave = f"({ddd}) {primeira_parte}-{segunda_parte}"
    elif '@' in chave and tipo == 'email':
        return chave
    
    return chave

def mascarar_chave(tipo, chaves):
    if tipo == 'cpf':
        chave_mascarada =  f'***.{chaves[tipo][3:6]}.{chaves[tipo][6:9]}-**'
    elif tipo == 'telefone':
        chave_mascarada = f'({chaves[tipo][:2]}){chaves[tipo][2:4]}***-**{chaves[tipo][9:]}'
    else:
        parte_local, dominio = chaves[tipo].split('@')
        parte_mascarada = '*' * (len(parte_local) - 2 - 2)
        parte_local_mascarada = parte_local[:2] + parte_mascarada + parte_local[-2:]
        chave_mascarada = parte_local_mascarada + '@' + dominio
    
    return chave_mascarada

def mascarar_cpf(cpf):
    return f'***.{cpf[3:6]}.{cpf[6:9]}-**'

def validar_chave_destinatario(valor):
    if "@" in valor:
        return valor
    else:
        return valor.replace('.', '').replace('-', '').replace('(', '').replace(')', '').replace(' ','')
