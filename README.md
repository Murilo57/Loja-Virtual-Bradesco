# Orientação a Objetos com Python
curso de Orientação a Objetos com Python da Fundação Bradesco

****
08/09/2023
**Definindo Nomenclatura para Elementos de um Projeto**

Classes:
- Referente a caracteres, seguir o mesmo padrão de variaveis e objetos.
- Sempre iniciar as classes com caracteres maiúsculos, inclusive as iniciais de nomes compostos:
- Exemplo MinhaClasse()

Variaveis e/ou Objetos:
- Utilizar somente caracteres e letras minúsculas.
- No caso de variáveis com nome composto, utilizar o underline para sepração das palavras.
- Não iniciar o nome com números(podemos utilizar numeros no nome, mas não devemos iniciar com eles).
- Não utilizar caracteres especiais.
- Não utilizar espaçamento em branco.
- Evitar utilizar os caracteres I e O.

Pacotes, Módulos e Métodos:
- Utilizar nomes pequenos.
- Utilizar semrpe caracteres minúsculos.
- Utilizar o underline para unir nomes compostos.

**Declaração dos Membros da Classe**

Atributos (Propriedades):
- Os atributos armazenam as caracteristicas de uma classe.
- Os atributos são as declarações de variaveis da classe.

Métodos:
- São ações da classe, suas funções.
- Representam os estados e ações dos objetos quando instanciados.

**Método Construtor**

- É definido de forma implicita ou explicita por todas as classes, é utilizado para construir o objeto.

**Em Python não é recomendável criar mais de um Método Construtor para a classe**


****

**Encapsulamento de Dados**
 O conceito de encapsulamento de dados torna-se essencial, pois envolve a protreção dos atributos ou métodos de uma classe.

 Esse concenito garante a integridade das informações e também facilita a utilização das implementações.
****

**Métodos de Aceso(Get e Set)**

- Get: O método Get é utilizado para ler os valroes internos do objeto e envia-los como valor de retorno da função.
    Sintaxe: get_nome do atributo()
        Exemplo: get_idade(self): return self._idade

- Set: O método Set recebe argumentos que serão atribuidos a membros internos do objeto.
    Sintaxe: set_nome do atributo(valor do parâmetro)
        Exemplo: def set_idade(self,valor): self.idade = valor

Encapsular os dados de uma classe é muito importante, pois deixa seu sistema organizado para possivel mudanças.
****

**Protocolo de Descritores - Decorator**

Um decorator é um padrão de projeto de software que permite adicionar comportamento a um objeto ja existente, em tempo de execução, ou seja, agrega, de forma dinânimca, responsabilidades adicionais a um objeto.

Na prática, o decorator permite que atributos de uma classe tnham responsabilidades.

Um decorator é um objeto invocável, uma função que aceita outra função como parâmetro(a função decorada).

O decorator pode realizar algum processamento com a função decorada e devolê-la ou substitui-la por outra função.

**@Property**

Python traz outra solução para manter os atributos privados, conhecida como Property.
*A função Property é um Decorator e é utilizada para obter um valor de um atributo.*
Baicamente, a função Property permite que você declare uma função para obter o valor de um atributo.

****
