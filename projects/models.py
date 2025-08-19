from django.db import models
import uuid


# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    demo_link = models.CharField(max_length=2000, blank=True, null=True)
    source_link = models.CharField(max_length=2000, blank=True, null=True)
    featured_image = models.ImageField(default='default.svg', null=True, blank=True)  # Default image if none is provided
    tags = models.ManyToManyField('Tag', blank=True, related_name='projects')  # Many-to-many relationship with Tag model
    vote_total = models.IntegerField(default=0)  # Total votes for the project
    vote_ratio = models.IntegerField(default=0)  # Ratio of upvotes to downvotes
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False)  # Unique identifier for each project , we use editable=False to prevent it from being changed after creation

    def __str__(self):
        return self.title  # String representation of the model, returns the title of the project

    class Meta:
        ordering = ['-created_at']  # Order by creation date, newest first


class Review(models.Model):
    # Vote_Type = (
    #     ('1', '1 Star'),
    #     ('2', '2 Stars'),
    #     ('3', '3 Stars'),
    #     ('4', '4 Stars'),
    #     ('5', '5 Stars')
    # )  # Choices for the value field, representing star ratings

    Vote_Type = (
        ('up', 'Up vote'),
        ('down', 'Down vote')
    )

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='reviews')
    body = models.TextField()
    value = models.CharField(max_length=200,
                             choices=Vote_Type)  # The value field will store the star rating as a string
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False)

    def __str__(self):
        return f'Review for {self.project.title} - {self.value}'  # String representation of the model, returns the project title and value of the review


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False)

    def __str__(self):
        return self.name  # String representation of the model, returns the name of the tag

    class Meta:
        ordering = ['name']  # Order tags alphabetically by name