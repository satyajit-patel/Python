# s = input("enter input"); # hi there how are you
s = "hi there how are you";

print(s);
if(s.startswith("hi")) :
    print("Hey")

#       join => joins into a string
print(",".join(s)); 
print("->".join(["hi", "I am", "batman"]));

#       split => splits the string into list (space is bydefault)
print(s.split());
print("hi$there$how$are$you".split("$"));

# remove white space with strip
print("       hey there     ".strip());

# spam.strip('ampS') means
# removes all leading and trailing occurrences of any characters 
#in the string 'ampS'.

print("SpamSpamBaconSpamEggsSpamSpam".strip("ampS")); # BaconSpamEggs

#                       count
sentence = 'one sheep two sheep three sheep four'
print(sentence.count("sheep"));
print(sentence.count("sheep", 10)); # (target, startIndex, endIndex+1)
print(sentence.count("e", 0, 3));

#                       replace
print(sentence.replace("one",  "ONE"));
print(sentence.replace("sheep", "GOAT", 2)); # replaces only first 2 occurance