from .context import Context

def component(*args, **kwargs):
    context = Context()
    identifier = None
    if 'identifier' in kwargs:
        identifier = kwargs['identifier']
    def wrap_get_instance(clazz):
        if identifier is None:
            component_name = clazz.__name__
        else:
            component_name = identifier
        def get_instance(*args, **kwargs):
            if not context.hasComponent(component_name):
                inst =  clazz(*args, **kwargs)
                context.register(component_name, inst)
            return context.getComponent(component_name)
        return get_instance
    return wrap_get_instance

def inject(*args, **kwargs):
    keyAsMap = [(item, item[0].lower() + item[1:]) for item in args] + [(key, kwargs[key]) for key in kwargs]
    def wrap_get_instance(clazz):
        context = Context()
        def get_instance(*args, **kwargs):
            inst = clazz(*args, **kwargs)
            for key, keyAs in keyAsMap:
                context.inject(inst,key,keyAs)
            return inst
        return get_instance
    return wrap_get_instance
