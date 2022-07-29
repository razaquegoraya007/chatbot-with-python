import re
import long_responses as long

def message_probability(user_message,recognized_words,single_response = False,required_words = []):
    message_certainity = 0
    has_required_words = True
    for word in user_message:
        if word in recognized_words:
            message_certainity += 1
    percentage = float(message_certainity)/float(len(recognized_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0


def check_all_the_message(message):
    highest_prob_list = {}

    def response(bot_response,list_of_words,single_response= False,required_words = []):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message,list_of_words,single_response,required_words)

    response('The Presidential Initiative for Artificial Intelligence and Computing was launched by the President of Pakistan, Dr. Arif Alvi, to promote education, research and business opportunities',['PIAIC','piaic','what is piaic'],single_response=True)
    response('The courses offered by PIAIC are Artificial Intelligence, Blockchain, Internet of Things, and Cloud Native Computing',['courses','what courses are being offered'],single_response=True)
    response('Teachers are Sir Qasim, Sir Nasir and Sir Zeeshan',['whose are the teachers teaching these courses', 'teachers'])

    best_match = max(highest_prob_list,key=highest_prob_list.get)
    # print(highest_prob_list)

    return best_match


def get_response(user_input):
    split_message = re.split(r'\s+|[,.!-?:;]\s*',user_input.lower())
    response = check_all_the_message(split_message)
    return response

# Testing the response System
while True:
    print('Bot: '+ get_response(input('You: ')))
