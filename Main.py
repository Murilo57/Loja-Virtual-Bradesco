class Main:
    pass  #Como a classe main não possui atributos passo a palavra reservada pass para o objeto.

print("Testando o projeto")

#Comando para importar classe (from chama a classe e import chama o arquivo da classe).
from Cliente import Cliente
from Conta import Conta

#Instanciando um Novo Objeto, passo o nome da classe instanciada no caso a classe "CLIENTE"
c1 = Cliente("Muliro","9977070-7070")
conta = Conta(c1.nome,3232,0)

print (c1)
print(c1.nome, " e ", c1.telefone)
print(conta.titular, " Numero: ", conta.numero, "Saldo: ", conta.saldo)

