from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category, Tag
from django.db.models import F


class Home(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Classic Blog Design'
        return context


class PostsByCategory(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 4
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context


class PostsByTag(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 4
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Записи по тегу: ' + str(Tag.objects.get(slug=self.kwargs['slug']))
        return context


class GetPost(DetailView):
    model = Post
    template_name = 'blog/single.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        Как правило, get_context_data данные контекста всех родительских классов объединяются с данными текущего класса.
        Чтобы сохранить это поведение в ваших собственных классах, где вы хотите изменить контекст, вы должны
        обязательно вызвать get_context_dataсуперкласс. Когда никакие два класса не пытаются определить один и тот же ключ,
        это даст ожидаемые результаты. Однако, если какой-либо класс пытается переопределить ключ после того, как
        родительские классы установили его (после вызова super), любые дочерние элементы этого класса также должны
        будут явно установить его после super, если они хотят обязательно переопределить всех родителей. Если у вас
        возникли проблемы, проверьте порядок разрешения методов вашего представления.

        Еще одно соображение заключается в том, что данные контекста из общих представлений на основе классов будут
        иметь приоритет над данными, предоставленными обработчиками контекста; см. get_context_data()пример.
        """
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1  # Кол-во просмотров
        self.object.save()
        self.object.refresh_from_db()  # помогает обновлять значения из бд
        return context


class Search(ListView):
    template_name = 'blog/search.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = f"s={self.request.GET.get('s')}&"
        return context
