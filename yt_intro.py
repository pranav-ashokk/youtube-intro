import bpy
from bpy import *

#import Blender
#from Blender import *

from random import randint 

# Clear everything
scene = bpy.context.scene
scene.camera = None

for obj in scene.objects:
    if obj.type == 'MESH':
        obj.select_set(True)
    else:
        obj.select_set(False)
        

bpy.ops.object.delete()


# Create plane and background surface
bpy.ops.mesh.primitive_plane_add(location=(0, 0, 0))
plane = bpy.context.object
plane.dimensions = (800, 800, 0)
plane_mat = bpy.data.materials.new('plane_material')
plane_mat.diffuse_color = (0, 0, 0, 1)
plane.data.materials.append(plane_mat)

bpy.ops.mesh.primitive_cube_add(location=(-400, 0,200))
bpy.ops.transform.resize(value=(0, 400, 200))
bpy.ops.mesh.primitive_cube_add(location=(400, 0,200))
bpy.ops.transform.resize(value=(0, 400, 200))
bpy.ops.mesh.primitive_cube_add(location=(0, 400,200))
bpy.ops.transform.resize(value=(400, 0, 200))
bpy.ops.mesh.primitive_cube_add(location=(0, -400,200))
bpy.ops.transform.resize(value=(-400, 0, 200))

# Create the background animation (audio animation)
y_loc = -300

for rect_prism in range(150):
    y_loc+=4    
    rand = randint(1,20)
    bpy.ops.mesh.primitive_cube_add(location=(0, 2+y_loc,rand))
    bpy.ops.transform.resize(value=(2, 2, rand))
    
    # Assign colors randomly to audio animation (out of two different colors)
    prism = bpy.context.active_object
    randColor = randint(1,2)
    
    mat1 = bpy.data.materials.new('rect_material_1_' + str(rect_prism))
    mat2 = bpy.data.materials.new('rect_material_2_' + str(rect_prism))
    mat1.diffuse_color = (0, 255, 123, 1)
    mat2.diffuse_color = (0, 0, 0, 1)
    
    if(randColor==1):        
        prism.data.materials.append(mat1)
    
    else:        
        prism.data.materials.append(mat2)        