import speech_recognition as sr
import pyttsx3


def listen():
    # Создание экземпляра объекта для распознавания речи
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Скажите что-нибудь...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        # Распознавание речи с использованием Google Speech Recognition
        text = r.recognize_google(audio, language="ru-RU")
        print(f"Распознанный текст: {text}")
        return text
    except sr.UnknownValueError:
        print("Хм, не удалось распознать речь")
    except sr.RequestError as e:
        print(f"Ошибка сервиса распознавания речи; {e}")

    return ""


def speak(text):
    # Создание экземпляра синтезатора речи
    engine = pyttsx3.init()

    # Установка голоса на русский
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    # Синтез и воспроизведение речи
    engine.say(text)
    engine.runAndWait()


def robot_cook():
    speak("Привет! Я робот-повар Шэфи. Чем могу помочь?")

    while True:
        command = listen().lower()

        if "привет" in command:
            speak("Приветствую!")
        elif "пока" in command:
            speak("До свидания!")
            break
        else:
            speak("Извините, я не понял вашу команду.")


def add_task(tasks, task):
    tasks.append(task)
    print("Задача добавлена:" + task)


def main():
    tasks = []

    while True:
        command = listen().lower()

        if "добавить задачу" in command:
            task = command.replace("добавить задачу", "").strip()
            add_task(tasks, task)
        elif "показать задачи" in command:
            print("Список задач:")
            for task in tasks:
                print(task)
        elif "выход" in command:
            break
        else:
            print("Команда не распознана. Попробуйте еще раз.")


if __name__ == "__main__":
    robot_cook()
    main()