import threading
from threading import Thread

def relay():
    execfile("RelayCode.py")
    
def music():
    execfile("MusicCode.py")

if __name__ == '__main__':
    Thread(target = relay).start()
    Thread(target = music).start()
