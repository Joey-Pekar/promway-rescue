from django.db import models
from django.utils import timezone

# Get gallery directory for dog.
def get_dir(instance, filename):

    if isinstance(instance, Dog):
        dog_dir = instance.name
    elif isinstance(instance, GalleryImage):
        dog_dir = instance.dog.name
    else:
        return "gallery/{0}".format(filename)
    
    return "gallery/{0}/{1}".format(dog_dir, filename)

# Create your models here.
class Dog(models.Model):
    class Sex(models.TextChoices):
        Male = "Male"
        Female = "Female"

    # 

    # Basic Information
    name = models.CharField(max_length=255)
    breed = models.CharField(max_length=255)
    dob = models.DateField("Birthdate")
    sex = models.CharField(max_length=6, choices=Sex.choices)
    weight = models.IntegerField()

    # Compatibility
    dog_friendly = models.BooleanField()
    cat_friendly = models.BooleanField()
    child_friendly = models.BooleanField()
    house_broken = models.BooleanField()

    profile_pic = models.ImageField("Profile Picture", upload_to=get_dir)
    description = models.TextField()

    # Other
    adopted = models.BooleanField()
    notice = models.CharField(max_length=255, blank=True, null=True)
    bonded_pair = models.ManyToManyField("self", blank=True)
    hidden = models.BooleanField()

    def __str__(self):
        return self.name
    
    def Age(self):
        now = timezone.now().date()
        return int(now.year) - int(self.dob.year) - ((int(now.month), int(now.day)) < (int(self.dob.month), int(self.dob.day)))

    
class GalleryImage(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_dir)