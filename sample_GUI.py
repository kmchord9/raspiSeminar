#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import numpy as np
import matplotlib.pyplot as plt
import datetime
import random
from module.csvModule import fileExistCheckAndSaveCsv
from module.sensor import getADT7410SensorData

#設定値
SAVE_CYCLE_TIME = 20
SAVE_PATH = "./datalog/"
MAX_SHOW_ELEMENT_N = 540

kv_def = '''
<RootWidget>:
    orientation: 'vertical'

    Label:
        text: 'The following is a graph of Matplotlib'
        size_hint_y: 0.2

    GraphView:

<GraphView>:
'''
Builder.load_string(kv_def)

def randomTemp():
    return random.random()*25

class GraphView(BoxLayout):
    """Matplotlib のグラフを表示するためのウィジェット"""

    def __init__(self, *args, **kwargs):

        self.dt_now = datetime.datetime.now()
        #self.xVal = np.array([ self.dt_now + datetime.timedelta(seconds=t) for t in range(6) ])
        #self.yVal = np.array([randomTemp() for i in range(6)])  
         
        self.xVal = np.array([ self.dt_now ])
        self.yVal = np.array([randomTemp()])  
        super().__init__(*args, **kwargs)

        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot(self.xVal, self.yVal)

        widget = FigureCanvasKivyAgg(self.fig)
        self.add_widget(widget)

        Clock.schedule_interval(self.update_view, SAVE_CYCLE_TIME)

    def update_view(self, *args, **kwargs):

        self.dt_now = datetime.datetime.now()
        self.tm_now = getADT7410SensorData()

        if self.xVal.size > MAX_SHOW_ELEMENT_N: 
            self.xVal = np.roll(self.xVal, -1)
            self.yVal = np.roll(self.yVal, -1)

            self.xVal[-1] = self.dt_now
            self.yVal[-1] = self.tm_now

        else:

            self.xVal = np.append(self.xVal, self.dt_now)
            self.yVal = np.append(self.yVal, self.tm_now)

        #今日の日付のCSVファイルの存在を確認してデータ保存
        if not fileExistCheckAndSaveCsv(self.dt_now, self.tm_now):
            self.xVal = np.array([]) #日付が更新されたら表示される要素を初期化
            self,yVal = np.array([])    

        #saveCSV(self.dt_now, self.tm_now, save_path=SAVE_PATH)


        # Line にデータを設定する
        self.line.set_data(self.xVal, self.yVal)
        # グラフの見栄えを調整する
        self.ax.relim()
        self.ax.autoscale_view()
        # 再描画する
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

class RootWidget(BoxLayout):
    """子を追加していくためのウィジェットを用意しておく"""


class GraphApp(App):
    """Matplotlib のグラフを表示するアプリケーション"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = 'Matplotlib graph on Kivy'

    def build(self):
        return RootWidget()


def main():
    # アプリケーションを開始する
    app = GraphApp()
    app.run()


if __name__ == '__main__':
    main()
