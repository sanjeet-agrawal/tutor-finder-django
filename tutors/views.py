from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Tutor
from .forms import TutorForm
from django.shortcuts import render

def tutor_list(request):
    query = request.GET.get('q')

    if query:
        tutors = (Tutor.objects.filter(subject__name__icontains=query) | 
          Tutor.objects.filter(location__icontains=query)).distinct()
    else:
        tutors = Tutor.objects.all()

    return render(request, 'tutors/tutor_list.html', {'tutors': tutors})

def tutor_detail(request, tutor_id):
    tutor = get_object_or_404(Tutor, id=tutor_id)
    return render(request, 'tutors/tutor_detail.html', {'tutor': tutor})



@login_required
def edit_tutor_profile(request):

    tutor = Tutor.objects.get(user=request.user)

    if request.method == 'POST':
        form = TutorForm(request.POST, request.FILES, instance=tutor)

        if form.is_valid():
            form.save()
            return redirect('/tutors/')

    else:
        form = TutorForm(instance=tutor)

    return render(request, 'tutors/edit_profile.html', {'form': form})