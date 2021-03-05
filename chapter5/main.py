#gets the daily and weekly weather reports
from  chapter5 import daily,weekly

print ("Daily forecast:",daily.forecast())
print("weekly forecast:")
for number, outlook in enumerate(weekly.forecast(), 1):
    print(number, outlook)
