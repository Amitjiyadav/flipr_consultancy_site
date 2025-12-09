from django.db import models
# Create your models here.
from PIL import Image   

class Project(models.Model):
    # pehle image_url = models.URLField()
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # pehle normal save
        super().save(*args, **kwargs)

        if self.image:
            img_path = self.image.path
            img = Image.open(img_path)

            target_w, target_h = 450, 350
            w, h = img.size

            # --- crop to target ratio (center crop) ---
            target_ratio = target_w / target_h
            current_ratio = w / h

            if current_ratio > target_ratio:
                # image zyada wide hai -> sides se crop
                new_w = int(h * target_ratio)
                left = (w - new_w) // 2
                upper = 0
                right = left + new_w
                lower = h
            else:
                # image zyada tall hai -> top/bottom se crop
                new_h = int(w / target_ratio)
                left = 0
                upper = (h - new_h) // 2
                right = w
                lower = upper + new_h

            img = img.crop((left, upper, right, lower))
            # final size fix
            img = img.resize((target_w, target_h), Image.LANCZOS)

            # overwrite same file
            img.save(img_path, quality=90)


class Client(models.Model):
    # pehle image_url = models.URLField()
    image = models.ImageField(upload_to="clients/", blank=True, null=True)
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            img_path = self.image.path
            img = Image.open(img_path)

            target_w, target_h = 450, 350
            w, h = img.size
            target_ratio = target_w / target_h
            current_ratio = w / h

            if current_ratio > target_ratio:
                new_w = int(h * target_ratio)
                left = (w - new_w) // 2
                upper = 0
                right = left + new_w
                lower = h
            else:
                new_h = int(w / target_ratio)
                left = 0
                upper = (h - new_h) // 2
                right = w
                lower = upper + new_h

            img = img.crop((left, upper, right, lower))
            img = img.resize((target_w, target_h), Image.LANCZOS)
            img.save(img_path, quality=90)



class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.email}"


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
