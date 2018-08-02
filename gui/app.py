import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.label import Label


class GuessingGame(App):
    def build(self):
        return Label(text="Welcome to the Guessing Game!")

if __name__=='__main__':
    GuessingGame().run()
