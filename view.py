from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from signal import Signal


class CounterViewExtended(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        self.value_label = Label()
        self.add_widget(self.value_label)

        button_layout = BoxLayout()

        increment_button = Button(text='Increment')
        self.increment_signal = Signal()
        increment_button.bind(on_press=self.increment_callback)
        button_layout.add_widget(increment_button)

        decrement_button = Button(text='Decrement')
        self.decrement_signal = Signal()
        decrement_button.bind(on_press=self.decrement_callback)
        button_layout.add_widget(decrement_button)

        self.add_widget(button_layout)

    def increment_callback(self, instance):
        self.increment_signal.emit()

    def decrement_callback(self, instance):
        self.decrement_signal.emit()


class CounterApp(App):
    def build(self):
        return CounterViewExtended()
