"""
what we have to do is to create a dictionary, similar to the real-world dictionary. There is no limit to the definition you provide to any word as this exercise is just for your practice.

The details and functionalities that are essential and must be present are:

User will give a word as an input. Suppose that the word is present in your dictionary along with its definition or meaning.
The program will print the meaning or definition of that word.
"""

dic = {
    "ambigue": "An ambiguous statement or expression.",
    "Anglosphere": "	English-speaking countries considered collectively",
    "anti-suffragism": "Opposition to the extension of the right to vote in political elections to women; the political movement dedicated to this.",
    "Aperol":	"A proprietary name for  an orange-coloured Italian aperitif flavoured with gentian, rhubarb, and a variety of herbs and roots."
}
print("What word you want")
a = input()
print("The meaning of", a , "is")
print(dic[a])
