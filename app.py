from deep_translator import GoogleTranslator

def english_to_hindi_translator():
    print("English to Hindi Translator")
    print("--------------------------")
    
    while True:
        print("\nOptions:")
        print("1. Translate English to Hindi")
        print("2. Exit")
        
        choice = input("Enter your choice (1/2): ")
        
        if choice == '1':
            english_text = input("\nEnter English text: ")
            
            if not english_text.strip():
                print("Please enter some text to translate.")
                continue
                
            try:
                translation = GoogleTranslator(source='en', target='hi').translate(english_text)
                print("\nTranslation Result:")
                print(f"English: {english_text}")
                print(f"Hindi: {translation}")
                    
            except Exception as e:
                print(f"Translation failed. Error: {e}")
                
        elif choice == '2':
            print("Thank you for using the translator. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter 1 or 2.")

if name == "main":
    english_to_hindi_translator()
