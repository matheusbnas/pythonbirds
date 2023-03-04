class Pessoa: 
    def __init__(self, nome, idade = 28): #Excutado quandoo constrói o objeto
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):# Método é uma função que pertence a uma classe. Portanto sempre está conectada a um objeto.
        return f'Olá, {id(self)} '


if __name__=='__main__':
    p = Pessoa('Matheus') #p é uma variavel objeto(instância), Pessoa é uma classe
    print(Pessoa.cumprimentar(p)) #executar o método cumprimentar. classe.método()
    print(id(p))
    print(p.cumprimentar()) # p é o objeto, cumprimentar é o método
    print(p.nome)
    p.nome = 'José'
    print(p.nome)
    print(p.idade)