from django.shortcuts import render
from django.http import HttpResponse
import os
from pathlib import Path

# Create your views here.

personal_computer_username = 'enter username here'

subdirectory = f'/Users/{personal_computer_username}/Desktop/department_feedback'
success = f'/Users/{personal_computer_username}/Desktop/irvineHack/studentFeedback/templates/studentFeedback/receivedData.html'
failure = f'/Users/{personal_computer_username}/Desktop/irvineHack/studentFeedback/templates/studentFeedback/sameNameFailure.html'
IDs = []

def index(request):
    'Displays the starting page of the feedback form'
    return render(request, f'/Users/{personal_computer_username}/Desktop/irvineHack/studentFeedback/templates/studentFeedback/feedbackQuestions.html')


def save_file(file_name, lines, response_format):
    'Saves each of the lines in a file'
    file_path = Path(os.path.join(subdirectory, file_name))
    with open(file_path, 'w') as file:
        n = 0
        while n < len(lines):
            file.write(response_format[n])
            file.write(lines[n])
            file.write('\n')
            n += 1


def receivedFeedback(request):
    '''
    Receives the feedback, renders a file showing what was submitted and
    saves what was submitted into a folder given a directory.
    '''
    if request.method == 'POST':
        studentID = request.POST['id']
        if studentID not in IDs:
            IDs.append(studentID)
            courseImpression = request.POST['courseImpression']
            expectations = request.POST['expectations']
            rating = request.POST['rating']
            lines = [studentID, courseImpression, expectations, rating]
            responses = ['Student ID:          ',
                         'Course Impression:   ', 
                         'Expectations:        ', 
                         'Rating:              ']
            save_file(studentID, lines, responses)
            return render(request, success, {
                'id': studentID,
                'courseImpression': courseImpression,
                'expectations': expectations,
                'rating': rating,
            })
        else:
            return render(request, failure, {
                'id': studentID,
            })