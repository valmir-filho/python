"""
Special Methods, Magic Methods ou Dunder Methods no Python.

No Python, os "Special Methods," também conhecidos como "Magic Methods" ou "Dunder Methods" (abreviação de "Double Underscore Methods"), são métodos especiais que
têm nomes que começam e terminam com dois sublinhados duplos, como "__init__", "__str__", "__add__", entre outros. Esses métodos especiais são usados para definir
comportamentos específicos para classes e objetos. Eles não são chamados diretamente como métodos normais, mas Python os invoca automaticamente em resposta a
operações específicas.

Aqui estão alguns exemplos de "Special Methods" e suas finalidades:

- "__init__": este método é chamado quando um objeto é criado a partir da classe e é usado para inicializar atributos e estados do objeto.

- "__str__": este método é chamado quando você usa a função "str()" em um objeto e é usado para retornar uma representação de string legível para humanos do objeto.

- "__repr__": este método é chamado quando você usa a função "repr()" em um objeto e é usado para retornar uma representação de string que deve ser suficientemente
precisa para reconstruir o objeto.

- "__add__", "__sub__", "__mul__", "__truediv__", etc.: esses métodos são usados para sobrecarregar operadores matemáticos, permitindo que você defina o
comportamento desses operadores para objetos da sua classe.

- "__len__": este método é usado para determinar o tamanho de um objeto, como uma lista, quando você usa a função "len()".

- "__getitem__", "__setitem__": esses métodos são usados para acessar e modificar elementos de um objeto, como um dicionário, usando a notação de colchetes.

- "__call__": este método permite que um objeto seja chamado como uma função, tornando o objeto "invocável".

- "__eq__", "__ne__", "__lt__", "__gt__", etc.: esses métodos são usados para sobrecarregar operadores de comparação, permitindo que você defina o comportamento
desses operadores para objetos da sua classe.

- "__enter__", "__exit__": esses métodos são usados em contextos de gerenciamento de recursos (usando a instrução "with").

Esses são apenas alguns exemplos dos muitos "Special Methods" disponíveis no Python. Usando esses métodos especiais, você pode personalizar o comportamento das
suas classes e objetos, tornando-os mais poderosos e flexíveis. Eles são uma parte fundamental da linguagem Python e são amplamente utilizados na construção de
classes personalizadas.
"""
