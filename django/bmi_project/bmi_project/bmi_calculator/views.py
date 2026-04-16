from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

def index(request):
	if request.method == 'POST':
		weightKg = float(request.POST.get('weight', 0)) # Weight in Kilograms.
		heightCm = float(request.POST.get('height', 0)) # Height in Centimeter.
		bmi = calcBmi(weightKg, heightCm);
		return render(request, 'bmi_form.html', { 'bmi': bmi })
	elif request.method == 'GET':
		return render(request, 'bmi_form.html', { 'bmi': None })


def calcBmi(weightKg, heightCm):
	if heightCm <= 0 or weightKg <= 0:
		return "[ERROR] Invalid value(s); Failed to calculate BMI.";
	heightM = heightCm / 100.0 # Height in meter.
	return round(weightKg / (heightM * heightM), 2)