class Singleton:
    """
    Singleton class that ensures only one instance of the class is created.

    Attributes:
    __instances (dict): A dictionary that keeps track of instances of the class created.

    Methods:
    __new__(cls): Creates a new instance of the class if it doesn't exist, otherwise returns the existing instance.
    Singleton(cls): Returns the existing instance of the class if it exists, otherwise creates a new instance and returns it.
    """

    __instances = {}

    def __new__(cls):
        """
        Creates a new instance of the class if it doesn't exist, otherwise returns the existing instance.

        Args:
        cls (class): The class to create an instance of.

        Returns:
        The existing instance of the class or a new instance of the class.
        """
        return cls.Singleton()

    @classmethod
    def Singleton(cls):
        """
        Returns the existing instance of the class if it exists, otherwise creates a new instance and returns it.

        Args:
        cls (class): The class to get or create an instance of.

        Returns:
        The existing instance of the class or a new instance of the class.
        """
        if cls not in Singleton.__instances:
            Singleton.__instances[cls] = super().__new__(Singleton)
        return Singleton.__instances[cls]

    @staticmethod
    def wrap(cls):
        """
        Decorator method that creates a new class that inherits from the original class and the Singleton class.

        Args:
        cls (class): The class to decorate.

        Returns:
        A new class that inherits from the original class and the Singleton class.
        """
        wrapped = type(cls.__name__, (cls, Singleton), {})

        return wrapped
