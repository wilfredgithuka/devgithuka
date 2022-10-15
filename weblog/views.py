# Standard Python Library imports.
from functools import reduce
import operator

# Core Django imports.
from django.contrib import messages
from django.db.models import Q
from django.db.models import Count
from django.views.generic import (
    DetailView,
    ListView,
)

# Weblog application imports.
from .models import Post

class PostListView(ListView):
    context_object_name = "posts"
    paginate_by = 12
    #queryset = Documents.objects.filter(status=Post.PUBLISHED, deleted=False)
    queryset = Post.objects.all()
    template_name = "posts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['categories'] = Category.objects.filter(approved=True)
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts_detail.html'

    def get_context_data(self, **kwargs):
        session_key = f"viewed_equipment {self.object.title}"
        if not self.request.session.get(session_key, False):
            #self.object.views += 1
            self.object.save()
            self.request.session[session_key] = True

        # kwargs['related_docyments'] = \
        #     Document.objects.filter(category=self.object.category).order_by('?')[:3]
        kwargs['post'] = self.object
        #kwargs['comment_form'] = CommentForm()
        return super().get_context_data(**kwargs)


class PostSearchListView(ListView):
    model = Post
    paginate_by = 12
    context_object_name = 'search_results'
    template_name = "posts_search.html"

    def get_queryset(self):
        
        query = self.request.GET.get('q')

        if query:
            query_list = query.split()
            search_results = Equipment.objects.filter(
                reduce(operator.and_,
                       (Q(title__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(content__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                        (Q(status__icontains=q) for q in query_list))
            )

            if not search_results:
                messages.info(self.request, f"No results for '{query}'")
                return search_results
            else:
                messages.success(self.request, f"Results for '{query}'")
                return search_results
        else:
            messages.error(self.request, f"Sorry you did not enter any keyword")
            return []

    def get_context_data(self, **kwargs):
        """
            Add categories to context data
        """
        context = super(PostSearchListView, self).get_context_data(**kwargs)
        #context['categories'] = Category.objects.filter(approved=True)
        return context
