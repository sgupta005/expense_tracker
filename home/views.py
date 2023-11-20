from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from users.forms import ProfileUpdateForm, UserUpdateForm

@login_required
def home(request):
    profile = Profile.objects.filter(user = request.user).first()
    expenses = Expense.objects.filter(user = request.user)
    if request.method == 'POST':
        text = request.POST.get('text')
        amount = request.POST.get('amount')
        expense_type = request.POST.get('expense_type') 

        expense = Expense(name=text , amount=amount , expense_type=expense_type , user= request.user)
        expense.save()
        
        if expense_type == 'Positive':
            profile.income += float(amount)
        else:
            profile.expenses += float(amount)
            
        profile.save()
        return redirect('/')

    context = {'profile' : profile , 'expenses' : expenses}
    return render(request , 'home.html' , context)

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'profile.html',context)