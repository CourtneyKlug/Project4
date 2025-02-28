from direct.showbase.ShowBase import ShowBase
from CollideObjectBase import *
from direct.task import Task
from panda3d.core import *
    
class Universe(InverseSphereCollideObject):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        super(Universe, self).__init__(loader, modelPath, parentNode, nodeName, Vec3(0, 0, 0), 0.9)
        self.modelNode.setPos(posVec) 
        self.modelNode.setScale (scaleVec)
        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath) 
        self.modelNode.setTexture(tex, 1)
    
    
class Planet(SphereCollideObject):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        super(Planet, self).__init__(loader, modelPath, parentNode, nodeName, Vec3(0, 0, 0), 1)
        self.modelNode.setPos(posVec) 
        self.modelNode.setScale (scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath) 
        self.modelNode.setTexture(tex, 1)

class SpaceStation(CapsuleCollidableObject):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        super(SpaceStation, self).__init__(loader, modelPath, parentNode, nodeName, 1, -1, 5, 1, -1, -5, 10) 
        self.modelNode.setPos(posVec) 
        self.modelNode.setScale (scaleVec)
        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath) 
        self.modelNode.setTexture(tex, 1)

class Drone(SphereCollideObject):
    # How many drones have been spawned.
    droneCount = 0

    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        super(Drone, self).__init__(loader, modelPath, parentNode, nodeName, Vec3(0, 0, 0), 1)
        self.modelNode.setPos(posVec) 
        self.modelNode.setScale (scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath) 
        self.modelNode.setTexture(tex, 1)
        
    