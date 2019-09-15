import abc


class BaseProblem(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_name(self):
        return

    @abc.abstractmethod
    def solve(self):
        return

    @abc.abstractmethod
    def show(self):
        return

    @abc.abstractmethod
    def test(self):
        return

    @abc.abstractmethod
    def define(self):
        return

    @abc.abstractmethod
    def detail(self):
        return
