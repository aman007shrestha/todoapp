from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem
# Create your views here.

def todoview(request):
	todos = TodoItem.objects.all()
	context ={'todos': todos}

	return render(request, 'todo/home.html', context)
#	return HttpResponse("This is todoview")

def add_todo(request):
	print('hi')
	content = request.POST['content']
	print(content)
	obj = TodoItem(content=content)
	obj.save()
	return redirect('index')

def delete(request, pk):
	todo_obj = get_object_or_404(TodoItem, pk=pk)
	todo_obj.delete()
	return redirect('index')

