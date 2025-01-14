from django.db import models

class About(models.Model):
  """
  Stores the About section's content
  """
  title = models.CharField(max_length=200)
  content = models.TextField()

  def __str__(self):
    return self.title