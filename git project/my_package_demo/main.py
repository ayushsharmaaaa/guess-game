from my_package import greetings
import pandas as pd

print(greetings.say1("ayush"))
data={
    "students":["Ayush","Naman","Sharavan"],
    "marks":[100,99,100]
}
df=pd.DataFrame(data)
print("\nStudents Data:\n",df)