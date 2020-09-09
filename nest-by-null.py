for node in hou.selectedNodes():
    
    if node.type().category().name() != "Object":
        continue
    
    # Make parent
    existing_parent = [conn.inputNode() for conn in node.inputConnections() if conn.inputIndex() == 0]
    existing_parent = existing_parent[0] if len(existing_parent) > 0 else None
    
    parent = node.createInputNode(0, "null", "%s_parent" % node.name())
    
    if existing_parent:
        parent.setInput(0, existing_parent)
    
    # Copy all parameters below Transform tab
    parms_orig = node.parmsInFolder(('Transform',))
    
    for parm_src in parms_orig:
        name = parm_src.name()        
        parm_dest = parent.parm(name)
        
        if parm_dest:        
            parm_dest.setFromParm(parm_src)
        
        # Reset
        parm_src.deleteAllKeyframes()
        parm_src.revertToDefaults()
        
    
    
    
        
