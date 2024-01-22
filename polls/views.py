from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.urls import reverse
from django.views import generic


# class IndexView(generic.ListView):
#     template_name = 'polls/index.html'
#     contex_object_name = 'latest_question_list'

#     def get_queryset(self):
#         return Question.objects.order_by('-pub_date')[:3]
    
# class DetailView(generic.DetailView):
#     model = Question
#     template_name =  'polls/detail.html'

# class ResultView(generic.DetailView):
#     model = Question
#     template_name = 'polls/result.html'


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:3]
    # print("List is  ________")
    # print(list(latest_question_list))
    # output = ', '.join([q.question_text for q in latest_question_list])
    # print(output)
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list' : latest_question_list,
    }
    # print(context)
    # return HttpResponse(template.render(context,request))
    return render( request,'polls/index.html',context)


def details(request,question_id):
    question = get_object_or_404(Question, pk= question_id)
    return render(request, 'polls/detail.html', {'question': question})

    # return HttpResponse("You are looking at question %s" % question_id)

def result(request,question_id):
    # response = "You are looking at result of question %s"
    # return HttpResponse(response % question_id)
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/result.html', {'question':question})

def vote(request,question_id):
    question = get_object_or_404(Question,pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        print("____selected choice")
        print(selected_choice)
    except (KeyError,Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, 'error_message': "No choice was selected"})
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:result',args=(question.id,)))

