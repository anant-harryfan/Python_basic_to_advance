import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title="**Please drink water NOW!!",
            message="The National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: Audio 15.5 cups (3.7 liters) of fluids for men. Audio 11.5 cups (2.7 liters) of fluids a day for women.",
            app_icon="C:\\Users\\xyz\\PycharmProjects\\PythonTuts\\Python_Practise\\Practise11_glass.ico",
            timeout=5
        )
        time.sleep(60*60)