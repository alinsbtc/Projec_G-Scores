from django.shortcuts import render
from .models import Score
from django.db.models import F, ExpressionWrapper, FloatField


def index(request):
    top_students = (
        Score.objects.annotate(
            total_score=F('toan') + F('vat_li') + F('hoa_hoc')  
        )
        .filter(toan__isnull=False, vat_li__isnull=False, hoa_hoc__isnull=False) 
        .order_by('-total_score')[:10]  
    )

    return render(request, 'scores/index.html', {'top_students': top_students})

def search_scores(request):
    query = request.GET.get('query', '')
    scores = Score.objects.filter(sbd__icontains=query) if query else []
    return render(request, 'scores/search.html', {'scores': scores, 'query': query})

from django.shortcuts import render
from django.db.models import Count
from scores.models import Score

def report(request):
    # Define all subjects
    subjects = [
        'toan', 'ngu_van', 'ngoai_ngu', 
        'vat_li', 'hoa_hoc', 'sinh_hoc', 
        'lich_su', 'dia_li', 'gdcd'
    ]
    
    # Initialize data dictionary
    data = {}

    # Loop through each subject to calculate statistics
    for subject in subjects:
        data[subject] = {
            'level_1': Score.objects.filter(**{f"{subject}__gte": 8}).count(),
            'level_2': Score.objects.filter(**{f"{subject}__lt": 8, f"{subject}__gte": 6}).count(),
            'level_3': Score.objects.filter(**{f"{subject}__lt": 6, f"{subject}__gte": 4}).count(),
            'level_4': Score.objects.filter(**{f"{subject}__lt": 4}).count(),
        }

    return render(request, 'scores/report.html', {'data': data})
