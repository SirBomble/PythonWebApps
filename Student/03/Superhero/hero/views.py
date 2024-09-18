from django.views.generic import TemplateView

heroes = {
    'hulk': {
        'title': 'Hulk',
        'body': 'My name is Bruce Banner',
        'image': '/static/images/hulk.jpg',
        'url': '/hulk'
    },
    'ironman': {
        'title': 'Iron Man',
        'body': 'My name is Tony Stark, but I am Iron Man',
        'image': '/static/images/iron_man.jpg',
        'url': '/ironman'
    },
    'blackwidow': {
        'title': 'Black Widow',
        'body': 'My name is Natasha Romanova',
        'image': '/static/images/black_widow.jpg',
        'url': '/blackwidow'
    },
    'spiderpig': {
        'title': 'Spider Pig',
        'body': 'My name is Peter Porker',
        'image': '/static/images/spiderpig.jpg',
        'url': '/spiderpig'
    }
}

class IndexView(TemplateView):
    template_name = 'heroes.html'

class HulkView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return heroes['hulk']


class IronManView(TemplateView):
    template_name = "hero.html"

    def get_context_data(self, **kwargs):
        return heroes['ironman']


class BlackWidow(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return heroes['blackwidow']

class SpiderPig(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return heroes['spiderpig']