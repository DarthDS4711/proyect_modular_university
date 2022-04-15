from core.colorpage.models import ColorPage


class ObtainColorMixin:
    def get_number_color(self):
        color = ColorPage.objects.using('color').get(id=1)
        if color is not None:
            return color.color_selected
        else:
            return 3