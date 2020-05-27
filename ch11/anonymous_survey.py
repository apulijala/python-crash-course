
class AnyonymousSurvey():
    def __init__(self, question):
        self.question = question
        self.responses = []
    
    def ask_question(self):
        print(self.question)
    
    def store_responses(self, response):
        self.responses.append(response)
    
    def print_survey(self):
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")


"""
question= "What language did you first learn to speak?"
my_survey = AnyonymousSurvey(question)
my_survey.ask_question()

print("Enter 'q' at any time to quit. ")
response= input("Lanugage: ")

while response != 'q':
    my_survey.store_responses(response)
    response= input("Lanugage: ")

my_survey.print_survey()
"""