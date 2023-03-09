import spacy 

# Using advanced language model
nlp = spacy.load('en_core_web_md') 

# Variable store to word.  To be used to compare with one another
word1 = nlp( "cat" ) 
word2 = nlp( "monkey" ) 
word3 = nlp( "banana" ) 

# Print out similarity between the different words 
print(word1.similarity(word2)) 
print(word3.similarity(word2)) 
print(word3.similarity(word1))


tokens = nlp('cat apple monkey banana') 

# Compares the words with one another
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# Variable containing a sentence
sentence_to_compare = "Why is my cat on the car"

# List containing a list of sentence
sentences = [ "where did my dog go" , "Hello, there is my car" , "I\'ve lost my car in my car" , "I\'d like my boat back" , "I will name my dog Diana" ]

model_sentence = nlp(sentence_to_compare)

# Compares sentence in sentence_to_compare with sentences in the list
for sentence in sentences: 
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)



# ------------- Notes ---------------- #
"""
The similarities between cat, monkey and banana

Cat and Monkey have a similarity score of 0.59299. The highest score out of the three.
They seem to be similar, which may be due to the fact that they are both animals and mammals.

Cat and banana have a similarity score of 0.223588 which is a low score. They are not similar and has the lowest score.
This may be due to the fact that cats are carnivorous animals. They tend to eat other animals.

Monkey and Banana have a similarity score of 0.40415. They are similar.
This may be due to the fact that most monkeys are omnivores and are associated with eating bananas.
"""


# ------------- Notes for the Example.py---------------- #
"""
When using model 'en_core_web_md' the similarity scores tends to be higher than the score for 'en_core_web_sm'. The model 'en_core_web_md' generally has a higher 
degree of similarity for all three comparisons.  That's comparison for complaints, recipe instruction, and recipe instruction compared with a complaint.

Also, when using the model 'en_core_web_sm' a warning appeared notifying users that similarity judgement is based on the tagger, parser and NER.
It doesn't come with its own word vectors unlike the higher model 'en_core_web_md', which makes it a lesser useful similarity judgement.

For 'en_core_web_sm' you can manually add vector words if one chooses to.
"""


################## My Example ################################
# Variable store to word.  To be used to compare with one another
word_a = nlp( "Car" ) 
word_b = nlp( "Bike" ) 
word_c = nlp( "Plane" ) 

# Print out similarity between the different words 
print(word_a.similarity(word_b)) 
print(word_c.similarity(word_b)) 
print(word_c.similarity(word_a))


"""
The similarities between Car, Bike and Plane

Car and bike have a similarity score of 0.65451. The highest score. All three words are a means of transportation.
The high similarity between car and bike, may due to the fact that they are mainly driven by one person and transport people on roads.

Plane and bike have a similarity score of 0.46065. They seem to be similar, which may be due the fact that they are 
both form of transportation. It has the lowest score, which may be because they carry less passengers than plans and cars.

Car and Plane have a similarity score of 0.49651. They seem to be similar.
Again, they are a mode of transport.
"""

###########################################################################################