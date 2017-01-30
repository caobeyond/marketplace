def singleton(clazz):
    instances = {}
    def get_instance():
        if clazz not in instances:
            instances[clazz] = clazz()
        return instances[clazz]
    return get_instance

@singleton
class Context:
    def __init__(self):
        self.components = {}
    def register(self, key, instance):
        self.components[key] =  instance
    def hasComponent(self, key):
        return key in self.components
    def getComponent(self,key):
        return self.components[key]
    def inject(self, other, key, keyAs):
        component = self.getComponent(key)
        setattr(other, keyAs,component)
