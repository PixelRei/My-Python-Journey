#len() returns the lenght of a string or even of a list
string = "ciao kebab"
print(len(string))

#for upper case we use upper()
print(string.upper()) #of course it's the same for lower

#using format
string1 = "io {} {}"
print(string1.format("bevo", "kefir alla fragola")) #the placeholders get replaced by the parameters
#strip == trim() in other languages, it removes whitespaces

#replace, to replace chars
print(string.replace("k", "x")) #the first is a letter of the sentence, the second is the new one

#split() just splits a string returning a list
print(string.split(" ")) #removes the whitespace (in this case) and returns the array