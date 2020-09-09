import hou

easings = ["bezier()", "linear()"]

current = hou.getPreference("anim.firstfunc.val")

try:
    index = easings.index(current)
except ValueError:
    index = -1

index = (index + 1) % len(easings)

newEasing = easings[index]
hou.setPreference("anim.firstfunc.val", newEasing)

hou.ui.setStatusMessage("Default Easing set to: %s" % easings[index])
