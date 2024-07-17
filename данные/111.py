import pandas
pandas.set_option("display.max_columns",None)
pandas.set_option("display.max_rows",None)
data=pandas.read_csv("heats.csv")
data_new=data.sort_values('time', ascending=False)
print(data)



