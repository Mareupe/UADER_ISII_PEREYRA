from __future__ import annotations
from abc import ABC
from textblob import TextBlob
import msvcrt

class Mediator(ABC):
    """
    The Mediator interface declares a method used by components to notify the
    mediator about various events. The Mediator may react to these events and
    pass the execution to other components.
    """

    def notify(self, sender: object, event: str) -> None:
        pass


class ConcreteMediator(Mediator):
    def __init__(self, component1: Component1, component2: Component2) -> None:
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def notify(self, sender: object, event: str) -> None:
        if event == "A":
            eb=TextBlob("Mediator reacts on A and triggers following operations:")
            print(eb.translate(from_lang="en", to="es"))
            self._component2.do_c()
        elif event == "D":
            eb=TextBlob("Mediator reacts on D and triggers following operations:")
            print(eb.translate(from_lang="en", to="es"))
            self._component1.do_b()
            self._component2.do_c()


class BaseComponent:
    """
    The Base Component provides the basic functionality of storing a mediator's
    instance inside component objects.
    """

    def __init__(self, mediator: Mediator = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator


"""
Concrete Components implement various functionality. They don't depend on other
components. They also don't depend on any concrete mediator classes.
"""


class Component1(BaseComponent):
    def do_a(self) -> None:
        eb=TextBlob("Component 1 does A.")
        print(eb.translate(from_lang="en", to="es"))
        self.mediator.notify(self, "A")

    def do_b(self) -> None:
        eb=TextBlob("Component 1 does B.")
        print(eb.translate(from_lang="en", to="es"))
        self.mediator.notify(self, "B")


class Component2(BaseComponent):
    def do_c(self) -> None:
        eb=TextBlob("Component 2 does C.")
        print(eb.translate(from_lang="en", to="es"))
        self.mediator.notify(self, "C")

    def do_d(self) -> None:
        eb=TextBlob("Component 2 does D.")
        print(eb.translate(from_lang="en", to="es"))
        self.mediator.notify(self, "D")


if __name__ == "__main__":
    # The client code.
    c1 = Component1()
    c2 = Component2()
    mediator = ConcreteMediator(c1, c2)

    eb=TextBlob("Client triggers operation A.")
    print(eb.translate(from_lang="en", to="es"))
    c1.do_a()

    print("\n", end="")

    eb=TextBlob("Client triggers operation D.")
    print(eb.translate(from_lang="en", to="es"))
    c2.do_d()

msvcrt.getch()