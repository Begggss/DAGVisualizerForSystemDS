class Operation:

    def __init__(self, name,input,  output):
        self.name = name
        self.input = input
        self.output = output

    def get_name(self):
        return self.name
    def get_input(self):
        return self.input
    def add_input(self, input):
        self.input.append((input))
    def get_output(self):
        return self.output
