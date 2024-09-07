import py0d as zd

def install (reg):
    def instantiator (reg, owner, name, template_data):      
        name_with_id = zd.gensym ("?")
        return zd.make_leaf (name=name_with_id, owner=owner, instance_data=None, handler=handler)
    def handler (eh, msg):
        print (f"B got {msg.datum.srepr ()} on port {msg.port}")
    zd.register_component (reg, zd.Template ("Unit B", None, instantiator))

