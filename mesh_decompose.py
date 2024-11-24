# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/1d_mesh_decompose

from bpy.props import FloatProperty
from bpy.types import Operator, Panel, Scene
from bpy.utils import register_class, unregister_class

bl_info = {
    "name": "Knife Imprint",
    "description": "Shifts all selected objects to offset by Z-axis",
    "author": "Nikita Akimov, Paul Kotelevets",
    "version": (1, 0, 0),
    "blender": (2, 79, 0),
    "location": "View3D > Tool panel > 1D > Knife Imprint",
    "doc_url": "https://github.com/Korchy/1d_mesh_decompose",
    "tracker_url": "https://github.com/Korchy/1d_mesh_decompose",
    "category": "All"
}


# MAIN CLASS

class MeshDecompose:

    @classmethod
    def shift(cls, context, offset=0.5):
        # shift all selected meshes to offset by Z-axis
        for i, obj in enumerate(context.selected_objects):
            obj.location.z += offset * i

    @staticmethod
    def ui(layout, context):
        # ui panel
        # Mesh Decompose
        op = layout.operator(
            operator='meshdecompose.shift',
            icon='SEQ_SEQUENCER'
        )
        op.offset = context.scene.meshdecompose_prop_offset
        layout.prop(
            data=context.scene,
            property='meshdecompose_prop_offset'
        )


# OPERATORS

class MeshDecompose_OT_shift(Operator):
    bl_idname = 'meshdecompose.shift'
    bl_label = 'Shift'
    bl_options = {'REGISTER', 'UNDO'}

    offset = FloatProperty(
        name='Offset',
        default=0.5
    )

    def execute(self, context):
        MeshDecompose.shift(
            context=context,
            offset=self.offset
        )
        return {'FINISHED'}


# PANELS

class MeshDecompose_PT_panel(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_label = 'Mesh Decompose'
    bl_category = '1D'

    def draw(self, context):
        MeshDecompose.ui(
            layout=self.layout,
            context=context
        )


# REGISTER

def register(ui=True):
    Scene.meshdecompose_prop_offset = FloatProperty(
        name='Offset',
        default=0.5
    )
    register_class(MeshDecompose_OT_shift)
    if ui:
        register_class(MeshDecompose_PT_panel)


def unregister(ui=True):
    if ui:
        unregister_class(MeshDecompose_PT_panel)
    unregister_class(MeshDecompose_OT_shift)
    del Scene.meshdecompose_prop_offset


if __name__ == '__main__':
    register()
