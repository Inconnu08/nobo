from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Plot, Booking, Applicant


class PlotForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Plot
        fields = '__all__'


class BookingForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Booking
        fields = '__all__'


class ApplicantForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Applicant
        fields = '__all__'
