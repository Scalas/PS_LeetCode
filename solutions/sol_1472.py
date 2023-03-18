class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = homepage
        self.backward_history = []
        self.forward_history = []

    def visit(self, url: str) -> None:
        self.backward_history.append(self.current)
        self.forward_history = []
        self.current = url

    def back(self, steps: int) -> str:
        while steps and self.backward_history:
            self.forward_history.append(self.current)
            self.current = self.backward_history.pop()
            steps -= 1
        return self.current

    def forward(self, steps: int) -> str:
        while steps and self.forward_history:
            self.backward_history.append(self.current)
            self.current = self.forward_history.pop()
            steps -= 1
        return self.current
