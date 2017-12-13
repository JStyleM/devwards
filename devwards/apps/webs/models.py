from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class WebSite(models.Model):

	nombre = models.CharField(max_length=100)
	slug = models.SlugField(editable=False)
	url = models.URLField()
	description = models.CharField(max_length=100)
	designer = models.CharField(max_length=100)
	designer_url = models.URLField()
	twitter = models.CharField(max_length=100)
	image1 = models.ImageField(upload_to = 'websites')
	image2 = models.ImageField(upload_to = 'websites')
	image3 = models.ImageField(upload_to = 'websites')

	create_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(WebSite, self).save(*args, **kwargs)

