bl_info = {
    # required
    'name': 'Timer',
    'blender': (3, 6, 1),
    'category': 'Object',
    # optional
    'author': 'Netraj Patil',
    'description': 'A timer for blender',
}

import bpy
import datetime

flag = False

# == OPERATORS
class TimerOperator(bpy.types.Operator):
    
    bl_idname = 'opr.timer'
    bl_label = 'button'
    
    def execute(self, context):
        global flag
        global time1, time2
        if(flag == False):
            flag = True
            time1 = datetime.datetime.now()
            time2=0
        else:
            flag = False
            time2 = datetime.datetime.now()
        return {'FINISHED'}

# == PANELS
class TimerPanel(bpy.types.Panel):
    
    bl_idname = 'VIEW3D_TIMER'
    bl_label = 'Timer'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Timer"
    
    def draw(self, context):
        row = self.layout.row()    
        row.operator('opr.timer', text='start/stop')
        row1 = self.layout.row()
        global flag
        if(flag==True):
            row1.label(text = "press button to stop")
        if(flag==False):
            row1.label(text = "press button to start")
        row2 = self.layout.row()
        global time1
        global time2
        time = time2 - time1
        row2.label(text = str(time))

# == MAIN ROUTINE
CLASSES = [
    TimerOperator,
    TimerPanel,
]

def register():
    for klass in CLASSES:
        bpy.utils.register_class(klass)

def unregister():
    for klass in CLASSES:
        bpy.utils.unregister_class(klass)   

if __name__ == '__main__':
    register()