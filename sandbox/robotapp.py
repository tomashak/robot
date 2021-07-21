from pynput import keyboard
import os
 
class robotapp:
    def __init__(self):
        pass
 
    def on_press(self, key):
        try:
            HORIZ=str(2)
            VERT=str(2)
            user_string='XXX'
            print("\033["+VERT+";"+HORIZ+"f"+user_string)
            print('alphanumeric key {0} pressed'.format(
                key.char))
        except AttributeError:
            print('special key {0} pressed'.format(
                key))
 
    def on_release(self, key):
        print('{0} released'.format(
            key))
        if key == keyboard.Key.esc:
            # Stop listener
            return False
 
    # Collect events until released
    def main(self):
        with keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release) as listener:
            listener.join()
 
    def start_listener(self):
        keyboard.Listener.start
        self.main()
 
if __name__ == '__main__':
    os.system('cls' if os.name=='nt' else 'clear')
    ck = robotapp()
    ck.start_listener()