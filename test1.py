import math
import sys
import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello " + str(who_to_greet)
    return greeting


print(greet("World"))
print(greet("Buru"))
print(greet("Git0"))

r = requests.get("https://google.com")
print(r.status_code)
print(r.ok)
