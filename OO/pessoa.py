class Pessoa: 
    def cumprimentar(self):# Método é uma função que pertence a uma classe. Portanto sempre está conectada a um objeto.
        return f'Olá, {id(self)} '


if __name__=='__main__':
    p = Pessoa() #p é um objeto, Pessoa é uma classe
    print(Pessoa.cumprimentar(p)) #executar o método cumprimentar
    print(id(p))
    print(p.cumprimentar())