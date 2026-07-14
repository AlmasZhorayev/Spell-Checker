import spell_checker 

def main():
    bf, tree = spell_checker.build_spell_checker()

    sentence = input("Enter a sentence: ")
    results = spell_checker.check_sentence(sentence, bf, tree)

    if not results:
        print("No misspelled words found.")
    else:
        for word, suggestions in results.items():
            print(f"Misspelled word: '{word}'")
            print(f"Suggestions: {', '.join(suggestions)}")

if __name__ == "__main__":
    main()