from django.shortcuts import render , get_object_or_404, redirect
from django.contrib.staticfiles import *
from django.templatetags.static import static
from prepa.models import Question
from csv import *
from os import *

# Create your views here.
def home(request):

    """ print(request.GET.get("Privé"))

    filière = request.GET.get("filière")
    if filière == "None":
        filière = ""

    département = request.GET.get("Département")

    nom = request.GET.get("Nom")
    if nom == "None":
        nom = ""

    privé = request.GET.get("Privé")
    public = request.GET.get("Public")
    
    context = {
        'filière': filière,
        'département': département,
        'nom': nom,
    }
    return render(request, 'prepa/home.html', context) 

    """ 
    
    file_csv = open('prepa/csv/prepa-scientifiques.csv',"r",encoding="utf-8")
    prepa_csv = file_csv.reader(file_csv,delimiter=";")
    prepa_list = []
    for ligne in prepa_csv:
        prepa_list.append(ligne[0,1,3:9,16])
    print(prepa[1])





def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    context = {
        'question': question,
        'options': question.options.all(),
        'nb_questions': Question.objects.count(),
        'question_number': question.get_number(),
    }
    return render(request, 'prepa/q.html', context)
