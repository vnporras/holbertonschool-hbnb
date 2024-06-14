#!/usr/bin/python3


class State:
    """A class representing a state in a finite state machine.

    Attributes:
        name (str): The name of the state.
        state (list): A list of child states.
    """

    def __init__(self, name):
        """Initializes a new State object.

        Args:
            name (str): The name of the state.
        """

        self.name = name
        self.state = []