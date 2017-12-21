from nltk.stem import SnowballStemmer
stemmer = SnowballStemmer('english')

string = "something i am writing" 
string_before_Stem = string.split()
print(string_before_Stem)


string = stemmer.stem(string)
string = string.split()
print(string) 

