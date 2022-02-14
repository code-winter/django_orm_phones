from django.shortcuts import render, redirect

from phones.models import Phone


phones_obj = Phone.objects.all()
phone_list = []
for phone in phones_obj:
    phone_list.append(phone)


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    result = []
    sort_mode = request.GET.get('sort')
    if sort_mode:
        if sort_mode == 'name':
            result = sorted(phone_list, key=lambda model: model.name)
        elif sort_mode == 'min_price':
            result = sorted(phone_list, key=lambda model: model.price)
        elif sort_mode == 'max_price':
            result = sorted(phone_list, key=lambda model: model.price, reverse=True)
    else:
        result = phone_list
    context = {'phones': result}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    result = {}
    for model in phone_list:
        if slug == model.slug:
            result = model
    context = {'phone': result}
    return render(request, template, context)
