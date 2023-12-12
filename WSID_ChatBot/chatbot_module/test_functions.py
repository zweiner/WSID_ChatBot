from functions import remove_punctuation, prepare_text, should_end_chat, check_greeting, change_greeting


def test_remove_punctuation():
    
    assert callable(remove_punctuation)
        
    #does punctuation get removed
    assert remove_punctuation("..!!?@") == ""

    # does just punctuation get removed
    # does it keep spaces
    assert remove_punctuation("l.l.l.l. ") == "llll "
        
    
        
        
        
def test_prepare_text():
    
    assert callable(prepare_text)
    
    # test lowercase method implementation
    assert prepare_text("HI, I'M ZACH!") == ["hi","im", "zach"]

    # test remove punctuation function implementation
    assert prepare_text("!!!?..") == []

    # test split method implementation
    assert prepare_text("hi hi hi") == ["hi","hi","hi"]
        
   

        
        
def test_should_end_chat():
    
    assert callable(should_end_chat)
  
    # does it return True if list is quit
    assert should_end_chat(["quit"]) == True

    # does it return True if quit in list
    assert should_end_chat(["blah", "blah","quit"]) == True

    # does it return False if quit not in list
    assert should_end_chat(["hi","hi","hi"]) == False
        
    
        
# following list, variable, and append method necessary for following test      
GREETINGS_IN = ['hello', 'hi', 'hey', 'hola', 'welcome', 'bonjour', 
                'greetings', "what", "should", "I", "do", "?"]

GREETINGS_IN_MOD = GREETINGS_IN

GREETINGS_IN_MOD.append("aloha")



        
    
def test_check_greeting():
    
    assert callable(check_greeting)
  
    # does it return None if first input message is a greeting
    assert check_greeting(["hello"],[]) == None

    # does it return None if quit in list
    assert check_greeting(["quit"],[]) == None

    # does it return the message prompting the user to input a greeting
    assert check_greeting(["yo"], ["no greeting"]) == "Please input a greeting"
                                                  
        
   
        
        
def test_change_greeting():
    

     
    # does it append GREETINGS_IN list upon seeing a new greeting ("aloha")
    change_greeting(["not a greeting", "aloha"])

    assert GREETINGS_IN_MOD == GREETINGS_IN

    # after it appends GREETINGS_IN list, will it return None
    # and accept the newly appended greeting as a valid one if aloha
    # (the new greeting) is inputted later on
    assert change_greeting(["not a greeting", "aloha"]) == None
       
    
 
        
 
    