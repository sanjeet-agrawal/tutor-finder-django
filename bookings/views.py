from django.shortcuts import render, get_object_or_404, redirect
from tutors.models import Tutor
from .forms import BookingForm
from .models import Booking
from django.contrib.auth.decorators import login_required

@login_required
def book_tutor(request, tutor_id):
    tutor = get_object_or_404(Tutor, id=tutor_id)

    if request.user == tutor.user:
        return redirect('tutor_list')

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.student = request.user
            booking.tutor = tutor
            booking.save()
            return redirect('/tutors/')
    else:
        form = BookingForm()

    return render(request, 'bookings/book_tutor.html', {'form': form, 'tutor': tutor})


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(student=request.user)
    return render(request, 'bookings/my_bookings.html', {'bookings': bookings})

@login_required
def tutor_bookings(request):
    try:
        tutor = Tutor.objects.get(user=request.user)
    except Tutor.DoesNotExist:
        return render(request, 'bookings/tutor_bookings.html', {
            'error': 'You are not registered as a tutor.'
        })

    bookings = Booking.objects.filter(tutor=tutor)

    return render(request, 'bookings/tutor_bookings.html', {'bookings': bookings})