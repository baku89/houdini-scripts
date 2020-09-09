def setCameraVisibility(cam, flag):
    if cam.isInsideLockedHDA():
        return
        
    # Check if the camera has the mandantory spare parameters, if not, add them to it
    if cam.parm('soho_viewport_menu') == None:
        viewport_menu = hou.properties.parmTemplate('viewport', 'soho_viewport_menu')
        parm_group = cam.parmTemplateGroup()
        folder = parm_group.findFolder('Transform')
        folder.addParmTemplate(viewport_menu)
        parm_group.appendToFolder('Transform', viewport_menu)
        cam.setParmTemplateGroup(parm_group)
    
        
    cam.parm('soho_viewport_menu').set(flag)

def getCurrentNetworkEditorPane():
    editors = [pane for pane in hou.ui.paneTabs() if isinstance(pane, hou.NetworkEditor) and pane.isCurrentTab() and pane.pwd().path().startswith("/obj")]
    
    if len(editors):
        return editors[0]
    
pane = getCurrentNetworkEditorPane()

if pane:
    node = pane.pwd()
    
    # Hide all cameras at first
    for cam in hou.node('/').recursiveGlob('*', hou.nodeTypeFilter.ObjCamera):
        setCameraVisibility(cam, False)
       
    # Unhide cameras below the pwd node
    for cam in node.recursiveGlob('*', hou.nodeTypeFilter.ObjCamera):
        setCameraVisibility(cam, True)
    
