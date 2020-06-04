from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager):
	""" Helps Djnago work with our custom user model """
	def create_user(self, email, name, password=None):
		""" Creates a new user profile object """
		if not email:
			raise ValueError('User must have an email address')

		user = self.model(
			email=self.normalize_email(email),
			name=name
		)
		user.set_password(password)     #encrypt
		user.save(using=self._db)

		return user

	def create_superuser(self, email, name, password):
		""" Creates and saves a new superuser with given details """
		user = self.create_user(email, name, password)

		user.is_superuser = True
		user.is_staff = True

		user.save(using=self._db)

		return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
	"""Respents a "user profile" inside our system."""
	#look at documentation about models/fields
	email = models.EmailField(max_length=255, unique=True)
	name = models.CharField(max_length=255)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)	

	objects = UserProfileManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['name']    #all that you want

	def get_full_name(self):
		""" Used to get a user's full name """
		return self.name

	def get_short_name(self):
		""" Used to get a user's short name """
		return self.name

	def __str__(self):
		""" Django uses this when it needs to convert the object to a string """
		return str(self.name) if self.name else ''



class ProfileFeedItem(models.Model):
	""" Profile status update """

	user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
	status_text = models.CharField(max_length=255)
	created_on = models.DateTimeField(auto_now_add=True)	

	def __str__(self):
		""" Returns the model as a string """
		return self.status_text


