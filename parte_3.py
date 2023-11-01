import pandas as pd
from datasets import load_dataset
dataset = load_dataset("mstz/heart_failure")
df = pd.DataFrame(dataset['train'])
print(df.dtypes)

fumadores_por_genero = df.groupby(['is_male', 'is_smoker']).size().unstack()
fumadores_por_genero = fumadores_por_genero.fillna(0)

print(fumadores_por_genero)

