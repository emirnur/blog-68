import datetime
import json
from datetime import datetime
from django.http import HttpResponse, JsonResponse

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def digit_valid(string):
    if string.isdigit():
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


@csrf_exempt
def add(request, *args, **kwargs):
    if request.method == 'POST':
        data = json.loads(request.body)
        count = 0
        for item in data:
            if digit_valid(str(data[item])) is True:
                count += float(data[item])
            else:
                response = JsonResponse({'error': "Symbols must be digits!"})
                response.status_code = 400
                return response
        return JsonResponse({'answer': count})


@csrf_exempt
def subtract(request, *args, **kwargs):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        first_number = data.get('A')
        second_number = data.get('B')
        if (digit_valid(str(first_number)) is True) and (digit_valid(str(second_number)) is True):
            return JsonResponse({'answer': float(first_number) - float(second_number)})
        else:
            response = JsonResponse({'error': "Symbols must be digits!"})
            response.status_code = 400
            return response


@csrf_exempt
def multiply(request, *args, **kwargs):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        first_number = data.get('A')
        second_number = data.get('B')
        if (digit_valid(str(first_number)) is True) and (digit_valid(str(second_number)) is True):
            return JsonResponse({'answer': float(first_number) * float(second_number)})
        else:
            response = JsonResponse({'error': "Symbols must be digits!"})
            response.status_code = 400
            return response


@csrf_exempt
def divide(request, *args, **kwargs):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        first_number = data.get('A')
        second_number = data.get('B')
        if (digit_valid(str(first_number)) is True) and (digit_valid(str(second_number)) is True):
            if int(second_number) == 0:
                response = JsonResponse({'error': "Division by zero!"})
                response.status_code = 400
                return response
            else:
                return JsonResponse({'answer': float(first_number) / float(second_number)})
        else:
            response = JsonResponse({'error': "Symbols must be digits!"})
            response.status_code = 400
            return response

