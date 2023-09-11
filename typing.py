import random
import time

def get_random_sentence():
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Python is a versatile programming language.",
        "Typing tests can improve your coding skills.",
        "Practice makes perfect!",
    ]
    return random.choice(sentences)

def calculate_typing_speed(start_time, end_time, typed_text):
    elapsed_time = end_time - start_time
    words = typed_text.split()
    num_words = len(words)
    words_per_minute = (num_words / elapsed_time) * 60
    return words_per_minute

def typing_test():
    print("Welcome to the Typing Test!")
    input("Press Enter to start...")
    
    sentence = get_random_sentence()
    print(f"Type this sentence: {sentence}")
    
    start_time = time.time()
    typed_text = input()
    end_time = time.time()
    
    words_per_minute = calculate_typing_speed(start_time, end_time, typed_text)
    
    correct_words = sum(1 for typed_word, original_word in zip(typed_text.split(), sentence.split()) if typed_word == original_word)
    accuracy = (correct_words / len(sentence.split())) * 100
    
    print(f"Your typing speed: {words_per_minute:.2f} words per minute")
    print(f"Accuracy: {accuracy:.2f}%")
    
if __name__ == "__main__":
    typing_test()
