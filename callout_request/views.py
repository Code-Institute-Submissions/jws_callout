from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Request 
from .forms import RequestForm
from .forms import CommentForm


class RequestList(generic.ListView):
    model = Request
    queryset = Request.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6 


class RequestDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Request.objects.filter(slug=slug)
        request_obj = get_object_or_404(queryset, slug=slug)
        comments = request_obj.comments.filter(approved=True).order_by("-created_on")
        

        return render(
            request,
            "callout_request.html",
            {
                "request": request,
                "comments": comments,
                "comment_form": CommentForm()
            },
        )


class AddRequest(generic.CreateView):
    model = Request
    form_class = RequestForm
    template_name = 'add_request.html'
  