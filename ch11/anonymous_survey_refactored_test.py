from anonymous_survey import AnyonymousSurvey
import unittest

class AnyonymousSurveyTest(unittest.TestCase):

    def setUp(self):
        question = "What Language did you learn first? "
        self.my_survey = AnyonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']
       


    def test_single_response(self):
        self.my_survey.store_responses(self.responses[0])
        self.assertIn("English", self.my_survey.responses)

    def test_multiple_responses(self):
       
       
       #  responses_again = ["English", "Hindi", "Telugu", "Sanskrit"]
        for response in self.responses:
            self.my_survey.store_responses(response)

        # for response in responses_again:
        for response in self.my_survey.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == "__main__":
    unittest.main()