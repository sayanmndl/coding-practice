class Logger:
    def __init__(self):
        self.next_allowed = {}

    def shouldPrintMessage(self, timestamp, message):
        if message not in self.next_allowed or timestamp >= self.next_allowed[message]:
            self.next_allowed[message] = timestamp+10
            return True

        return False