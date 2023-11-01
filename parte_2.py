import pandas as pd
from datasets import load_dataset

dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]


df = pd.DataFrame(data)

df_perecieron = df[df["is_dead"] == 1]
df_no_perecieron = df[df["is_dead"] == 0]


promedio_edad_perecieron = df_perecieron["age"].mean()
promedio_edad_no_perecieron = df_no_perecieron["age"].mean()


print("Promedio de edades de personas que perecieron:", promedio_edad_perecieron)
print("Promedio de edades de personas que no perecieron:", promedio_edad_no_perecieron)
