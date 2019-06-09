
from datetime import date

from django.conf import settings
from django.db import models
# from django.urlresolvers import reverse

# Create your models here.
#MVC model view controller

# class PostManager(models.Manager):
# 	def all(self, *args, **kwargs)
# 		return super(PostManager, self).filter(draft=False).filter(publish__lte=timezone.now)

def upload_location(instance, filename):
	return "blog%s_%s" %(instance.id,filename)

class Post(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	title = models.CharField(max_length=120)
	image = models.ImageField(
		upload_to=upload_location,
		null=True,
		blank=True)
	content = models.TextField()
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)

	draft = models.BooleanField(default=False)

#	objects = PostManager() #link the overriden class


	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

	# def get_absolute_url(self):
	# 	return reverse("posts:details", kwargs={"id": self.id})

#		return "/posts/%s/" %(self.id)

	class Meta:
		ordering  = ["-updated"]
# 		order by reverse id,timestamp,updated