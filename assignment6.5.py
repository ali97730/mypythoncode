text = "X-DSPAM-Confidence:    0.8475"
start= text.find('0')
stringvalue = text[start: start+7]
floatvalue =float(stringvalue)
print(floatvalue)
