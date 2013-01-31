__author__ = 'aramael'

from django.shortcuts import render
from open_mike.apps.signups.models import SignUp

def home(request):

    context = {}

    if request.method == 'POST':
        # Parse Information Posted to create New Sign Up

        errors = []

        # Check Email
        from django.core.validators import validate_email
        from django.core.exceptions import ValidationError
        try:
            email = validate_email( request.POST['email'] )
        except (ValidationError, KeyError):
            errors.append('How can we contact you? You forgot to give us an email &hellip;')
            email = None

        # Check Name
        if 'name' in request.POST and len(request.POST['name']) > 3:
            name = request.POST['name']
        else:
            errors.append('Please provide a name.')
            name = None

        # Check Act Name
        if 'act-name' in request.POST and len(request.POST['act-name']) > 3:
            act_name = request.POST['act-name']
        else:
            errors.append('Give us something to call this talent. Think about it like giving it a codename')
            act_name = None

        # Check Act Description
        if 'act-description' in request.POST and len(request.POST['act-description']) > 3:
            act_description = request.POST['act-description']
        else:
            errors.append('Tell us about what you plan on doing. Anything would be nice.')
            act_description = None

        # Check Act Special Requests
        if 'act-requests' in request.POST:
            act_requests = request.POST['act-requests']
        else:
            act_requests = None

        if not errors:
            sign_up = SignUp(
                name = name,
                act_name = act_name,
                act_description = act_description,
                act_requests = act_requests
            )
            sign_up.save()
            context.update({
                'errors': None,
                'success': True
            })
        else:
            context.update({
                'errors': errors
            })

    return render(request,'front_page.html', context)