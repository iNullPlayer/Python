# Inversion de cadena #

def reverse(text):
  text_len = len(text) - 1
  reverse_text = ""
  for index in range(0, len(text)):
    reverse_text += text[text_len - index]
  return reverse_text

print(reverse("Hola mundo"))