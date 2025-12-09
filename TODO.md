# Fix Image Display Issue

## Tasks
- [ ] Change image_url to image (ImageField) in models.py for Project and Client
- [ ] Update admin.py to include the image field in list_display and add form fields
- [ ] Update forms.py to include the image field
- [ ] Add MEDIA_URL and MEDIA_ROOT to settings.py
- [ ] Update home.html template to use {{ p.image.url }} instead of {{ p.image_url }}
- [ ] Run migrations
