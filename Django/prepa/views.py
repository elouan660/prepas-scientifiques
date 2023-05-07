from django.shortcuts import render , get_object_or_404, redirect
from prepa.models import Question

# Create your views here.
def home(request):
    return render(request, 'prepa/home.html')

def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    context = {
        'question': question,
        'options': question.options.all(),
        'nb_questions': Question.objects.count(),
        'question_number': question.get_number(),
    }
    return render(request, 'prepa/q.html', context)

