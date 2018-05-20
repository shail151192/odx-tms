from django import forms
from .models import AuthUser
from django.contrib.auth.models import User

class UserForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    username=forms.CharField(required=True)

    class Meta:
        model=User
        fields=('first_name', 'last_name', 'email', 'username')

    def to_python(self, value):
        '''
        :param value:
        :return: converted value to correct data type
        '''
        return value

    def validate(self, value):
        '''
        handle the specfic validation
        :param value:
        :return None:
        '''

        pass

    def run_validators(self):
        '''
        run all the fields validators and aggrigates the results
        :return:
        '''
        pass

    def clean_first_name(self):
        print "firstname is valid"
        data=self.cleaned_data
        return data['first_name']

    def clean_last_name(self):
        print "lastname is valid"
        data=self.cleaned_data
        return data['last_name']

    def clean_email(self):
        print "email is valid"
        data=self.cleaned_data
        return data['email']

    # def clean_phone_no(self):
    #     print "phone number is valid"
    #     data=self.cleaned_data
    #     return data

    # def clean_username(self):
    #     print "username is valid"
    #     data=self.cleaned_data
    #     return data
    #
    # def clean_password(self):
    #     print "password is valid"
    #     data=self.cleaned_data
    #     return data

    def save(self, commit=True):
        print "save methd is called"
        print self.cleaned_data
        print self.cleaned_data['last_name']
        validated_data=self.cleaned_data
        user=AuthUser(**validated_data)
        user.save()
        return user


