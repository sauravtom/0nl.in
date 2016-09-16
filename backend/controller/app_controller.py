""" App controller """

from django.shortcuts import render, get_object_or_404
from profiles.models import Profile

import os
import subprocess
import yaml

# Root directory '/' i.e. (src)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Directory containing all the profiles
PROFILES_DIR = os.path.join(BASE_DIR, 'static/profiles/e')

# List of all the templates, user can choose from
TEMPLATES_LIST = {
    '1': 'profiles_base/template1.html',
    '2': 'profiles_base/template2.html',
    '3': 'profiles_base/template3.html',
}

class Controller(object):
    """ App controller class """

    def __init__(self, request):
        """ Initialise object with all the details """
        self.request = request

    def get_user(self):
        """ Get user details """

        user = get_object_or_404(CustomUser, id=self.request.user.id)
        return user

    def touch(self, file_name):
        """ Create a file, `touch` functionality of shell """

        open(file_name, 'a').close()
        return

    def create_yaml(self, filename, data):
        """ Given a filename and data create and write a yaml file for a user """

        with open('app.yaml', 'w') as outfile:
            yaml.dump(data, outfile, default_flow_style=False)
        return

    def load_yaml(self, filename):
        """ Load the yaml data of a given file """

        with open(filename, 'r') as f:
            yaml_data = yaml.load(f)
        return yaml_data

    def update_yaml_file(self, filename, yaml_data):
        """ Given a file, data update the yaml file with new data """

        with open(filename, "w") as f:
            yaml.dump(yaml_data, f, default_flow_style=False)
        return

    def is_register_form_valid(self, data):
        """ Check if the data provided in the register form is valid """

        # List to catch errors
        error_list = []

        first_name = data['first_name']
        last_name = data['last_name']
        username = data['username']
        email = data['email']
        
        if username:
            print username
            try:
                Profile.objects.get(username=username)
                error_list.append("Profile already exists")
            except:
                pass
        else:
            error_list.append("Please enter a valid username")

        if email:
            try:
                Profile.objects.get(username=username)
                error_list.append("Email already exists")
            except:
                pass
        else:
            error_list.append("Please enter a valid email")

        if not first_name:
            error_list.append("First name should not be empty")

        if not last_name:
            error_list.append("Last name should not be empty")

        if len(error_list) is 0:
            return True, error_list
        else:
            return False, error_list

    def get_create_profile(self):
        """ Initial data for creat user profile """

        # Return dict
        data = {}

        # html tempplate for `create_profile`
        html = 'create_profile.html'

        if self.request.method == 'GET':
            pass
        else:
            # POST request
            # Get all the data from the request
            data = {
                'first_name': str(self.request.POST.get('firstname', '')),
                'last_name': str(self.request.POST.get('lastname', '')),
                'username': str(self.request.POST.get('username', '')),
                'email': str(self.request.POST.get('email', '')),
                'about': str(self.request.POST.get('about', '')),
                'github_url': str(self.request.POST.get('github_url', '')),
                'twitter_url': str(self.request.POST.get('twitter_url', '')),
                'facebook_url': str(self.request.POST.get('facebook_url', '')),
                'linkedin_url': str(self.request.POST.get('linkedin_url', '')),
                'website': str(self.request.POST.get('website', '')),
                'skype_id': str(self.request.POST.get('skype_id', '')),
                'template': str(self.request.POST.get('template', '')),
                'phone': str(self.request.POST.get('phone', '')),
            }

            # Check if form is valid and fetch errors if any
            is_valid, error_list = self.is_register_form_valid(data)

            if is_valid:
                # Create and save profile object
                profile = Profile(**data)
                profile.save()

                # Create the folder with name => 'username'
                os.chdir(PROFILES_DIR)
                try:
                    os.mkdir(data.get('username'))
                except OSError as e:
                    print e.errno,
                    print e.filename
                    print e.strerror
                os.chdir(data.get('username'))

                self.create_yaml("app.yaml", data) # create and write app.yaml

                # Navigate to the directory containing the shell script i.e. `/static/profiles/`
                os.chdir(BASE_DIR)

                # Commit changes to github using the shell script
                # Passing the 'add' argument to commit update message
                subprocess.check_call(['./commit_changes.sh', 'add', data['username']])
                data['success'] = True
            else:
                data['errors'] = error_list
                data['success'] = False

        return data, html

    def get_profile_data(self, id):
        """ Fetch and send data of a profile """
        
        # Get the profile object
        profile = get_object_or_404(Profile, id=id)

        # html tempplate for `edit_profile`
        html = 'edit_profile.html'

        # Navigate to the user profile dir
        try:
            os.chdir(os.path.join(PROFILES_DIR, profile.username))
        except OSError as e:
            print e.errno,
            print e.filename
            print e.strerror

        # Load the yaml data
        yaml_data = self.load_yaml('app.yaml')

        # Get the html path from users template attribute and global TEMPLATE LIST
        html = TEMPLATES_LIST[yaml_data['template']]

        return yaml_data, html

    def get_edit_profile_data(self, id):
        """ Get profile data for editing """

        # Get the profile object
        profile = get_object_or_404(Profile, id=id)

        # html tempplate for `create_profile`
        html = 'edit_profile.html'

        # Navigate to the user profile dir
        try:
            os.chdir(os.path.join(PROFILES_DIR, profile.username))
        except OSError as e:
            print e.errno,
            print e.filename
            print e.strerror

        # Load the yaml data
        yaml_data = self.load_yaml('app.yaml')

        if self.request.method == 'POST':
            # Data to be returned
            dict = {}

            # Get POST data
            data = {
                'first_name': str(self.request.POST.get('firstname', '')),
                'username': str(profile.username), # workaround as disabled inputs passed as empty
                'email': str(profile.email), # workaround as disabled inputs passed as empty
                'last_name': str(self.request.POST.get('lastname', '')),
                'about': str(self.request.POST.get('about', '')),
                'github_url': str(self.request.POST.get('github_url', '')),
                'twitter_url': str(self.request.POST.get('twitter_url', '')),
                'facebook_url': str(self.request.POST.get('facebook_url', '')),
                'linkedin_url': str(self.request.POST.get('linkedin_url', '')),
                'website': str(self.request.POST.get('website', '')),
                'skype_id': str(self.request.POST.get('skype_id', '')),
                'template': str(self.request.POST.get('template', '')),
                'phone': str(self.request.POST.get('phone', '')),
            }

            # Update yaml data
            yaml_data['first_name'] = data['first_name']
            yaml_data['last_name'] = data['last_name']
            yaml_data['about'] = data['about']
            yaml_data['github_url'] = data['github_url']
            yaml_data['twitter_url'] = data['twitter_url']
            yaml_data['facebook_url'] = data['facebook_url']
            yaml_data['linkedin_url'] = data['linkedin_url']
            yaml_data['website'] = data['website']
            yaml_data['skype_id'] = data['skype_id']
            yaml_data['template'] = data['template']
            yaml_data['phone'] = data['phone']

            # Updpate yaml file
            self.update_yaml_file('app.yaml', yaml_data)

            # Save data to database, using this way I need the pk so that we can use it in filter
            Profile.objects.filter(id=profile.id).update(**yaml_data)

            # Navigate to the directory containing the shell script i.e. `/static/profiles/`
            os.chdir(BASE_DIR)

            # Commit changes to github using the shell script
            # Passing the 'update' argument to commit update message
            subprocess.check_call(['./commit_changes.sh', 'update', data['username']])

            dict['success'] = True
            return dict, html

        return yaml_data, html
