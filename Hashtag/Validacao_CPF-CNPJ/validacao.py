from validate_docbr import CPF, CNPJ

"""
    Valida um CPF ou CNPJ utilizando a biblioteca validate-docbr.
    Na função validar_cpf, é criado um objeto da classe CPF e o método validate é chamado para verificar a validade do CPF fornecido.
    Na função validar_cnpj, é criado um objeto da classe CNPJ e o método validate.
    
    Argumentos:
    cpf (str): O número do CPF a ser validado.
    cnpj (str): O número do CNPJ a ser validado.
    Retorna:
    bool: True se o CPF ou CNPJ for válido, False caso contrário.
    
""" 

def validar_cpf(cpf: str) -> bool:
    validador_cpf = CPF()
    return validador_cpf.validate(cpf)

def validar_cnpj(cnpj: str) -> bool:
    validador_cnpj = CNPJ()
    return validador_cnpj.validate(cnpj)

print("Digite seu CPF: ")
cpf_input = input()

if validar_cpf(cpf_input):
    print("CPF válido.")
else:
    print("CPF inválido.")

print("Digite seu CNPJ: ")
cnpj_input = input()

if validar_cnpj(cnpj_input):
    print("CNPJ válido.")
else:
    print("CNPJ inválido.")
