class InvalidTextSubmissionException(Exception):
    """
    Exception raised when text submissions violate the rules.

    Attributes:
        expression: invalid text submission
        message: explanation of invalidity
    """

    def __init__(self, expression: str, message: str):
        self.expression = expression
        self.message = message
