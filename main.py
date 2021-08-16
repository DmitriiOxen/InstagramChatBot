from time import sleep
import pyautogui as pt
import pyperclip as pc

sleep(2)


def move_to_text_input(message):
    position = pt.locateOnScreen("images/photo icon.PNG", confidence=0.7)
    pt.moveTo(position[0:2], duration=0.5)
    pt.moveRel(-100, 20, duration=0.5)
    pt.doubleClick(interval=0.3)
    pt.typewrite(message, interval=0.01)
    pt.typewrite("\n")


def get_messages():
    position = pt.locateOnScreen('images/emojis.png', confidence=0.9)
    pt.moveTo(position[0:2], duration=0.5)
    pt.moveRel(50, -50, duration=0.5)
    pt.click()
# click on triple dots
    position = pt.locateOnScreen('images/dots icon.png', confidence=0.9)
    pt.moveTo(position[0:2], duration=0.5)
    pt.click()
# click on "copy" button
    position = pt.locateOnScreen('images/copy_icon.png', confidence=0.7)
    pt.moveTo(position[0] + 10, position[1] + 15, duration=0.5)
    pt.click()

    userText = pc.paste()
    return userText


def process_message(message):
    msg = str(message).lower()

    if msg == 'hello':
        return 'Hey Bud! You can ask me : what is your age? where are you located?'
    elif msg == 'hey':
        return 'Hey yo... now bye'
    elif msg == 'whats up?':
        return 'not your business...'
    elif msg == 'what is your age?':
        return 'I am 20 years old, my birthday is on February 7th'
    elif msg == 'where are you located?':
        return 'I am in Toronto, country Canada, province Ontario at the moment. Let me know if you are close by'
    else:
        return 'sounds like nonsense. Text me "hello" to see possible questions'


currentMessage, lastMessage = '', ''


def insta_chatbot():
    global lastMessage, currentMessage
    currentMessage = get_messages()
    if currentMessage != lastMessage:
        lastMessage = currentMessage
        print(f'Last message: {currentMessage}')
        # bot response
        response = process_message(currentMessage)
        print(f'Bot: {response}')
        if lastMessage != response:
            move_to_text_input(response)
    else:
        print('No new messages...')


while True:
    try:
        insta_chatbot()
        sleep(10)
    except Exception as e:
        print(f'Exception: {e}')
        sleep(10)
