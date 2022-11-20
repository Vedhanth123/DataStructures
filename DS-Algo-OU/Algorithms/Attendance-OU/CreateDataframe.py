import pandas as pd

date1 = input()

# create a dataframe
df = {
    date1: [x-x for x in range(72)],
}


df = pd.DataFrame(df, index = [f"1005-21-7290{x}" for x in range(1, 88) if (x <= 65 or x >= 81)])

print(df.head())
df.to_csv("Attendance.csv")
