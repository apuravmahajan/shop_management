from django.shortcuts import render
from .models import salesData
from datetime import datetime
from django.db import models

# Create your views here.

def update(request):
    if request.method == 'POST':
        date = datetime.strptime(request.POST['date'], '%Y-%m-%d')
        writtensp = float(request.POST['writtensp'])
        actualsp = float(request.POST['actualsp'])
        cp = (writtensp-550) * 0.8
        profit = actualsp - cp
        salesData.objects.create(date=date,cp=cp, sp=actualsp, profit=profit)
        return render(request, 'update.html', {"submitted":True,"cp":cp,"sp":actualsp,"profit":profit})
    return render(request, 'update.html', {"submitted" : False})

def display(request):
    if request.method =='POST':
        start = request.POST['date1']
        end = request.POST['date2']
        data = salesData.objects.filter(date__range=[start, end])
        
        grouped_data = data.values('date').annotate(
            sales_count=models.Sum('profit'),
            items_count=models.Count('id')
        ).order_by('date')

        items = data.count()
        total_profit = data.aggregate(models.Sum('profit'))['profit__sum'] or 0
        total_profit_m = total_profit - 50*items

        return render(request, 'display.html', {'submitted':True, 'items':items, 'data':grouped_data, 'total_profit_m':total_profit_m, 'total_profit':total_profit})
    return render(request, 'display.html', {'submitted':False})
    
def delete(request):
    if request.method == 'POST':
        id = request.POST['id']
        salesData.objects.filter(id=id).delete()
        return render(request, 'delete.html', {'submitted':True})
    else:
        data = salesData.objects.all()
        return render(request, 'delete.html', {'submitted':False, 'data':data})