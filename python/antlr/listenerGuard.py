class ListenerGuard:
    def __init__(self):
        self.stack = []

    def open_gate(self) -> None:
        self.stack.append(True)

    def close_gate(self) -> None:
        self.stack.append(False)

    def end_open_or_close(self) -> None:
        self.stack.pop()

    def is_gate_open(self) -> bool:
        return len(self.stack) > 0 and self.stack[-1]
