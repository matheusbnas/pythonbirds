class Pessoa: 
    def __init__(self, *filhos, nome, idade = 28): #Excutado quando constrói o objeto
        self.nome = nome
        self.idade = idade #tributo de uma instância(objeto)
        self.filhos = list(filhos) #atributo filhos que é uma lista

    def cumprimentar(self):# Método é uma função que pertence a uma classe. Portanto sempre está conectada a um objeto.
        return f'Olá, {id(self)} '


if __name__=='__main__':
    p = Pessoa(nome='Matheus') #p é uma variavel objeto(instância), Pessoa é uma classe

    #Atributo simples
    print(Pessoa.cumprimentar(p)) #executar o método cumprimentar. classe.método()
    print(id(p))
    print(p.cumprimentar()) # p é o objeto, cumprimentar é o método
    print(p.nome)
    p.nome = 'José'
    print(p.nome)
    print(p.idade)

    #Atributo Complexo. Objetos podem ser complexos
    joao = Pessoa(nome='João')
    natalia = Pessoa(joao, nome='Natália')

    print(Pessoa.cumprimentar(natalia))
    print(natalia.nome)
    print(natalia.idade)
    for filho in natalia.filhos:
        print(filho.nome)
        print(filho.idade)