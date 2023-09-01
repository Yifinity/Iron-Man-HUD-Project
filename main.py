from App import *

def main():
    # Create a new app instance 
    app = App()

    while(True):
        app.onStep()
        app.redrawAll()
        app.onKeyPress()

main()
