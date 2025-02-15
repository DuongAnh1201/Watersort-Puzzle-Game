from random import shuffle
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
        return self.stack
    def pop(self):
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]
    def size(self):
        return len(self.stack)
    def empty(self):
        return len(self.stack) == 0
    def set(self):
        self.stack = set(self.stack)
        return self.stack
    def show(self):
        return self.stack

class Game:
    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()
        self.stack_3 = Stack()
        self.color=["R","G","B"]*3
        self.stacked = [self.stack_1, self.stack_2, self.stack_3]
    def initialize(self):
        shuffle(self.color)
        for i in range(len(self.color)):
            if i%3==0:
                self.stack_1.push(self.color[i])
            if i%3==1:
                self.stack_2.push(self.color[i])
            if i%3==2:
                self.stack_3.push(self.color[i])
    def start(self):
        self.initialize()
        print(f"Stack 1: {self.stack_1.show()}")
        print(f"Stack 2: {self.stack_2.show()}")
        print(f"Stack 3: {self.stack_3.show()}")
    def show(self):
        print(f"Stack 1: {self.stack_1.show()}")
        print(f"Stack 2: {self.stack_2.show()}")
        print(f"Stack 3: {self.stack_3.show()}")
    def submit(self):
        self.stack_1=self.stack_1.set()
        self.stack_2=self.stack_2.set()
        self.stack_3=self.stack_3.set()
        if len(self.stack_1) == len(self.stack_2) == len(self.stack_3)==1:
            return "Good game!"
        else:
            return "Bad game!"
    def move(self):
        self.start()
        #Type it by stack_n, stack_n
        while True:
            n = input(f"You can only move the last color of each row.\n Please type in which item you want to pick and type in which row you want to move in: ").split(",")
            if n == ["0"]:
                print(self.submit())
            if n!= ["0"]:
                m = [int(x) for x in n]
                move_color=self.stacked[m[0]-1].pop()
                self.stacked[m[1]-1].push(move_color)
                self.show()

if __name__ == "__main__":
    game = Game()
    game.move()




