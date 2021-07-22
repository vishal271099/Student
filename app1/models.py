from django.db import models



STD_CHOICE = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10')
)
EVALUATION_CHOICE = (
    ('fail', 'Fail'),
    ('pass', 'Pass')
)
RELATION_CHOICE = (
    ('mother', 'Mother'),
    ('father', 'Father'),
    ('other', 'Other')
)


class StudentDetail(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    standard = models.CharField(
        default="1", max_length=50, choices=STD_CHOICE)
    evaluation = models.CharField(
        default='pass', max_length=5, choices=EVALUATION_CHOICE)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    active = models.BooleanField()
    joined_on = models.DateTimeField()

    def __str__(self):
        return self.first_name


class GuardianDetail(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20,)
    student = models.ForeignKey(
        StudentDetail, on_delete=models.CASCADE, related_name="guardians")
    relation = models.CharField(
        default='father', max_length=20, choices=RELATION_CHOICE)
    address = models.TextField()
    mobile_no = models.PositiveIntegerField()

    def __str__(self):
        return self.first_name





