from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
 
class MyApp(ShowBase):
 
    def __init__(self):
        ShowBase.__init__(self)

        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(0.005, 0.005, 0.005)
        self.pandaActor.reparentTo(self.render)
        self.pandaActor.loop("walk")

        self.camera.setPos(20, -30, 3)
 
base = MyApp()
base.run()