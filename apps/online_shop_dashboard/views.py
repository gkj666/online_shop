from django.shortcuts import render, redirect

def dashboard(request):
    return render(request, "online_shop_dashboard/dashboard.html", {})
