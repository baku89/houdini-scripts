lock_parms = ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz', 'px', 'py', 'pz', 'prx', 'pry', 'prz', 'projection', 'focal', 'aperture']

for node in hou.selectedNodes():

    if node.type().name() != "cam":
        continue
    
    
    is_locked = node.parm('tx').isLocked()
    val = not is_locked
    
    for parm in lock_parms:
        node.parm(parm).lock(val)
    
    node.setComment("Locked" if val else "")
    
    
    
