from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import requests
import mysql.connector
import json

class InputForm(GridLayout):
    def __init__(self, **kwargs):
        super(InputForm, self).__init__(**kwargs)
        self.cols = 2
        
        self.add_widget(Label(text='Table number:'))
        self.table_number = TextInput(multiline=False)
        self.add_widget(self.table_number)

        self.add_widget(Label(text='Command number:'))
        self.command_number = TextInput(multiline=False)
        self.add_widget(self.command_number)

        self.add_widget(Label(text='Chop title:'))
        self.chop_title = TextInput(multiline=False)
        self.add_widget(self.chop_title)

        self.add_widget(Label(text='Portion title:'))
        self.portion_title = TextInput(multiline=False)
        self.add_widget(self.portion_title)

        self.submit = Button(text="Submit")
        self.submit.bind(on_press=self.submit_data)
        self.add_widget(self.submit)

    # def create_json(self, instance):
    #     data = {
    #         'table_number': self.table_number.text,
    #         'command_number': self.command_number.text,
    #         'chop_title': self.chop_title.text,
    #         'portion_title': self.portion_title.text
    #     }
    #     json_data = json.dumps(data)
    #     print(json_data)

    def submit_data(self, instance):
        # Connect to the MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='alex',
            password='04082004Am#',
            database='germaniaApp'
        )

        # Prepare the data to be inserted
        data = {'tableNumer': self.table_number, 'isUsing': '1'}
        columns = ', '.join(data.keys())

        # Insert the data into the database
        cursor = connection.cursor()
        query = f"INSERT INTO tables (isUsing) VALUES ({self.table_number.text})"
        cursor.execute(query)
        connection.commit()
        cursor.close()
        connection.close()

class MyApp(App):
    def build(self):
        return InputForm()

if __name__ == '__main__':
    MyApp().run()
