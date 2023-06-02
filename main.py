class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

    def minusFunc(self, num):
        return self.result - num

    def upstreamTest(self):
        return "업스트림 테스트"