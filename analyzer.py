import re
import math
def entropy(password):
    charset = 0
 if re.search(r"[a-z]", password):
        charset += 26
if re.search(r"[A-Z]", password):
        charset += 26
if re.search(r"[0-9]", password):
        charset += 10
if re.search(r"[^A-Za-z0-9]", password):
        charset += 32
 if charset == 0:
        return 0
return len(password) * math.log2(charset)
def check strength(password):
    score = 0
if len(password) >= 8:
        score += 1
if re.search(r"[A-Z]", password):
        score += 1
if re.search(r"[a-z]", password):
        score += 1
if re.search(r"[0-9]", password):
        score += 1
if re.search(r"[^A-Za-z0-9]", password):
        score += 1
if score <= 2:
        return "Weak"
elif score <= 4:
        return "Medium"
   else:
return "Strong"
