from django.db import models


class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        if len(postData['course_name']) < 5:
            errors['course_name'] = "Course name should be at least 5 characters"
        if len(postData['course_description']) < 15:
            errors['course_description'] = "Course description should be at least 15 characters"
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()
