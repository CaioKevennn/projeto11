import controller

def menu():
    op=int(input(('Digite a opção desejada:\n1-Caixa\n2-Produtos\n3-Categorias\n4-Clientes\n5-Funcionarios\n6-Fornecedores\n')))
    if op==1:
        caixa()

    elif op==2:
        produto()
menu()
def caixa():
     op=int(input("Digite a opção desejada:\n1-Fechar caixa\n2-Vender\n3-Voltar ao menu anterior\n"))
     if op==1:
        if controller.CaixaController.fechar():
            print("Caixa fechado com sucesso")
        else:
            print("Erro ao fechar o caixa")
     elif op==2:
        if controller.CaixaController.vender(input("Digite o nome do produto\n"),input('Digite o nome do comprador')):
            print("Venda realizada com sucesso")
            #seria interessante ter feito uma opção comprovante pra ele ser imprimido aqui ou talvez mostrar a venda que é guardada
        else:
            print("ERRO! DIGITE DADOS VALIDOS")
     elif op ==3:
         print("ERRO! DIGITE DADOS VALIDOS")
         caixa()
     else:
        print("Voltando ao menu")
        caixa()

         
def produto(): 
    op2=int(input("Digite a opção desejada:\n1-Cadastrar Produtos\n2-Remover Produtos\n3-Alterar Produtos\n4-Voltar ao menu anterior\n"))
    if op2==1:
        if controller.ProdutoController.cadastrar(input("Digite o nome do produto\n"),float(input("Digite o preço do produto\n")),int(input("Digite a quantidade do produto\n")),input("Digite a categoria do produto\n")):
            print("Produto Cadastrado com sucesso")
        else:
            print("ERRO! DIGITE DADOS VALIDOS")
            produto()
    elif op2==2:
        if controller.ProdutoController.remover(input("Digite o nome do produto\n"),(input("Digite a categoria do produto\n"))):
            print("Produto removido com sucesso")
        else:
            print("ERRO! DIGITE DADOS VALIDOS" )
            produto()
    elif op2==3:
        print('Digite os seguintes dados originais do produto:')
        if controller.ProdutoController.alterar(input("Digite o nome do produto\n"),float(input("Digite o preço do produto\n")),int(input("Digite a quantidade do produto\n")),input("Digite a categoria do produto\n"),input("Digite os novos dados\n Digite o nome do produto\n"),float(input("Digite o preço do produto\n")),int(input("Digite a quantidade do produto\n"))):
            print("Produto cadastrado com sucesso")
        else:
            print("ERRO! DIGITE DADOS VALIDOS")
            produto()
    elif op2==4:
        menu()
    else:
        print("Programa Finalizado")

def categoria():
    op2=int(input("Digite a opção desejada:\n1-Cadastrar Categoria\n2-Remover Categoria\n3-Voltar ao menu anterior\n"))
    if op2==1:
        if controller.CategoriaController.cadastrar(input("Digite o nome da Categoria")):
            print("Categoria cadastrada com sucesso")
        else:
            print("ERRO! DIGITE DADOS VALIDOS")
            categoria()
    if op2==2:
        if controller.CategoriaController.remover(input("Digite o nome da categoria")):
            print("Categoria cadastarda com sucesso")
        else:
            print("ERRO! DIGITE DADOS VALIDOS")
            categoria()
    if op2==3:
        categoria()
    else:
        print("Digite a opção valida")

def cliente():
        op2=int(input("Digite a opção desejada:\n1-Cadastrar Cliente\n2-Remover Cliente\n3-Alterar cliente\n4-Voltar ao menu anterior\n"))
        if op2==1:
            if controller.ClienteController.cadastrar(input("Digite o nome do cliente"),input("Digite o telefone do cliente"),input("Digite o endereço do cliente",input("Digite a idade do cliente"))):
                print("Cliente cadastrado com sucesso")
            else:
                print("ERRO! DIGITE DADOS VALIDOS")
        if op2==2:
            if controller.ClienteController.remover(input("Digite o código do cliente")):
                print("Cliente cadastrado com sucesso")
            else:
                print("ERRO! DIGITE DADOS VALIDOS")
        if op2==3:
            if controller.ClienteController.alterar(input("Digite o código do cliente"),input("Digite o novo nome"), input("Digite o novo telefone"), input("Digite o novo CPF"), input("Digite o novo endereço"),input("Digite a nova idade")):
                print("Cliente alterado com sucesso")
            else:
                print("ERRO! DIGITE DADOS VALIDOS")
        if op2==4:
            menu()
        else:
            print("ERRO! DIGITE DADOS VALIDOS")
            cliente()
def funcionario():
        op2=int(input("Digite a opção desejada:\n1-Cadastrar Funcionario\n2-Remover Funcionario\n3-Alterar Funcionario\n4-Voltar ao menu anterior\n"))
        if op2==1:
            if controller.FuncionarioController.cadastrar(input("Digite o nome do Funcionario"),input("Digite o telefone do Funcionario"),input("Digite o endereço do Funcionario",input("Digite a idade do Funcionario"))):
                print("Funcionario cadastrado com sucesso")
            else:
                print("ERRO! DIGITE DADOS VALIDOS")
        if op2==2:
            if controller.FuncionarioController.remover(input("Digite o código do Funcionario")):
                print("Funcionario cadastrado com sucesso")
            else:
                print("ERRO! DIGITE DADOS VALIDOS")
        if op2==3:
            if controller.ClienteController.alterar(input("Digite o código do Funcionario"),input("Digite o novo nome"), input("Digite o novo telefone"), input("Digite o novo CPF"), input("Digite o novo endereço"),input("Digite a nova idade")):
                print("Funcionario alterado com sucesso")
            else:
                print("ERRO! DIGITE DADOS VALIDOS")
        if op2==4:
            menu()
        else:
            print("ERRO! DIGITE DADOS VALIDOS")
            funcionario()

def fornecedores():
        op2=int(input("Digite a opção desejada:\n1-Cadastrar Fornecedor\n2-Remover Fornecedor\n3-Alterar Fornecedor\n4-Voltar ao menu anterior\n"))
        if op2==1:
            if controller.FornecedorController.cadastrar(input("Digite o nome do Fornecedor"),input("Digite o telefone "),input("Digite o endereço ",input("Digite a idade"))):
                print("Fornecedores cadastrado com sucesso")
            else:
                print("ERRO! DIGITE DADOS VALIDOS")
        if op2==2:
            if controller.FornecedorController.remover(input("Digite o código do Fornecedores")):
                print("Fornecedores cadastrado com sucesso")
            else:
                print("ERRO! DIGITE DADOS VALIDOS")
        if op2==3:
            if controller.FornecedorController.alterar(input("Digite o código do Fornecedores"),input("Digite o novo nome"), input("Digite o novo Telefone"), input("Digite o novo CPF"), input("Digite o novo endereço"),input("Digite a nova idade")):
                print("Fornecedores alterado com sucesso")
            else:
                print("ERRO! DIGITE DADOS VALIDOS")
        if op2==4:
            menu()
        else:
            print("ERRO! DIGITE DADOS VALIDOS")
            fornecedores()

    


    




