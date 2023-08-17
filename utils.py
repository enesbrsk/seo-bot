from stem import Signal
from stem.control import Controller

port = 9151

def ip_switch():
    try:
        with Controller.from_port(port=port) as controller:
            controller.authenticate()
            controller.signal(Signal.NEWNYM)
            print("Identity Switched.")
    except Exception as i:
        print("Unable to switch Identity: {0}".format(i))

