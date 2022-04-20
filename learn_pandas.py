import pandas

df_1 = pandas.DataFrame({"name": ["a", "b", "c"], "value": [100, 200, 300]})
df_2 = pandas.DataFrame({"name": ["b", "c", "d"], "value": [100, 200, 300]})
df_3 = pandas.concat([df_1, df_2])
df_4 = pandas.concat([df_1, df_2], axis=1)
df_4.columns = ["n1", "v1", "n2", "v2"]
print(df_1)
print(df_2)
print(df_3)
print(df_4)
