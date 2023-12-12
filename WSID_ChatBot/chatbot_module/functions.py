import string
import random


def remove_punctuation(input_string):
    """removes punctuation.
    
    (Code from A3-Chatbot)
    
    Parameters
    ----------
    input_string: string that
    needs to have its punctuation removed
    
    Returns
    -------
    answer : string without punctuation
    """
    unpunctuated_string = ""
    
    # punctuation removing loop
    for char in input_string:
        
        if char not in string.punctuation:
            unpunctuated_string += char
            
    return unpunctuated_string



# makes input string an unpunctuated list of lower case words
def prepare_text(input_string):
    """removes punctuation,
    makes words lowercase, and
    splits input_string text into list
    of words.
    
    (Code from A3-Chatbot)
    
    Parameters
    ----------
    input_string: string that
    is going to become text the msg
    the chatbot interprets
    
    Returns
    -------
    out_list : list
    list whose elements are lowercase strings of
    individual words
    """
    
    # make the string lowercase
    temp_string = input_string.lower()
    
    # remove punctuation
    temp_string_2 = remove_punctuation(temp_string)
    
    # split up the string list of individual words
    out_list = temp_string_2.split()
    
    return out_list



def should_end_chat(input_list):
    """ends chat in response to "quit input".
    
    (Code from A3-Chatbot)
    
    Parameters
    ----------
    input_list: list
    
    string that
    went through prepare text function
    and became a list of lowercase strings
    
    Returns
    -------
    output : boolean
    if user inputs quit (if quit is in the input_list), 
    function outputs True
    if not, function outputs False
    """
    
    if "quit" in input_list :
        output = True
        
    else:
        output = False
        
    return output



# Lists chatbot will use to evaluate inputs and outputs

# chatbot will look at start to see if user inputs greeting
GREETINGS_IN = ['hello', 'hi', 'hey', 'hola', 'welcome', 'bonjour', 
                'greetings', "what", "should", "I", "do", "?"]
# first output if user inputs greeting
# prompt user to choose a path (hungry, bored, anxious, or lonely)
GREETINGS_OUT = ["Are you hungry, are you bored, are you anxious, are you lonely?"]

# the following lists are for after the user chooses a path
# by answering the above question

# User inputs that prompt Hungry path
HUNGRY_IN_1 = ["hungry", "first", "1"]
# Hungry path prompt to get user to choose from two new paths
# (eating in or eating out)
HUNGRY_OUT_1 = ["Looks like you are looking for a place to eat. Would you rather eat out or eat in?"]

# If user responds with in, it will prompt the in part
# of the Hungry path
HUNGRY_IN_2 = ["in"]
# Final response: website with 101 recipes
# followed by a number corresponding to a recipe
HUNGRY_OUT_2 = ["Pick one of the recipes from the following website to cook:"
                "https://www.countryliving.com/food-drinks/g648/quick-easy-dinner-recipes/"
                "?utm_source=google&utm_medium=cpc&utm_campaign=arb_ga_clv_d_bm_prog_org_us_g648&gclid"
                "=CjwKCAiAvJarBhA1EiwAGgZl0IBB6DxVXnzah9_ADYDS5SX8Ii0lF0L3XFfbsr9w2o0ojMePWrg6ehoCCigQAvD_BwE"
               ]
HUNGRY_OUT_2_CONT = ["Pick the recipe with the following number: "]

# User inputs the prompt of out path within the Hungry path
HUNGRY_IN_3 = ["out"]
# Final response: prompts user to go eat out a restaraunt
# of randomly selected type
HUNGRY_OUT_3 = ["Eat at the most convenient restaraunt with the following type: "]
HUNGRY_OUT_3_CONT = ["Indian", "Thai", "Jamaican", "American", "Chinese", "Hibachi", "Breakfast"]


# User inputs that prompt Bored path
BORED_IN_1 = ["bored", "second", "2"]
# Final response: prompts user to travel 1 mile in randomly chosen direction
BORED_OUT_1 = [
    "Travel exactly 1 mile in the following cardinal direction (or go as far as you safely can) "
    "and see what's up: "
]
BORED_OUT_1_CONT = ["North", "East", "South", "West"]


#User inputs that prompt Anxious path
ANXIOUS_IN_1 = ["anxious", "stressed"]
# Final response: prompts user to do random meditation
ANXIOUS_OUT_1 = ["Looks like you need a meditation. Do the following activity: "]
ANXIOUS_OUT_1_CONT = ["in for four, hold for seven, out for eight",
                      "visualize yourself in your happy place",
                      "stare at and become immersed in 1 thing in nature"]


# User inputs that prompt Lonely path
LONELY_IN_1 = ["lonely", "last", "alone"]
# Final response: prompts user to do random activity in public
# to make some friends because that's what public embarrassment does
# or something
LONELY_OUT_1 = [
    "Do or try to learn the following activity in public, "
    "in the same place, "
    "for at least three days in a row: "
]
LONELY_OUT_1_CONT = ["play an instrument", "moonwalk", "meditate"]



def check_greeting(msg, ins):
    """checks if first response is greeting 
    (original function)
    
    Parameters
    ----------
    msg: string that user inputted
    ins: list of previous inputs
    
    Returns
    -------
    greet_collect_message : string
    string to prompt user to input
    greeting
    
    answer: None
    if the message is in GREETINGS_IN,
    no extra greeting need be solicited
    """
    
    greet_collect_message = "Please input a greeting"
    
    # verify first user message is greeting
    # this function is further explained when it is used
    # in the chatbot function below
    if len(ins) == 1  and msg not in GREETINGS_IN and msg != "quit":
        return greet_collect_message
    
    else:
        return None



def change_greeting(ins):
    """adds new greeting to GREETINGS_IN.
    (original function)
    
    Parameters
    ----------
    ins: list of previous inputs
    
    Returns
    -------
    None : Nonetype
    if ins[1] is a new greeting,
    then append new greeting to GREETINGS_IN.
    Otherwise, return None just in case there
    isn't a ins[1] yet or if ins[1] is an acceptable
    greeting (no need for repeats in GREETINGS_IN)
    """
    
    # prevent index error using try and except
    try:
        if ins[1] not in GREETINGS_IN:
            GREETINGS_IN.append("".join(ins[1]).lower())
            
    except:
        return None
    
    
    
    
# the chatbot function
# while this function shares some similarities
# with the chatbot function in A3,
# it has a few disctinct differences in methods,
# how it records inputs and outputs, 
# the multitude of options, and how it can
# append inputted messages into acceptable inputs for
# a given situation
def what_should_i_do():
    """this function is a chatbot that tells you what to
    do if you are hungry, bored, anxious,
    and lonely based on what you input 
    into the function's msg variable. 
    It can also learn new greetings
    (original function)
    
    Parameters
    ----------
    None 
    (but it takes anything that 
    can be converted into strings and put into lists.
    That said, it, practically, only
    should take numbers and strings)
    
    Returns
    -------
    None
    (but it outputs, via printing, strings, which are, 
    generally, randomly selected
    from acceptable output lists)
    """
    
    # variable to regulate while loop
    chat = True
    
    # lists to record inputs and outputs
    outs = []
    ins = []
    
    # first user prompt from chatbot
    query = "Give me a greeting, if you dare :"
    
    # unless told otherwise, we want the chatbot
    # to be continously running, so we use a loop
    while chat:
        
        # get user input   
        msg = input(query)
        
        
        
        # prepare the input message
        msg = prepare_text(msg)
        
        # record latest msg
        ins.append(msg)
        
        out_msg = None
       
    
        # end chat if user says quit    
        if should_end_chat(msg):
            break
            
            
        # (299) verify first input is greeting
        # (300) if it isn't, ask user for greeting
        # (301) record interaction in outs list
        # (302) make sure query doesn't repeat the first prompt
        if check_greeting(msg, ins) and len(ins) == 1:
            out_msg = check_greeting(msg, ins)
            outs.append(out_msg)
            query = ""
            
            
        # collect user's greeting if it isn't already collected
        # prompt user to go to anxious, lonely, hungry, or bored path
        # record interaction to out list
        # and, like before, make sure query doesn't repeat the first prompt
        if outs[0] == "Please input a greeting" and len(ins) == 2 and len(outs) == 1:
            change_greeting(ins)
            out_msg = "".join(GREETINGS_OUT)
            outs.append(out_msg)
            query = ""
            

        
        
        # the following conditionals follow the same format
        # if the user inputs something that is in a respective path's in list,
        # then output the path's outlist along with an randomly generated choice from the out_cont list
        # record output in outs list
        # reset the query to nothing (if necessary)
        # end the chat once all the path's responses are generated
        if any(word in msg for word in GREETINGS_IN):
            out_msg = random.choice(GREETINGS_OUT)
            outs.append(out_msg)
            query = ""

        if any(word in msg for word in HUNGRY_IN_1):
            out_msg = "".join(HUNGRY_OUT_1)
            outs.append(out_msg)
    

        if any(word in msg for word in HUNGRY_IN_2):
            out_msg = random.choice(HUNGRY_OUT_2) + "/t" + " " + random.choice(HUNGRY_OUT_2_CONT) + str(random.randint(1,101))
            outs.append(out_msg)
            chat = False
            

        if any(word in msg for word in HUNGRY_IN_3):
            out_msg = random.choice(HUNGRY_OUT_3) + random.choice(HUNGRY_OUT_3_CONT)
            outs.append(out_msg)
            chat = False

        if any(word in msg for word in BORED_IN_1):
            out_msg = "".join(BORED_OUT_1) + random.choice(BORED_OUT_1_CONT)
            outs.append(out_msg)
            chat = False
            

        if any(word in msg for word in ANXIOUS_IN_1):
            out_msg = "".join(ANXIOUS_OUT_1) + random.choice(ANXIOUS_OUT_1_CONT)
            outs.append(out_msg)
            chat = False
            

        if any(word in msg for word in LONELY_IN_1):
            out_msg = "".join(LONELY_OUT_1) + random.choice(LONELY_OUT_1_CONT)
            outs.append(out_msg)
            chat = False
        
        
        # print the out message given there is one
        if out_msg is not None:
            print('OUTPUT:', out_msg)
        
    