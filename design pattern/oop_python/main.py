from abc import ABCMeta, abstractmethod
from typing import override, ClassVar


class AbstractFlyBehavior(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass


class AbstractQuackBehavior(metaclass=ABCMeta):
    @abstractmethod
    def quack(self):
        pass


class FlyWithWings(AbstractFlyBehavior):
    def fly(self):
        print("Flying with wings")


class FlyNoWay(AbstractFlyBehavior):
    def fly(self):
        print("Flying No Way")


class Quack(AbstractQuackBehavior):
    def quack(self):
        print("Quacking")


class Squeak(AbstractQuackBehavior):
    def quack(self):
        print("Squeak")


class MuteQuack(AbstractQuackBehavior):
    def quack(self):
        print("MuteQuack")


class Duck:
    def __init__(self, fly_behavior: AbstractFlyBehavior, quack_behavior: AbstractQuackBehavior):
        self.fly_behavior = fly_behavior
        self.quack_behavior = quack_behavior

    def swim(self):
        print("swim duck")

    def display(self):
        print("display duck")

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()


class MallardDuck(Duck):
    fly_behavior: ClassVar[FlyWithWings] = FlyWithWings()
    quack_behavior: ClassVar[Quack] = Quack()

    def __init__(self):
        super().__init__(fly_behavior=self.fly_behavior, quack_behavior=self.quack_behavior)

    @override
    def display(self):
        print("display MallardDuck")


if __name__ == "__main__":
    d1 = MallardDuck()
    d1.perform_fly()
    d1.perform_quack()
