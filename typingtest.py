import time

def calculate_typing_speed(start_time, end_time, text):
    total_time = end_time - start_time
    words = text.split()
    num_words = len(words)
    speed = num_words / (total_time / 60)
    return speed

def run_speed_typing_test():
    print("Welcome to the Speed Typing Test!")
    text = "The quick brown fox jumps over the lazy dog."
    print("Type the following sentence:")
    print(text)
    input("Press Enter when you're ready...")
    
    start_time = time.time()
    user_input = input()
    end_time = time.time()
    
    typing_speed = calculate_typing_speed(start_time, end_time, user_input)
    print("Your typing speed: {:.2f} words per minute".format(typing_speed))

if __name__ == '__main__':
    run_speed_typing_test()
