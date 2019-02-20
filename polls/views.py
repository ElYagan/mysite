from django.shortcuts import get_object_or_404, render

# Create your views here.

from django.http import HttpResponse

from .models import CL_CHASIS


def index(request):
    latest_chasis_list = CL_CHASIS.objects.order_by('-FechaCreaChasis')[:20]
    context = { 'latest_chasis_list': latest_chasis_list }
    return render(request, 'polls/index.html', context)

def detail(request, CL_CHASIS_id):
    chasis = get_object_or_404(CL_CHASIS, pk=CL_CHASIS_id)
    return render(request, 'polls/detail.html', {'CL_CHASIS': chasis})


def results(request, CL_CHASIS_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % CL_CHASIS_id)


def vote(request, CL_CHASIS_id):
    return HttpResponse("You're voting on question %s." % CL_CHASIS_id)
