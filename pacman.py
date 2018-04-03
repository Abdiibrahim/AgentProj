from entities import DynamicEntity


class PacMan(DynamicEntity):
    def __init__(self, node, ownerID):
        DynamicEntity.__init__(self, node)
        self.color = (255, 255, 0)
        # self.agentibelcongto = # tie this to the id of the agent this target is tied to
        self.owner = ownerID
        
    def update(self, dt):
        #self.position += self.direction*self.speed*dt
        self.setPosition()
