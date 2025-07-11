import datetime

from django.urls import reverse
from django.test import TestCase
from django.utils import timezone

from .models import Question

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])
    def test_past_question(self):
        question = create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question]
        )
    def test_future_question(self):
        question = create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            []
        )
    def test_future_question_and_past_question(self):
        past_question = create_question(question_text="Past question.", days=-30)
        future_question = create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [past_question]
        )
    def test_two_past_questions(self):
        past_question1 = create_question(question_text="Past question 1.", days=-30)
        past_question2 = create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [past_question2, past_question1]
        )
    def test_two_future_questions(self):
        future_question1 = create_question(question_text="Future question 1.", days=30)
        future_question2 = create_question(question_text="Future question 2.", days=5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            []
        )
    def test_two_future_questions_and_one_past_question(self):
        past_question = create_question(question_text="Past question.", days=-30)
        future_question1 = create_question(question_text="Future question 1.", days=30)
        future_question2 = create_question(question_text="Future question 2.", days=5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [past_question]
        )
    def test_two_past_questions_and_one_future_question(self):
        past_question1 = create_question(question_text="Past question 1.", days=-30)
        past_question2 = create_question(question_text="Past question 2.", days=-5)
        future_question = create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [past_question2, past_question1]
        )
    def test_two_past_questions_and_one_future_question_with_different_days(self):
        past_question1 = create_question(question_text="Past question 1.", days=-30)
        past_question2 = create_question(question_text="Past question 2.", days=-5)
        future_question = create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [past_question2, past_question1]
        )
    def test_two_past_questions_and_one_future_question_with_different_days_and_order(self):
        past_question1 = create_question(question_text="Past question 1.", days=-30)
        past_question2 = create_question(question_text="Past question 2.", days=-5)
        future_question = create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [past_question2, past_question1]
        )
    def test_two_past_questions_and_one_future_question_with_different_days_and_order_and_different_text(self):
        past_question1 = create_question(question_text="Past question 1.", days=-30)
        past_question2 = create_question(question_text="Past question 2.", days=-5)
        future_question = create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [past_question2, past_question1]
        )
    def test_two_past_questions_and_one_future_question_with_different_days_and_order_and_different_text_and_different_order(self):
        past_question1 = create_question(question_text="Past question 1.", days=-30)
        past_question2 = create_question(question_text="Past question 2.", days=-5)
        future_question = create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [past_question2, past_question1]
        )
    def test_two_past_questions_and_one_future_question_with_different_days_and_order_and_different_text_and_different_order_and_different_text(self):
        past_question1 = create_question(question_text="Past question 1.", days=-30)
        past_question2 = create_question(question_text="Past question 2.", days=-5)
        future_question = create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [past_question2, past_question1]
        )
    def test_two_past_questions_and_one_future_question_with_different_days_and_order_and_different_text_and_different_order_and_different_text_and_different_order(self):
        past_question1 = create_question(question_text="Past question 1.", days=-30)
        past_question2 = create_question(question_text="Past question 2.", days=-5)
        future_question = create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [past_question2, past_question1]
        )
