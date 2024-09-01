import py0d as zd

def main ():
    arg_array = zd.parse_command_line_args ()
    root_project = arg_array [0] 
    root_0D = arg_array [1]
    arg = arg_array [2]
    main_container_name = arg_array [3]
    diagram_names = arg_array [4]
    palette = zd.initialize_component_palette (root_project, root_0D, diagram_names, components_to_include_in_project)
    zd.run (palette, root_project, root_0D, arg, main_container_name, diagram_names, start_function,
              show_hierarchy=False, show_connections=False, show_traces=False, show_all_outputs=False)

def start_function (root_project, root_0D, arg, main_container):
    arg = zd.new_datum_string (arg)
    msg = zd.make_message("", arg)
    zd.inject (main_container, msg)

def components_to_include_in_project (root_project, root_0D, reg):
    # due to the simplicity of this example, I've put all 3 components into this file
    # App1 ignores "Unit C"
    # App2 ignores "Unit B"
    # both apps use "Unit A" - which outputs a value (42) without needing to know what the actual receivers are
    # "Unit A" is used - without modification - in both apps
    # in larger projects, one would include only the Leaf code that is needed for a project
    # (or use something like m4 to include Leaf code blocks)
    unitA (reg)
    unitB (reg)
    unitC (reg)

def unitA (reg):
    zd.register_component (reg, zd.Template ("Unit A", None, unitA_instantiator))
def unitA_instantiator (reg, owner, name, template_data):      
    name_with_id = zd.gensym ("?")
    return zd.make_leaf (name=name_with_id, owner=owner, instance_data=None, handler=unitA_handler)
def unitA_handler (eh, msg):
    zd.send (eh, "f", zd.new_datum_int (42), msg)

def unitB (reg):
    zd.register_component (reg, zd.Template ("Unit B", None, unitB_instantiator))
def unitB_instantiator (reg, owner, name, template_data):      
    name_with_id = zd.gensym ("?")
    return zd.make_leaf (name=name_with_id, owner=owner, instance_data=None, handler=unitB_handler)
def unitB_handler (eh, msg):
    print (f"B got {msg.datum.srepr ()} on port {msg.port}")

def unitC (reg):
    zd.register_component (reg, zd.Template ("Unit C", None, unitC_instantiator))
def unitC_instantiator (reg, owner, name, template_data):      
    name_with_id = zd.gensym ("?")
    return zd.make_leaf (name=name_with_id, owner=owner, instance_data=None, handler=unitC_handler)
def unitC_handler (eh, msg):
    print (f"C got {msg.datum.srepr ()} on port {msg.port}")

main ()
