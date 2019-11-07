text = "X-DSPAM-Confidence:    0.8475";
text.strip()
loc=text.find('0.8475')
num=text[loc:(loc+len('0.8475'))]
num=float(num)
print(num)