from graph import logo
from converter import Converter

# setup
run_converter = True
print(logo)

while run_converter:
    text = input("Give me text! ").upper()

    converter = Converter()
    print(f"Here's your text converted to morsecode: {converter.to_morsecode(text)}")

    cont = input("Do you want to convert something else? Y/N ").upper()
    if cont == "N":
        print("OK, bye!")
        run_converter = False
