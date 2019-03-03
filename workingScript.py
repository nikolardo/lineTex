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

#vertexColor is an array of vertex colors
vertexColor = data.vertex_colors[0].data
i = 0
# for each face of the polygon
for f in obj.data.polygons:
    # copy the existing material
    mat = materials[f.material_index].copy()me
    # give it an appropriate name
    mat.name = ('NikMat' + str(f.index))
    col = 0
    # for each vertex
    # color = vertexColor[i]
    for idx in f.loop_indices:
        col = vertexColor[i].color
        i += 1
    # set that color to the specular color
    mat.specular_color = col
    # add it as a material
    obj.data.materials.append(mat)
    # set the current face to use that material
    f.material_index = len(obj.data.materials)-1
