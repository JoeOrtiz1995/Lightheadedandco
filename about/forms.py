from django import forms
from .models import Testimonial


class TestimonialForm(forms.ModelForm):
    """
    Form class for Users to submit Testimonials
    """
    class Meta:
        """
        Indicates the model used and field order
        """
        model = Testimonial
        fields = ('body',)
