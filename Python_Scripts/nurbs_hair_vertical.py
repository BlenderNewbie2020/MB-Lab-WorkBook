"""
Takes a series of vertical splines, adds a pre-existing bevel object, converts
them to NURBS, adjusted to use the endpoint, and changes the spline order and
resolution.
"""


import bpy
import os

ob = bpy.context.object
assert ob.type == 'CURVE' # throw error if it's not a curve

bpy.ops.object.mode_set(mode='OBJECT')

curve = ob.data
curve.bevel_object = bpy.data.objects['Hair_Bevel_Object']
curve.use_uv_as_generated = True

bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.curve.spline_type_set(type='NURBS')

for s in curve.splines:
    bpy.ops.curve.select_all(action='DESELECT')
    s.points[0].select = True
    s.use_endpoint_u = True
    s.order_u = 4
    s.resolution_u = 6
    if (s.points[0].co[2] < s.points[s.point_count_u-1].co[2]):
        bpy.ops.curve.switch_direction()

bpy.ops.curve.select_all(action='SELECT')
bpy.ops.transform.transform(mode='CURVE_SHRINKFATTEN', value=(0.1, 0, 0, 0), axis=(0, 0, 0), constraint_orientation='GLOBAL',
                            mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=0.03)
bpy.ops.curve.shade_smooth()

bpy.ops.object.mode_set(mode='OBJECT')

