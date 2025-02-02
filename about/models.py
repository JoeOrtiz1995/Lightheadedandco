from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Unapproved"), (1, "Approved"))


class About(models.Model):
    """
    Stores the About section's content
    """
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    """
    Stores Testminoials submitted by users
    """
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="testimonial_author")
    body = models.TextField()
    approved = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Testimonial submitted by {self.author}"
