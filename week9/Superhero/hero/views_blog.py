from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Blog
class BlogView(RedirectView):
    url = reverse_lazy('blog_list')


class BlogListView(ListView):
    template_name = 'blog/list.html'
    model = Blog
    context_object_name = 'blogs'


class BlogDetailView(DetailView):
    template_name = 'blog/detail.html'
    model = Blog
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = self.object.article_set.filter(blog__pk=self.object.pk)
        return context


class BlogCreateView(LoginRequiredMixin, CreateView):
    template_name = "blog/add.html"
    model = Blog
    fields = '__all__'

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        if not self.request.user.is_staff:
            form.fields.pop('author', None)
        return form

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "blog/edit.html"
    model = Blog
    fields = '__all__'


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('blog_list')
