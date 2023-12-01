# views.py
import json
from django.shortcuts import render
from django.http import JsonResponse
from .models import Question, Option, PersonalityType
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
# def index(request):
#     questions = Question.objects.all()
#     context = {'questions': questions}
#     return render(request, 'trials/index.html', context)

def landing(request):
    return render(request, 'trials/landing.html')

def index(request):
    if request.method == 'POST':
        answers = request.POST.get('answers')
        print('Answers:', answers)
        if answers:
            answers_dict = json.loads(answers)

            label_a_count = 0
            label_b_count = 0
            labels_for_sets = []

            for i, (question_id, option_id) in enumerate(answers_dict.items(), start=1):
                option = Option.objects.get(pk=option_id)
                if option.label == 'a':
                    label_a_count += 1
                elif option.label == 'b':
                    label_b_count += 1

                if i % 3 == 0:
                    current_label = determine_label(label_a_count, label_b_count, i // 3)
                    labels_for_sets.append(current_label)
                    label_a_count = 0
                    label_b_count = 0

            print('Labels for Sets:', labels_for_sets)

            request.session['labels_for_sets'] = labels_for_sets

            if len(labels_for_sets) == 3:
                final_personality_trait = determine_final_personality(labels_for_sets)
                personality_type = find_personality_type(final_personality_trait)
                print('Personality Type:', personality_type)

                if personality_type:
                    return JsonResponse({'personality_type': personality_type.name})
                else:
                    return JsonResponse({'error': 'Personality type not found.'})
            return JsonResponse({'error': 'Personality type not found.'})
        else:
            return JsonResponse({'error': 'Answers not found.'})
    else:
        questions = Question.objects.all()
        context = {'questions': questions}
        return render(request, 'trials/index.html', context)

def result(request):
    personality_type = request.GET.get('personality_type')

    if personality_type:
        personality_type_instance = get_object_or_404(PersonalityType, name=personality_type)

        # Generate the absolute URL for the current page including query parameters
        current_page_url = request.build_absolute_uri(request.get_full_path())

        return render(request, 'trials/result.html', {'personality_type': personality_type_instance, 'current_page_url': current_page_url})
    else:
        # Redirect to an error page or handle the error case differently
        return render(request, 'trials/result.html', {'error': 'Personality type not found.'})
    
def determine_label(label_a_count, label_b_count, set_number):
    # Determine the label for the current set of three questions

    if label_a_count > label_b_count:
        if set_number == 1:
            return 'a'
        elif set_number == 2:
            return 'c'
        elif set_number == 3:
            return 'e'
    elif label_a_count < label_b_count:
        if set_number == 1:
            return 'b'
        elif set_number == 2:
            return 'd'
        elif set_number == 3:
            return 'f'
    else:
        return 'neutral' 
    
def determine_final_personality(labels_for_sets):
    # Determine the final personality trait based on the combination of three labels
    # You can customize this logic based on your specific requirements
    # For simplicity, this example assumes a linear combination
    if labels_for_sets == ['b', 'c', 'e']:
        return '小葡气'  # First result page
    elif labels_for_sets == ['b', 'd', 'e']:
        return '芒芒人海'  # Second result page
    elif labels_for_sets == ['a', 'c', 'e']:
        return '十有八酒'  # Third result page
    elif labels_for_sets == ['a', 'd', 'e']:
        return '龙舌兰日出'  # Fourth result page
    elif labels_for_sets == ['b', 'c', 'f']:
        return '汽泡艺术家'  # Fifth result page
    elif labels_for_sets == ['b', 'd', 'f']:
        return '四季茶香'  # Sixth result page
    elif labels_for_sets == ['a', 'c', 'f']:
        return '橘子海'  # Seventh result page
    elif labels_for_sets == ['a', 'd', 'f']:
        return '樱花落'  # Eighth result page
    else:
        return 'Unknown Personality'  # Handle any other case as needed

def find_personality_type(personality_type_name):
    try:
        personality_type = PersonalityType.objects.get(name=personality_type_name)
        return personality_type
    except PersonalityType.DoesNotExist:
        return None