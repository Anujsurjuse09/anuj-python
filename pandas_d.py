# df.head() ---first five rows
# df.tail() ---last five rows
# df.info() ---
# df.describe() ---statistical summary
# df.shape()---rows,coloumn
# df.column---coloumn
# df.random---

# handling missing data
# df.isnull(sum)---identify missing 
# df.dropna()---drop rows with missing values
# df.fillna(0)---
# df.fillna(df.mean)---fill with clm mean

import numpy as np
import pandas as pd

ser = pd.Series()
print("pandas series:\n",ser)

data = np.array(['g','e','e','k','s'])

ser = pd.Series(data)
print("pandas series:\n",ser)



import pandas as pd

df = pd.DataFrame()
print(df)

a = ['Geen','For','Geens','is','portal','for','Geens']

df = pd.DataFrame(a)
print(df)




