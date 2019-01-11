import bpy

#Get the object we're fixing up
obj = bpy.context.object
data = obj.data
materials = data.materials

#Save materials not associated with this process, overwrite old ones that are
matsToKeep = []
for mat in materials:
    if 'NikMat' not in mat.name:
        matsToKeep.append(mat)

materials.clear(update_data=True)
for mat in matsToKeep:
    materials.append(mat)

vertexColor = data.vertex_colors[0].data
i = 0
for f in obj.data.polygons:
    mat = materials[f.material_index].copy()me
    
    mat.name = ('NikMat' + str(f.index))
    col = 0
    for idx in f.loop_indices:
        col = vertexColor[i].color
        i += 1
    mat.specular_color = col
    obj.data.materials.append(mat)
    f.material_index = len(obj.data.materials)-1
