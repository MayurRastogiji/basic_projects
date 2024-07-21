import random
import pyttsx3
engine = pyttsx3.init()
def speakandprint(str):
    print(str)
    engine.say(str)
    engine.runAndWait()
questions = ["What is the primary function of a CPU?", "Which protocol is used for sending emails?", "What is the file extension for a Microsoft Word document?", "What does \"HTML\" stand for in web development?", "What programming language is often used for web development?", "What is the term for a program that replicates itself and spreads to other computers?", " Which programming language is known for its use in data analysis and scientific computing?", "What does \"URL\" stand for?", "In computing, what does \"RAM\" stand for?", "Which company developed the Windows operating system?", " What is the standard protocol used for secure web communication?", "What is the code name of the open-source web browser developed by Mozilla?", "What is the term for a small piece of code that performs a specific task within a larger program?", "What type of software allows users to view web pages on the internet?", "What is the file extension for a compressed archive format commonly used on Windows?"]
answers = ["processing data", "smtp", "docx", "hypertext markup language", "javascript", "virus", "python", "uniform resource locator", "random access memory", "microsoft", "https", "firefox", "function", "web browser", "zip"]
speakandprint("enter your name : \n")
name = input()
speakandprint(f"welcome {name} to the quiz game")
prize = 0
speakandprint("enter number of attempts : \n")
attempt = int(input())
i = 0
while i < attempt:
    if i != 0:
        speakandprint("your next question is\n")
    random_index = random.randint(0, len(questions) - 1)
    speakandprint(questions[random_index])
    speakandprint("your options are:")
    for j in range(1,4):
        options = random.randint(0, len(answers) - 1)
        print(j , answers[options])
    # ans = int(random_index)
    # print("\n\n\n" , ans)
    print(j+1 , answers[random_index])
    speakandprint("enter your answer : \n")
    a = input()
    if a == answers[random_index] or j+1:
        speakandprint("your answer is correct \nyou won 1000 rupees \n ")
        prize = prize + 1000
    else:
        speakandprint("your answer is wrong \nyou lost 500 rupees \n ")
        prize = prize - 500
    i = i+1
if prize > 0:
    print(name," won: ",prize,"\ncongratulations")
else:
    print(name," lost: ",prize,"\ntry again")
