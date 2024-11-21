from chatterbot import ChatBot
import time 
from chatterbot.trainers import ListTrainer
time.clock = time.time
bot = ChatBot('H19', read_only = False, logic_adapters = ['chatterbot.logic.BestMatch'])
list_to_response = [
    'Hello',
    'How i can help you ?',
    'How are you ?',
    'I \'m a chatbot'
]
list_response = ListTrainer(bot)
list_response.train('chatterbot.corpus.english')
while True:
    exit = ['bye', 'good bye','see you again']
    question = input('You: ')
    if question.lower() in exit:
        print('Bot: Bye')
        break
    else: answer = bot.get_response(question)
    print('Bot: ', answer)