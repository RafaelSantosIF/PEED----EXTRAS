cadastro1, cadastro2, cadastro3 = {}, {}, {}

def cadastrar(cdg):
    user = input("Nome do Usuário: ")
    season = int(input("Número da Temporada: "))
    score = float(input("Pontuação: "))
    if cdg == 111:
        chave = {"NOME": user, "TEMPORADA": season, "PONTOS": score}
        cadastro1[user] = chave
        print(cadastro1)
    elif cdg == 222:
        chave = {"NOME": user, "TEMPORADA": season, "PONTOS": score}
        cadastro2[user] = chave
        print(cadastro2)
    elif cdg == 333:
        chave = {"NOME": user, "TEMPORADA": season, "PONTOS": score}
        cadastro3[user] = chave
        print(cadastro3)

def pesquisar(cdg, search):
    if cdg == 111:
        resultado_pesquisa = cadastro1.get(search, 'Usuário Não Encontrado')
        print(resultado_pesquisa)
    elif cdg == 222:
        resultado_pesquisa = cadastro2.get(search, 'Usuário Não Encontrado')
        print(resultado_pesquisa)
    elif cdg == 333:
        resultado_pesquisa = cadastro3.get(search, 'Usuário Não Encontrado')
        print(resultado_pesquisa)

def editar(cdg, search):
    pesquisar(cdg, search)
    change = int(input("EDITAR: \n [1] PONTUAÇÃO [2] TEMPORADA\n:"))
    new_value = int(input("NOVO VALOR\n: "))
    if cdg == 111:
        if change == 1:
            cadastro1[search].update({"PONTOS": new_value})
        if change == 2:
            cadastro1[search].update({"TEMPORADA": new_value})
    elif cdg == 222:
        if change == 1:
            cadastro2[search].update({"PONTOS": new_value})
        if change == 2:
            cadastro2[search].update({"TEMPORADA": new_value})
    elif cdg == 333:
        if change == 1:
            cadastro3[search].update({"PONTOS": new_value})
        if change == 2:
            cadastro3[search].update({"TEMPORADA": new_value})

def excluir(cdg, search):
    if cdg == 111:
        del cadastro1[search]
    elif cdg == 222:
        del cadastro2[search]
    elif cdg == 333:
        del cadastro3[search]

def menu(cdg):
    opt = int(input("[1] CADASTRAR || [2] PESQUISAR || [3] EDITAR || [4] EXCLUIR || [5] TROCAR REGISTRO || [6] ENCERRAR \n:"))
    if opt == 1:
        cadastrar(cdg)
        menu(cdg)
    elif opt == 2:
        search = input("Nome do Usuário: ")
        pesquisar(cdg, search)
        menu(cdg)
    elif opt == 3:
        search = input("Nome do Usuário: ")
        editar(cdg, search)
        menu(cdg)
    elif opt == 4:
        search = input("Nome do Usuário: ")
        excluir(cdg, search)
        menu(cdg)
    elif opt == 5:
        main()
    elif opt == 6:
        print("ENCERRANDO REGISTRO [...]\n")
        exit()
    else:
        print("AÇÃO INVÁLIDA")
        menu(cdg)


def main():
    codigo = int(input("Código de Cadastro\n:"))
    menu(codigo)

if __name__ == "__main__":
    main()
