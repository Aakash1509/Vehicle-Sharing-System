from VehSS import Owner

def emaill(request):
    number=Owner.objects.all()
    return {'number':number}