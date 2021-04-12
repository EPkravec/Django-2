from django.shortcuts import render, redirect
from .models import Deal
from .forms import DealForm
from django.contrib import messages
import csv
import io
from django.http import HttpResponse


def index(request):
    deals = Deal.objects.all()
    return render(request, 'main/index.html', {'title': 'Тестовое задание', 'deal': deals})




def deal(request):
    error = ''
    if request.method == 'POST':
        form = DealForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('general')
        else:
            error = 'Форма заполена не верно'
    form = DealForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/deal.html', context)


def deal_load_csv(request):
    download_page = "main/deal_load_csv.html"

    prompt = {'order': 'Последовательность в csv должна быть customer, item, total, quantity, date'}

    if request.method == "GET":
        return render(request, download_page, prompt)

    csv_file = request.FILES['file_csv']

    if not csv_file.name.endswith('.csv'):
        return messages.error(request, 'Это не файл csv')

    data_set = csv_file.read().decode('utf-8-sig')
    io_string = io.StringIO(data_set)
    next(io_string)

    for column in csv.reader(io_string, delimiter=',', quotechar='|'):
        _, created = Deal.objects.update_or_create(
            customer=column[0],
            item=column[1],
            total=column[2],
            quantity=column[3],
            date=column[4]
        )

    context = {}
    return render(request, download_page, context)
