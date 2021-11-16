# CRIE UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA VOTO() QUE VAI RECEBER COMO PARÂMETRO O ANO DE NASCIMENTO DE UMA PESSOA, RETORNANDO UM VALOR LITERAL INDICANDO
# SE UMA PESSOA TEM VOTO NEGADO, OPCIONAL OU OBRIGATÓRIO NAS ELEIÇÕES.


def voto(nasicmento):
    # posso importar uma biblioteca somente para minha função em vez de global. Economiza memória
    from datetime import date
    idade = date.today().year - nasicmento
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL!'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'


print(voto(int(input('Digite o ano do seu nascimento: '))))



