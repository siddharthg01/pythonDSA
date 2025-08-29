import re
pattern =r"[a-z]+Phone"
text ='''Apple event: The iPhone aPhone 15 and iPhone 15 Pro models have finally been announced. While the India price starts at Rs 79,900, the company has revealed that the price for the US market will start from $799.'''
#match=re.search(pattern,text)
matches=re.finditer(pattern,text)
for match in matches :
    print(match)