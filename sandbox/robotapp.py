from pynput import keyboard
import pygame
import os
 
class robotapp:
    keyarray = []

    def __init__(self):
        pass

    def esc(code):
        return f'\033[{code}m'
 
    def on_press(self, key):
        try:
            HORIZ=str(1)
            VERT=str(1)
            user_string='Ovladání: Kurzorové šipky ↑ ↓ → ← pro pohyb. ESC = konec'
            print("\033["+VERT+";"+HORIZ+"f"+user_string)
            VERT=str(2)
            user_string='========================================================'
            print("\033["+VERT+";"+HORIZ+"f"+user_string)
            if '{0}'.format(key) not in self.keyarray:                
                self.keyarray.append('{0}'.format(key))
                print(str(self.keyarray))            
        except AttributeError:
            if '{0}'.format(key) not in self.keyarray:                
                self.keyarray.append('{0}'.format(key))
                print(str(self.keyarray))
 
    def on_release(self, key):
        if '{0}'.format(key) not in self.keyarray:
            self.keyarray.remove('{0}'.format(key))
        print(str(self.keyarray))        
        if key == keyboard.Key.esc:
            # Stop listener
            os.system('cls' if os.name=='nt' else 'clear')
            print(str(self.keyarray))
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