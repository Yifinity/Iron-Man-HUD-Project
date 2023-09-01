# Our scene that runs after the startup scene
class RunScene:
    def __init__(self, app):
        # take in our app object to get it's local variables
        self.app = app


    def onStep(self):
        self.app.userScreen.onStep()

    def redrawAll(self):
        frame = self.app.userCamera.getFrame()
        self.app.userScreen.redrawAll(frame)
