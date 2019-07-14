# Generated by Django 2.2.3 on 2019-07-14 00:41

from django.db import migrations
from django.utils import timezone


def add_initial_questions(apps, schema_editor):
    Question = apps.get_model("surveys", "Question")
    add_question(Question, "How cool is this app?", ["👌", "👏", "👍", "👎", "💩"])
    add_question(
        Question,
        "What is your favorite programming language",
        ["C#", "Python", "Java", "PHP", "Javascript", "Go"],
    )
    add_question(Question, "Tabs or Spaces", ["Tabs", "Spaces", "Seriously?"])
    add_question(Question, "What is your favorite OS", ["Linux", "Windows", "macOS"])


def add_question(question_model, question_text, choices):
    question = question_model(question_text=question_text, pub_date=timezone.now())
    question.save()
    for choice in choices:
        question.choices.create(choice_text=choice)


class Migration(migrations.Migration):

    dependencies = [("surveys", "0002_auto_20190713_1840")]

    operations = [migrations.RunPython(add_initial_questions)]
