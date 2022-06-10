from bpy.props import BoolProperty, PointerProperty
from ..hubs_component import HubsComponent
from ..types import Category, PanelType, NodeType
from ..utils import has_component
from bpy.types import Object


def filter_on_component(self, o):
    return has_component(o, 'video-texture-source')


class VideoTextureTarget(HubsComponent):
    _definition = {
        'name': 'video-texture-target',
        'display_name': 'Video Texture Target',
        'category': Category.AVATAR,
        'node_type': NodeType.MATERIAL,
        'panel_type': [PanelType.MATERIAL],
        'icon': 'IMAGE_DATA'
    }

    targetBaseColorMap: BoolProperty(
        name="Override Base Color Map", description="Should the video texture override the base color map?", default=True)

    targetEmissiveMap: BoolProperty(
        name="Override Emissive Color Map", description="Should the video texture override the emissive map?", default=True)

    srcNode: PointerProperty(
        name="Source",
        description="Node with a vide-texture-source to pull video from",
        type=Object,
        poll=filter_on_component)

    def draw(self, context, layout):
        has_material = len(context.object.material_slots) > 0
        if has_material:
            super().draw(context, layout)
        else:
            layout.alert = True
            layout.label(text='This component requires a material',
                         icon='ERROR')