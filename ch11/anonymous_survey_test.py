from anonymous_survey import AnyonymousSurvey
import unittest

class AnyonymousSurveyTest(unittest.TestCase):
    def test_single_response(self):

        question = "What Language did you learn first? "
        my_survey = AnyonymousSurvey(question)
        my_survey.store_responses("English")
        self.assertIn("English", my_survey.responses)

    def test_multiple_responses(self):
        question = "What Language did you learn first? "
        my_survey = AnyonymousSurvey(question)
        responses = ["English", "Hindi", "Telugu"]
       #  responses_again = ["English", "Hindi", "Telugu", "Sanskrit"]
        for response in responses:
            my_survey.store_responses(response)

        # for response in responses_again:
        for response in my_survey.responses:
            self.assertIn(response, my_survey.responses)

if __name__ == "__main__":
    unittest.main()