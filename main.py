from model import CounterModel
from view import CounterViewExtended
from presenter import CounterPresenter

if __name__ == '__main__':

    from kivy.base import runTouchApp

    # Create the view
    view = CounterViewExtended()

    # Create an instance of the model
    model = CounterModel()

    # Create an instance of the presenter
    presenter = CounterPresenter(view, model)

    # Run the Kivy app
    runTouchApp(view)
