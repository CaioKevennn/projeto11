class Pessoas:
    def __init__(self,nome,tel,cpf,enderexo,idade):
        self.nome=nome
        self.tel=tel
        self.cpf=cpf
        self.endereco=enderexo
        self.idade=idade

class Cliente(Pessoas):
    def __init__(self, nome, tel, cpf, enderexo, idade):
        super().__init__(nome, tel, cpf, enderexo, idade)
        self.codc=0
        

class Funcionario(Pessoas):
    def __init__(self, nome, tel, cpf, enderexo, idade):
        super().__init__(nome, tel, cpf, enderexo, idade)
        self.codf=0

class Fornecedor(Pessoas):
    def __init__(self, nome, tel, cpf, enderexo, idade,produtos):
        super().__init__(nome, tel, cpf, enderexo, idade)
        self.produtos=produtos
        self.codf=0

class Categoria():
    def __init__(self,nome):
        self.nome=nome

class Produto():
    def __init__(self, nome,preco,quantidade):
        self.nome=nome
        self.preco=preco
        self.quantidade=quantidade

class Caixa():
    def __init__(self):
        pass



        


