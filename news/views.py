from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import News, Category

class BlogIndexView(generic.ListView):
    model = News
    #paginate_by = 12
    template_name = 'news/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context.update({
            'news_list': News.objects.order_by('-created_on')
        })
        return context

class DetailedView(generic.DetailView):
    model = News
    template_name = "news/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class CategoryListView(generic.ListView):
    model = Category
    template_name = "news/cat_index.html"

    def get_context_data(self, **kwargs):
        category  = get_object_or_404(Category, cat_slug=self.kwargs.get('cat_slug'))
        context = super().get_context_data(**kwargs)
        context.update({
            'news_list': News.objects.order_by('-created_on').filter(category_id=category.id),
            'cat' : category,
        })
        return context