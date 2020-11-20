from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
#from matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

import random

matplotlib.use('module://kivy.garden.matplotlib.backend_kivy')

class GraphApp(App):

    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.title = 'Matplotlib graph on Kivy'

    def build(self):
        main_screen = BoxLayout()
        main_screen.orientation = 'vertical'

        label_text = 'The following is graph of Matplotlib'
        label = Label(text=label_text)
        label.size_hint_y = 0.2
        main_screen.add_widget(label)

        x = np.linspace(-np.pi, np.pi, 100)
        y = np.sin(x)

        fig, ax = plt.subplots()

        ax.plot(x,y)

        main_screen.add_widget(fig.canvas)

        return main_screen

def main():
    app = GraphApp()
    app.run()


if __name__ == '__main__':
    main()
