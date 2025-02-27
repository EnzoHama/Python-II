from django.shortcuts import render

def index(request):
    nome= ""
    if request.method == "POST":
        nome= request.POST.get("nome", "")
    return render(request, "minha_aplicação\index.html", {"nome": nome})
