import model
import json
class ClienteDal:
    @classmethod
    def cadastrar(cls,cliente:model.Cliente):
        with open('cliente.txt','a',encoding='utf-8') as arq:
            cliente.codc=0
            with open('cliente.txt','r', encoding='utf-8') as aqr2:
                for i in aqr2:
                    linha=i.split(',')
                cliente.codc=int(linha[5])
            arq.write(f"{cliente.nome},{cliente.tel},{cliente.cpf},{cliente.endereco},{cliente.idade},{cliente.codc+1}\n")

    @classmethod
    def remover(cls,codc):
        linhas=''
        listanova=[]
        with open('cliente.txt','r',encoding='utf-8' ) as arq:
            for i in arq:
                linhas=i.split(',')
                if int(linhas[5]) !=codc:
                    listanova.append(i)
        with open('cliente.txt','w',encoding='utf-8') as arq:
            arq.writelines(listanova)

    @classmethod
    def alterar(cls,codc,clientee2:model.Cliente):
        listanova=[]
        with open ('cliente.txt','r',encoding='utf-8') as arq:
            for i in arq:
                linha=i.split(',')
                if int(linha[5])== codc:
                    listanova.append(f"{clientee2.nome},{clientee2.tel},{clientee2.cpf},{clientee2.endereco},{clientee2.idade},{linha[5]}")
                else:
                    listanova.append(i)
        with open('cliente.txt','w',encoding='utf-8') as arq:
            arq.writelines(listanova)

class FuncionarioDal:
    @classmethod
    def cadastrar(cls,funcionario:model.Funcionario):
        linha=''
        with open('funcionarios.txt','a', encoding='utf-8') as arq:
            with open('funcionarios.txt','r', encoding='utf-8') as arq2:
                for i in arq2:
                    linha=i.split(',')
                    print(len(linha))
            arq.write(f"{funcionario.nome},{funcionario.tel},{funcionario.cpf},{funcionario.endereco},{funcionario.idade},{int(linha[5])+1}\n")

    @classmethod
    def remover(cls,codf):
        listanova=[]
        with open('funcionarios.txt','r',encoding='utf-8') as arq:
            linhas=[]
            for i in arq:
                linhas=i.split(',')
                if codf != int(linhas[5]):
                    listanova.append(i)
        with open('funcionarios.txt','w',encoding='utf-8') as arq:
            arq.writelines(listanova)

    @classmethod
    def alterar(cls, codf,funcionario2:model.Funcionario):
        listanova=[]
        linha=[]
        with open ('funcionarios.txt','r',encoding='utf-8') as arq:
            for i in arq:
                linha=i.split(',')
                if int(linha[5])==codf:
                    listanova.append(f"{funcionario2.nome},{funcionario2.tel},{funcionario2.cpf},{funcionario2.endereco},{funcionario2.idade},{linha[5]}")
                else:
                    listanova.append(i)
        with open('funcionarios.txt','w',encoding='utf-8' ) as arq:
            arq.writelines(listanova)

class FornecedorDal:
    @classmethod
    def cadastrar(cls,fornecedor:model.Fornecedor):
        linha=[]
        with open('fornecedores.txt','a',encoding='utf-8') as arq:
            with open('fornecedores.txt','r',encoding='utf-8') as arq2:
                for i in arq2:
                    linha=i.split(',')
                    print(linha)
            arq.write(f"{int(linha[0])+1},{fornecedor.nome}, {fornecedor.tel}, {fornecedor.cpf},  {fornecedor.endereco}, {fornecedor.idade}, {fornecedor.produtos}\n")
    
    @classmethod
    def remover(cls,codf):
        listanova=[]
        linha=[]
        with open('fornecedores.txt','r',encoding='utf-8') as arq:
            for i in arq:
                linha=i.split(',')
                if codf != int(linha[0]):
                    listanova.append(i)
        with open('fornecedores.txt','w',encoding='utf-8') as arq:
            arq.writelines(listanova)

    @classmethod
    def alterar(cls,codf,fornecedor2:model.Fornecedor):
        listanova=[]
        linha=[]
        with open('fornecedores.txt','r',encoding='utf-8') as arq:
            
            for i in arq:
                linha=i.split(',')    
                if codf==int(linha[0]) :
                    listanova.append(f"{fornecedor2.nome}, {fornecedor2.tel}, {fornecedor2.cpf},  {fornecedor2.endereco}, {fornecedor2.idade}, {fornecedor2.produtos}\n")
                else:
                    listanova.append(i)
        with open('fornecedores.txt','w',encoding='utf-8') as arq:
            arq.writelines(listanova)
class CategoriaDal:
    @classmethod
    def cadastrar(cls,categoria:model.Categoria):
        with open ('estoque.json','r',encoding='utf-8') as arq:
            categorias=json.loads(arq.read())
            categorias[categoria.nome]=[]

        with open ('estoque.json','w',encoding='utf-8') as arq:
            json.dump(categorias,arq, ensure_ascii=False)
    
    @classmethod
    def remover(cls,categoria:model.Categoria):
        with open ('estoque.json','r',encoding='utf-8') as arq:
            categorias=json.loads(arq.read())
            del categorias[categoria.nome]
        with open ('estoque.json','w',encoding='utf-8') as arq:
            json.dump(categorias,arq, ensure_ascii=False)

class ProdutoDal:
    @classmethod
    def cadastrar(cls,produto:model.Produto,categoria:model.Categoria):
        with open ('estoque.json','r',encoding='utf-8') as arq:
            categorias=json.loads(arq.read())
            categorias[categoria.nome].append({"nome_do_produto":produto.nome,'preco_do_arroz':produto.preco,"quantidade_estoque":produto.quantidade})

        with open ('estoque.json','w') as arq:
            json.dump(categorias,arq, ensure_ascii=False)

    @classmethod
    def remover(cls,nome,categoria:model.Categoria):
        with open ('estoque.json','r',encoding='utf-8') as arq:
            categorias=json.loads(arq.read())
            novosprdutos=[]
            for i in categorias[categoria.nome]:
                if nome != i["nome_do_produto"]:
                    novosprdutos.append(i)
            categorias[categoria.nome]=novosprdutos
        with open('estoque.json', 'w') as arq:
            json.dump(categorias, arq, ensure_ascii=False)   
    
    @classmethod
    def alterar(cls,produto1:model.Produto,produto2:model.Produto, categoria:model.Categoria):
        with open ("estoque.json",'r',encoding='utf-8') as arq:
            categorias=json.loads(arq.read())
            novosprodutos=[]
            for i in categorias[categoria.nome]:
                if produto1.nome== i["nome_do_produto"]:
                    novosprodutos.append({"nome_do_produto":produto2.nome,'preco_do_arroz':produto2.preco,"quantidade_estoque":produto2.preco})
                else:
                    novosprodutos.append(i)
            categorias[categoria.nome]=novosprodutos
        with open('estoque.json', 'w', encoding='utf-8') as arq:
            json.dump(categorias, arq, ensure_ascii=False)  

class CaixaDal():
    @classmethod
    def fechar(cls):   
        with open('relatorios.json','r',encoding='utf-8') as arq:
            dias=json.loads(arq.read())
            novo_dia=str(len(dias)+1)
            dias[novo_dia]=[{"codv": 0, "preco_do_produto": "preco", "quantidade_comprada": "quantidade", "nome_do_produto": "nome", "nome_do_cliente": "nome","codc":0}]
    
        with open('relatorios.json','w',encoding='utf-8') as arq:
            json.dump(dias,arq,ensure_ascii=False)

    @classmethod
    def vender(cls,nomeproduto,nomecliente):
        #cria um codigo de vendas novo(fusão do dia atual+quantidade de vendas do dia+1)
        with open('relatorios.json','r',encoding='utf-8') as arq:
            dias=json.loads(arq.read())
            dia_atual=str(len(dias))
            cod=len(dias[dia_atual])+1
            codv=str(dia_atual)+'x'+str(cod)
        #pega o codigo do cliente(sei que se tiver clientes com o mesmo nome vai dar problema, mas não achei pratico o usuario digitar o cod)
        with open('cliente.txt','r', encoding='utf-8') as arq:
            nome=nomecliente
            codc=''
            for i in arq:
                linha=i.split(',')
                if linha[0]==nome:
                    codc=linha[5]
        #remove produto do estoque e pega o preço
        with open('testecat.json','r',encoding='utf-8') as arq:
            preco_produto=0
            categorias=json.loads(arq.read())
            nome=nomeproduto
            for i in categorias:
                for j in categorias[i]:
                    if nome==j["nome_do_produto"]:
                        quantidade=int(j["quantidade_estoque"])
                        quantidade-=1
                        j["quantidade_estoque"]=quantidade
                        preco_produto=j["preco_do_produto"]
                        
            with open('testecat.json','w', encoding='utf-8') as arq:
                json.dump(categorias,arq,ensure_ascii=False)
        #adicona a venda no relatorio de vendas
        with open('relatorios.json','r',encoding='utf-8') as arq:
            dias=json.loads(arq.read())
            dia_atual=str(len(dias))
            dias[dia_atual].append({"codv": codv, "preco_do_produto": preco_produto, "quantidade_comprada": 1, "nome_do_produto": nomeproduto, "nome_do_cliente": nomecliente})
        with open('relatorios.json','w',encoding='utf-8') as arq:
            json.dump(dias,arq,ensure_ascii=False)
            #add a venda em melhores clientes 
        with open ('melhoresclientes.json','r',encoding='utf-8') as arq:
            melhores=json.loads(arq.read())
            tem=False
            with open ('melhoresclientes.json','r',encoding='utf-8') as arq2:
                novosmelhores=json.loads(arq2.read())
                nom=nomecliente
                for i, client in enumerate(novosmelhores):
                    data=client["nome"]
                    if data==nom:
                        melhores[i]['compras'].append('texte1')
                        tem=True      
                if tem==False:
                    melhores.append({"nome": nomecliente, "codc": codc, "compras": [codv]})
        with open ('melhoresclientes.json','w', encoding='utf-8') as arq:
            json.dump(melhores,arq,ensure_ascii=False)
        #add o produto em produtos mais vendidos
        with open ('melhoresprodutos.json','r',encoding='utf-8') as arq:
            nome=nomeproduto
            novomais=[]
            tem=False
            mais=json.loads(arq.read())
            for indexx,produto in enumerate(mais):
                if nome==produto['nome_do_produto']:
                    produto['cod_das_vendas'].append(codv)
                    novomais.append(produto)
                    tem=True
                else:
                    novomais.append(produto)
            if tem==False:
                novomais.append({"nome_do_produto": nomeproduto, "quantidade": 1, "cod_das_vendas": [codv]})
        with open ('melhoresprodutos.json','w', encoding='utf-8') as arq:
            json.dump(novomais,arq,ensure_ascii=False)

    
        








#n1=model.Produto("no2me",  "preco", "quantidade")
#n2=model.Produto("nomenovo",  "preco", "quantidade")
#ProdutoDal.alterar( n1 ,n2,model.Categoria("categoria1"))
#ClienteDal.alterar('vitor',model.Cliente('caio',9552,9985,'qno18',21))    
#ClienteDal.remover(3)
 



#ClienteDal.cadastrar(controller.Cliente('caio',9552,9985,'qno18',21,95))
#ClienteDal.cadastrar(controller.Cliente('keven',95552,94985,'qno17',2,9))
#ClienteDal.cadastrar(controller.Cliente('joão',952,995,'qno8',1,5))

#ClienteDal.remover(controller.Cliente('keven',95552,94985,'qno17',2,9))
#ClienteDal.alterar(controller.Cliente('keven',95552,94985,'qno17',2,9),controller.Cliente('joão',952,995,'qno8',1,5))

#FuncionarioDal.cadastrar(controller.Funcionario('caio',9552,9985,'qno18',21,95))
#FuncionarioDal.cadastrar(controller.Funcionario('keven',952,985,'qo18',1,9))
#FuncionarioDal.cadastrar(controller.Funcionario('Amorim',9,95,'q8',2,5))

#FuncionarioDal.remover(controller.Funcionario('Amorim',9,95,'q8',2,5))
#FuncionarioDal.alterar(controller.Funcionario('Amorim',9,95,'q8',2,5),controller.Funcionario('oliveira',9,95,'q8',2,5))
#FornecedorDal.cadastrar(controller.Fornecedor("Caio",9552,720456,'qno187',21,"Agua,suco,gelo,vento"))
#FornecedorDal.remover(controller.Fornecedor("Caio",9552,720456,'qno187',21,"Agua,suco,gelo,vento"))
#FornecedorDal.alterar(controller.Fornecedor("Caio",9552,720456,'qno187',21,"Agua,suco,gelo,vento"),controller.Fornecedor("keven",9552,720456,'qno187',21,"Agua,suco,gelo,vento"))

#ClienteDal.cadastrar(model.Cliente('caio',9552,9985,'qno18',21))
#ClienteDal.alterar(2,model.Cliente("João",9552,720,"Qno18",21))

#FuncionarioDal.cadastrar(model.Funcionario('caio',9552,9985,'qno18',21))
#FuncionarioDal.remover(6)
#FuncionarioDal.alterar(5,model.Funcionario('oliveira',9,95,'q8',2))
#FornecedorDal.cadastrar(model.Fornecedor("Caio",9552,720456,'qno187',21,"Agua,suco,gelo,vento"))
#FornecedorDal.alterar(7,model.Fornecedor("lindo",9552,720456,'qno187',21,"Agua,suco,gelo,vento"))
CaixaDal.fechar()