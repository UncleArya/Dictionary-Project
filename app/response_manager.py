# Modules
from api_call import call_api


class ResponseManager:
    def __init__(self, user_query):
        self.user_query = user_query
        self.response = call_api(self.user_query)[0]
        self.word = self.response["word"]
        self.phonetics = self.response["phonetics"]  # TODO - parse out
        # self.origin = self.response["origin"]
        # TODO - display all meanings
        self.meanings = self.response["meanings"]
        self.part_of_speech = self.meanings[0]["partOfSpeech"]
        # TODO - display all definitions
        self.definition = self.meanings[0]["definitions"][0]["definition"]
        # self.example = self.meanings[0]["definitions"][0]["example"] # TODO - display all examples
        self.source = self.response["sourceUrls"][0]

    def get_query(self):
        query_response = {
            "Word": self.word,
            "Phonetics": self.phonetics,
            # "Origin": self.origin,
            "Meanings": self.meanings,
            "Part of Speech": self.part_of_speech,
            "Definition": self.definition,
            # "Example": self.example,
            "Source": self.source,
        }
        return query_response
