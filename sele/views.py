import time

from django.http import JsonResponse
from django.shortcuts import render

from sele.models import Submission


def index(request):
    return render(request, 'index.html')


def table(request):
    time.sleep(0.5)  # Broken pipe from avoider
    queryset = Submission.objects.all()
    return render(request, 'table.html', {'submissions': queryset})


def form(request):

    if request.method == 'GET':
        return render(request, 'form.html')
    else:
        try:
            data = request.POST
            Submission.objects.create(
                title=data.get('title'),
                material=data.get('material'),
                work_cutting='work_cutting' in data.get('works'),
                work_griding='work_griding' in data.get('works'),
                work_filling='work_filling' in data.get('works'),
                comments=data.get('comments'),
                responsible=data.get('responsible'),
                phone=data.get('phone'),
            )
            return render(request, 'form.html', {'success': True, 'text': 'Форма успешно заполнена'})
        except Exception as e:
            return render(request, 'form.html', {'error': True, 'text': repr(e)})


def table_status_changer(request, id):
    inst = Submission.objects.get(pk=id)
    inst.status = not inst.status
    inst.save()
    return JsonResponse({'success': True}, status=201)
