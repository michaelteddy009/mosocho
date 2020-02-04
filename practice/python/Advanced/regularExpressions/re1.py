import re

print('\tMichael')
print(r'\tMichael')  #this will return a raw string includint the \t which in the first case is interpreted as tab
textToSearch = "abcdefgijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ"
pattern = re.compile(r'abc')  #here we specify our pattern
matches = pattern.finditer(textToSearch)

for match in matches:
	print(match)

#\. will look for where the fullstop is eg re.compile(r'\.') this is known as character escape

#the following serches for an email

email = 'michael.com'

pattern = re.compile(r'michael\.com')
matches = pattern.finditer(email)
for match in matches:
	print(match)

#\d for digit, \w for word, \s for whitespace, \b word boundary, ^ and $ for biggining and end of a string.


numbers = "123-456-632, 876.382.294"

pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d')
matches = pattern.finditer(numbers)
for match in matches:
	print(match)

#[1-5] meaning 1 to 5
#r'[^b]at' Matches everything that ends with at but doesn't start with a b
"""
We have the following quantifiers
		* - 0 or more
		+ - 1 or more
		? - 0 or 1
		{3} - Exact 3   eg \d{3} to mean the first 3 digits
		{3, 4} - range of numbers(minimum, maximum)
"""

#if we want to match Mr. Smith and Mr Smith we do something of this sort
#r'Mr\.?' the ? sign makes the . an optional search merit
#We can also a group in the following example
#r'M(s|r|rs)'  this generealises and searches for either Ms, Mr or Mrs


#we can also use group() to find the groups defined in the regular expression
#match.group(1)
#subbed =pattern.sub(\2\3, numbers) this makes copies with only the specified groups
#finditer returns the expression with extra information but findall will return matches as a list of strings and if it's matching groups then it will only return the groups
#pattern.match("Sentense")  the match method only serches sentense as the first string  but if we want to look in the entire string we use search method
#in re.compile() we can pass the following flags as arguments re.I of re.IGNORECASE