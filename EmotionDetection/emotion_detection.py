import nltk
import pandas as pd
from nltk import word_tokenize
from nltk.stem.snowball import SnowballStemmer
import requests
from LeXmo import LeXmo

t= """From the beginning, she had sat looking at him fixedly.
  As he now leaned back in his chair, and bent his deep-set eyes upon her in his turn,
  perhaps he might have seen one wavering moment in her, 
  when she was impelled to throw herself upon his breast,
  and give him the pent-up confidences of her heart.
  But, to see it, he must have overleaped at a bound the artificial barriers he had for many years been erecting, 
  between himself and all those subtle essences of humanity which will elude the utmost cunning of algebra
  until the last trumpet ever to be sounded shall blow even algebra to wreck.
  The barriers were too many and too high for such a leap. With his unbending,
  utilitarian, matter-of-fact face, he hardened her again;
  and the moment shot away into the plumbless depths of the past,
  to mingle with all the lost opportunities that are drowned there."""
# Charles Dickens, Hard Times


def emotion_detection(text_to_analyze):
    emotion = LeXmo.LeXmo(text_to_analyze)
    emotion.pop('text', None)

    max_value = max(emotion['anger'], emotion['disgust'],emotion['fear'],emotion['joy'],emotion['sadness'])
    dominant_emotion = ''
    for emo,value in emotion.items(): 
        if emo == 'anger' and max_value == value:
            dominant_emotion = 'anger' 
            break
        elif emo == 'disgust' and max_value == value:
            dominant_emotion = 'disgust' 
            break
        elif emo == 'fear' and max_value == value:
            dominant_emotion = 'fear' 
            break
        elif emo == 'joy' and max_value == value:
            dominant_emotion = 'joy' 
            break
        elif emo == 'sadness' and max_value == value:
            dominant_emotion = 'sadness' 
            break
        
  

    return {'anger': emotion['anger'], 
           'disgust': emotion['disgust'],
           'fear': emotion['fear'],
           'joy': emotion['joy'],
           'sadness': emotion['sadness'],
           'dominant_emotion' :dominant_emotion }


# result = emotion_detection("""I feel disgusted just hearing about this""")
# print(result)