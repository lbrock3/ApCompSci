def change_emoji(text):
    return text.replace(":)","🙂")
    return text.replace(":(", "🙁")

def main():
    text = input("Type a sentence: ")
    print(change_emoji(text))

main() 