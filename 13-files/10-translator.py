from translate import Translator

with open("message.txt", "r") as my_message:
  message_text = my_message.read()
  print(f"Original message: {message_text}")
  print("Translating....")
  translator = Translator(to_lang="es")
  translation = translator.translate(message_text)
  
  print(f"Message translated! {translation}")
  
  with open('translated_message.txt', 'w') as my_translation:
    my_translation.write(translation)