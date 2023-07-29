from django.db import models
from apps.account.models import Account


class TimeStamp(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.created_date


class Language(TimeStamp):
    title = models.CharField(max_length=221)

    def __str__(self):
        return f"{self.title} - {self.created_date}"


class Tag(TimeStamp):
    title = models.CharField(max_length=221)

    def __str__(self):
        return f"{self.title} - {self.created_date}"


class Discussion(TimeStamp):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=221)
    description = models.TextField()

    def __str__(self):
        return f"{self.account} - {self.title} - {self.description}"

class Solution(TimeStamp):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    solution = models.TextField()

    def __str__(self):
        return f"{self.solution} - {self.created_date}"


class Problem(TimeStamp):
    DIFFICULTY = (
        (0, 'Easy'),
        (1, 'Medium'),
        (2, 'Hard'),
    )
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=221)
    description = models.TextField()
    language = models.ForeignKey(Language, models.CASCADE)
    tags = models.ManyToManyField(Tag)
    difficulty = models.IntegerField(choices=DIFFICULTY, default=0)
    discussions = models.ManyToManyField(Discussion, null=True, blank=True)
    solutions = models.ForeignKey(Solution, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class SolvedProblem(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.account} - {self.problem}"
