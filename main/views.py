from django.shortcuts import render, redirect
from main.forms import CustomUserForm, MealForm
from main.models import Meal
from django.db.models import Sum
from datetime import datetime, timedelta


def add_meal(request):
    form = MealForm()
    if request.method == 'POST':
        form = MealForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('read_meal')
    return render(request, 'add_meal.html', {'form': form})


def read_meal(request):
    meals = Meal.objects.all()

    # Calculate total calories consumed in a day
    today = datetime.now().date()
    today_meals = meals.filter(date__date=today)
    total_calories_today = today_meals.aggregate(total_calories=Sum('calories'))['total_calories'] or 0

    # Calculate total calories consumed in the past week
    week_ago = today - timedelta(days=7)
    week_meals = meals.filter(date__date__gte=week_ago, date__date__lte=today)
    total_calories_week = week_meals.aggregate(total_calories=Sum('calories'))['total_calories'] or 0

    return render(request, 'read_meal.html', {
        "meals": meals,
        "total_calories_today": total_calories_today,
        "total_calories_week": total_calories_week,
        "user": request.user,
    })


def delete_meal(request, meal_id):
    meal = Meal.objects.get(id=meal_id)
    if request.method == 'POST':
        if 'return' in request.POST:
            return redirect('read_meal')
        if 'delete' in request.POST:
            meal.delete()
            return redirect('read_meal')
    return render(request, 'delete_meal.html', {'meal': meal})


def edit_meal(request, meal_id):
    meal = Meal.objects.get(id=meal_id)
    form = MealForm(instance=meal)
    if request.method == 'POST':
        form = MealForm(request.POST, instance=meal)
        form.save()
        return redirect('read_meal')
    return render(request, 'edit_meal.html', {'form': form})


def calculate_bmi(request):
    user = request.user
    if user.is_authenticated:
        form = CustomUserForm(instance=user)

        bmi = None

        if request.method == 'POST':
            form = CustomUserForm(request.POST, instance=user)
            if form.is_valid():
                user = form.save()
                bmi = user.calculate_bmi()
    else:
        form = CustomUserForm()

        bmi = None

        if request.method == 'POST':
            form = CustomUserForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                bmi = user.calculate_bmi()

    return render(request, 'calculate_bmi.html', {'form': form, 'bmi': bmi})
