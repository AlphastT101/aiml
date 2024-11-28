import aiml
# import os

kernel = aiml.Kernel()
kernel.load_preset("standard")
# aiml_directory = os.path.join(os.path.dirname(__file__), "aiml", "botdata", "standard")


# for filename in os.listdir(aiml_directory):
#     if filename.endswith(".aiml"):
#         aiml_file_path = os.path.join(aiml_directory, filename)
#         print(aiml_file_path)
#         kernel.learn(aiml_file_path, log=False)


# print("Chatbot ready! Type 'exit' to quit.")
# while True:
#     user_input = input("You: ")
#     if user_input.lower() == 'exit':
#         print("Goodbye!")
#         break

#     response = kernel.respond(user_input)
#     print(f"Chatbot: {response}")



