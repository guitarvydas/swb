import py0d as zd

def install (reg):
    def instantiator (reg, owner, name, template_data):      
        name_with_id = zd.gensym ("?")
        return zd.make_leaf (name=name_with_id, owner=owner, instance_data=None, handler=handler)
    def handler (eh, msg):
        zd.send (eh, "f", zd.new_datum_int (42), msg)
    zd.register_component (reg, zd.Template ("Unit A", None, instantiator))

