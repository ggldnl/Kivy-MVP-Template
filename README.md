# Simple Model-View-Presenter Counter App

This is a simple Model-View-Presenter (MVP) implementation of a counter app using the Kivy graphic library. The purpose of this app is to demonstrate the MVP architectural pattern and provide a basic example of how it can be applied.

## Table of Contents

- [Introduction](#introduction)
- [How It Works](#how-it-works)
- [License](#license)

## Introduction

The Model-View-Presenter is a design pattern used to separate the concerns of an application into three main components: 

- **Model**: Responsible for managing the data and business logic.
- **View**: Responsible for displaying the user interface and receiving user input.
- **Presenter**: Acts as a middleman between the Model and the View, handling user input and updating the Model and View accordingly.

This app implements a simple counter. The Model holds a variable and provides methods to increment and decrement it. The View is created using Kivy and consists of two buttons, one for incrementing and one for decrementing the variable, and a label to display its current value. The Presenter binds the Model and View together, ensuring that changes in the Model are reflected in the View and vice versa.

## How It Works

The Model contains a single integer variable `counter` and two methods:
- `increment()`: Increments the `counter` variable by 1.
- `decrement()`: Decrements the `counter` variable by 1.

The View is created using Kivy and consists of two buttons and one label. The buttons are bound to their respective callbacks (`increment_callback` and `decrement_callback`) and have a Signal object each (`increment_signal` and `decrement_signal`). The presenter connects to these signals and binds one of its methods to them. When a button is pressed, its callback is invoked. Inside the callback, the signal emits an event that is catched by the presenter (similar to what happens in the Observer pattern). The presenter then executes the method that binded to the signal that fired the event.

This way, the presenter can update the model. It can register the changes on the model and update the view accordingly.  

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify it as needed for your own projects.