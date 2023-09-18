class CounterPresenter:
    def __init__(self, view, model):
        self.view = view
        self.model = model

        self.view.increment_signal.connect(self.increment)
        self.view.decrement_signal.connect(self.decrement)

    def increment(self):
        self.model.increment()
        # print(f'Incremented to {self.model.value}')
        self.view.value_label.text = str(self.model.value)

    def decrement(self):
        self.model.decrement()
        # print(f'Decremented to {self.model.value}')
        self.view.value_label.text = str(self.model.value)
