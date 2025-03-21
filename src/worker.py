from abc import ABC, abstractmethod


class IWork(ABC):
    @abstractmethod
    def work(self):
        pass


class IEat(ABC):
    @abstractmethod
    def eat(self):
        pass


class HumanWorker(IWork, IEat):
    def work(self):
        print("Human worker working")

    def eat(self):
        print("Human worker eating")


class RobotWorker(IWork):
    def work(self):
        print("Robot worker working")


# Usage
human = HumanWorker()
robot = RobotWorker()

human.work()
human.eat()

robot.work()
