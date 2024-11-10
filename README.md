Lyric Generator With Graph

Co-Creators:

 -DavidEmFodor
 
 -VRuizInformatica

This project generates lyrics from text data using a graph-based approach. 
It reads text from .txt files, creates nodes and edges between words, and uses a random weighted selection to generate new sequences of words, 
resembling song lyrics. The output can be spoken using a text-to-speech engine (pyttsx3), adding a vocal aspect to the generated lyrics.

Text Cleaning: Unwanted characters and special symbols are removed from the text files. Each line is normalized and stripped of diacritics for better processing.
Graph Structure: Words in the text are stored as nodes, with edges representing transitions between words. The edges are weighted to reflect how often word pairs occur together.
Randomized Lyric Generation: A starting node is selected randomly, and new nodes are chosen based on the weight of their edges, allowing for varied and unpredictable lyric output.
Text-to-Speech Integration: After generating the lyrics, the program uses the pyttsx3 library to read them aloud.
Supports 10 Input Files: The program reads up to 10 .txt files, and processes their content into the graph structure for lyric generation.

 Dependencies:
    Python 3.x
    unidecode
    pyttsx3 
    re
