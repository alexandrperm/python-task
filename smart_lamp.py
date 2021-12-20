#программа для удалённого управления "умным" ночником
#через http-api
#доступные команды:
# /on?bright=X - включение на яркости X (0-100%)
# /off - выключение
# /status - получение статуса в формате json

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.clock import Clock
import json
from kivy.uix.boxlayout import BoxLayout
import requests


class MainApp(App):
    def build(self):
        #создаём слайдер для регулировки яркости
        self.brightnessControl = Slider(min=0, max=100, value=50)
        self.brightnessControl.bind(value=self.on_value_change)

        #создаём кнопку включения ночника
        button_on=Button(text='Включить',
                         background_color='green')
        button_on.bind(on_press=self.on_press_button)
        # создаём кнопку выключения ночника
        button_off = Button(text='Выключить',
                           background_color='red')
        button_off.bind(on_press=self.off_press_button)

        self.connect_label = Label(text='Не подключено')
        self.label_temp = Label(text ='Температура')
        self.temp = Label(text ='---')

        #формируем интерфейс
        HB = BoxLayout(orientation='horizontal')
        HB.add_widget(self.connect_label)
        HB.add_widget(self.label_temp)
        HB.add_widget(self.temp)

        HB1 = BoxLayout(orientation='horizontal')
        HB1.add_widget(Label(text ='Яркость'))
        HB1.add_widget(self.brightnessControl)

        HB2 = BoxLayout(orientation='horizontal')
        HB2.add_widget(button_on)
        HB2.add_widget(button_off)
        VB = BoxLayout(orientation='vertical')
        VB.add_widget(HB)
        VB.add_widget(HB1)
        VB.add_widget(HB2)

        #таймер для периодического опроса
        Clock.schedule_interval(self.timer, 1)

        #переменные для хранения статуса
        self.connection_status = 0
        self.state = 0
        self.brigthnes = 0
        self.temperature = 0
        return VB

    def on_press_button(self, instance):
        print('Вы нажали на кнопку Включения!')
        print(round(self.brightnessControl.value))
        if(self.connection_status==1):
            resp = requests.get('http://192.168.0.109/on?bright=' + str(round(self.brightnessControl.value)))

    def off_press_button(self, instance):
        print('Вы нажали на кнопку Выключения!')
        if (self.connection_status==1):
            resp = requests.get('http://192.168.0.109/off')

    def on_value_change(self, instance, value):
        print('Вы переместили слайдер!',self.brightnessControl.value)
        if (self.state == 1 and self.connection_status==1):
            resp = requests.get('http://192.168.0.109/on?bright=' + str(round(self.brightnessControl.value)))

    def timer(self, dt):
            try:
                resp = requests.get('http://192.168.0.109/status', timeout=1);
                if (resp.status_code == 200):
                    data = json.loads(resp.content)
                    self.state = data['state']
                    self.brigthnes = data['brigth']
                    self.temperature = (data['temperature'])

                    self.brightnessControl.value = self.brigthnes
                    self.temp.text = str(self.temperature / 10)
                    self.connection_status = 1
                    self.connect_label.text = 'Подключено'
                else:
                    print('заяц недоступен')
                    self.connection_status = 0
                    self.connect_label.text = 'Не подключено'
            except requests.exceptions.RequestException as e:
                print(e)
                self.connection_status = 0
                self.connect_label.text = 'Не подключено'






if __name__ == '__main__':
    app = MainApp()
    app.run()