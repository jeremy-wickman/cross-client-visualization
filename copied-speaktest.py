import os
victory_speech = raw_input("What do you want to say? ")
victory_speech_config = "say -v 'Alex' %s" %victory_speech
os.system(victory_speech_config)
