class Cliente:
    def __init__(self,n, fone): #def é utilizada para a declaração de método.
        #A palavra reservada init é um metodo especial que sera chamado sempre que criar um objeto da classe
        #o parametro self é obrigatório, que esta presente em todos os métodos. Resumindo o parametro 'self' nesse momento, exporta as caracteristicas do objeto.

    #Para adicionar atributos a uma classe, basta definir o nome do atributo acompanhado da palavra reservada 'self', no método especial
    #Denominado '__init__' do Método Constructor
        self.nome = n
        self.telefone = fone

        return

        #pass #Utiliza-se a palavra reservada 'pass' quando nenhuma estrutura será definida no corpo dessa classe
