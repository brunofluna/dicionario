# dicionário
usuario = {
    'nome': 'Bruno Luna',
    'idade': 40,
    'profissão': 'Dev'
}
print(usuario['nome'])
print(usuario['idade'])
print(usuario['profissão'])
#outra forma de exibir valores de um dicionário na tela
print(usuario.get('nome'))
print(usuario.get('idade'))
print(usuario.get('profissão'))
print(usuario.get('email'))
# adicionar uma nova chave
usuario['email'] = 'bruno@brunoluna.com.br'
print('\n')
print(usuario.get('email'))

# adcionar uma nova chave
usuario['Endereço'] = input('Informe um endereço: ')

# excluindo a chave
del usuario['idade']

# exibir valores de uma outra forma diferente na tela 
for chave in usuario:
    print(f'{chave}: {usuario.get(chave)}')

