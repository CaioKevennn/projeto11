import model
import dal

class ClienteController:
    @classmethod
    def cadastrar(cls,nome,tel,cpf,enderexo,idade):
        if nome!=""  and cpf!="" and enderexo!="" and idade>0 :
            try:
                dal.ClienteDal.cadastrar(model.Cliente(nome,tel,cpf,enderexo,idade))
                return True
            except:
                return False
        
    @classmethod
    def remover(cls,codc):
        if codc!=0:
            try:
                dal.ClienteDal.remover(codc)
                return True
            except:
                return False
            
    @classmethod
    #seria uma boa ideia ter uma função para listar os clientes e seus códigos. Tambem  Fica pra versão 2.0 do projeto.
    def alterar(cls,codc,nome,tel,cpf,enderexo,idade):
        if nome!=""  and cpf!="" and enderexo!=""  and idade>=18 :
            try:
                dal.ClienteDal.alterar(codc,model.Cliente(nome,tel,cpf,enderexo,idade))
                return True
            except:
                return False
    
class FuncionarioController:
    @classmethod
    def cadastrar(cls,nome,tel,cpf,enderexo,idade):
        if nome!="" and cpf!="" and enderexo!="" and idade>=18:
            try:
                dal.FuncionarioDal.cadastrar((model.Funcionario(nome,tel,cpf,enderexo,idade)))
                return True
            except:
                return False
    @classmethod
    def remover(cls,codf):
        codf=int(codf)
        if codf!="" :
            try:
                dal.FuncionarioDal.remover(model.Funcionario(codf))
                return True
            except:
                return False
    def alterar(cls,codf,nome,tel,cpf,enderexo,idade):
        codf=int(codf)
        if nome!="" and cpf!="" and enderexo!="" and codf!="" and idade>=18:
            try:
                dal.FuncionarioDal.remover(codf,model.Funcionario(nome,tel,cpf,enderexo,idade))
                return True
            except:
                return False

class CategoriaController:
    @classmethod
    def cadastrar(cls,nome):
        if nome!="":
            try:
                dal.CategoriaDal.cadastrar(model.Categoria(nome))
                return True
            except:
                return False
    
    @classmethod
    def remover(cls,nome):
        if nome!="":
            try:
                dal.CategoriaDal.remover(model.Categoria(nome))
                return True
            except:
                return False
class ProdutoController:
    @classmethod
    def cadastrar(cls,nome,preco,quantidade,categoria):
        if nome!=""and preco !="" and quantidade>0:
            try:
                dal.ProdutoDal.cadastrar(model.Produto(nome,preco,quantidade),model.Categoria(categoria))
                return True
            except:
                return False
    @classmethod
    def remover(cls,nome,categoria):
        if nome!="":
            try:
                dal.ProdutoDal.remover(nome,model.Categoria(categoria))
                return True
            except:
                return False
    @classmethod
    #eu poderia ter recebido apenas o nome do produto1
    def alterar(cls,nome,preco,quantidade,categoria,nome1,preco1,quantidade1):
        if nome!=""and preco !="" and quantidade>0 and nome1!=""and preco1 !="" and quantidade1>0:
            try:
                dal.ProdutoDal.alterar(model.Produto(nome,preco,quantidade),model.Produto(nome1,preco1,quantidade1), model.Categoria(categoria))
                return True
            except:
                return False
            
class FornecedorController:
    @classmethod
    def cadastrar(cls,nome,tel,cpf,enderexo,idade):
        if nome!="" and cpf!="" and enderexo!="" and idade>=18:
            try:
                dal.FuncionarioDal.cadastrar((model.Funcionario(nome,tel,cpf,enderexo,idade)))
                return True
            except:
                return False
    @classmethod
    def remover(cls,codf):
        codf=int(codf)
        if codf!="" :
            try:
                dal.FuncionarioDal.remover(model.Funcionario(codf))
                return True
            except:
                return False
    def alterar(cls,codf,nome,tel,cpf,enderexo,idade):
        codf=int(codf)
        if nome!="" and cpf!="" and enderexo!="" and codf!="" and idade>=18:
            try:
                dal.FuncionarioDal.remover(codf,model.Funcionario(nome,tel,cpf,enderexo,idade))
                return True
            except:
                return False

            
class CaixaController:
    @classmethod
    def fechar(cls):
        try:
            dal.CaixaDal.fechar()
            return True
        except:
            return False 
    @classmethod
    def vender(cls,nome_produto,nome_cliente):
        dal.CaixaDal.vender(nome_produto,nome_cliente)
            
#print(ProdutoController.alterar("arroz",45,32,"Categoria3","Feijão",88,956))

#ProdutoController.alterar(("arroz",45,32,"Categoria3","Feijão",88,956))
#print(ClienteController.remover('caio',9552,9985,'qno18',21))
#print(ClienteController.remover(2))
#print(ClienteController.alterar(2,"João",9552,720,"Qno18",21))