try:
    rez = 10/2
except ZeroDivisionError:
    print("Oops, you can't divide with zero.")
else:
    print("pjestimi eshte realizuar me sukses")
finally:
    print("ke mrri deri te line 8")

frutat = {
    "mollat":5,
    "banane":7,
    "portokalla":3
}

try:
    print(frutat["dredhezat"])
except KeyError:
    print("the key does not exist in the directory")

text="this is not a number"

try:
    text_to_int= int(text)
except Exception as m:
    print("ka ndodh nje error", m)
finally:
    print("hej ke mrri deri te line 26")
