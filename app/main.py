from response_manager import ResponseManager
# from flask import Flask

# app = Flask(__name__)


user_query = input("Search: ")
search = ResponseManager(user_query=user_query)
result = search.get_query()
print(result["Definition"])


# @app.route("/")
# def home():
#     return "<p>Hello, World!</p>"


# # Editing
# if __name__ == "__main__":
#     app.run(debug=True)
