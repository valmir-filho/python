"""
The following code could use a bit of object-oriented artistry.
While it's a simple method and works just fine as it is, in a larger
system it's best to organize methods into classes/objects. (Or, at least, something similar depending on your language)

Refactor the following code so that it belongs to a Person class/object.
Each Person instance will have a greet method. The Person instance should be
instantiated with a name so that it no longer has to be passed into each greet method call.

Here is how the final refactored code would be used:

joe = Person('Joe')
joe.greet('Kate') # should return 'Hello Kate, my name is Joe'
joe.name          # should == 'Joe'
"""


class Person:
  """
  Represents a person who can introduce themselves.
  """
  def __init__(self, name):
    """
    Initializes a new Person instance.

    Args:
      name (str): The name of the person.
    """
    self.name = name

  def greet(self, your_name):
    """
    Greets another person by name.

    Args:
      your_name (str): The name of the person to greet.

    Returns:
      str: The formatted greeting message.
    """
    return "Hello %s, my name is %s" % (your_name, self.name)

# Example Usage:

# 1. Instantiate the Person object with a name
joe = Person('Joe')

# 2. Access the name attribute directly
# This will output: 'Joe'
print(joe.name)

# 3. Call the greet method on the instance
# This will output: 'Hello Kate, my name is Joe'
print(joe.greet('Kate'))

# Another example
sally = Person('Sally')
print(sally.greet('Fred')) # Outputs: 'Hello Fred, my name is Sally'
