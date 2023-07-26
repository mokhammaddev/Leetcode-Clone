from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Difficulty(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Solutions(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text


class Problem(models.Model):
    difficulty = models.ForeignKey(Difficulty, on_delete=models.CASCADE)
    title = models.CharField(max_length=221)
    category = models.ForeignKey(Category, models.CASCADE)
    solutions = models.ForeignKey(Solutions, on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Descriptions(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    text = models.TextField()

    def __str__(self):
        return self.text


class Statistic(models.Model):
    difficulty = models.ForeignKey(Difficulty, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    descriptions = models.ForeignKey(Descriptions, on_delete=models.CASCADE)
