import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

data_beuth = pd.read_csv("https://raw.githubusercontent.com/edlich/eternalrepo/master/DS-WAHLFACH/dsm-beuth-edl-demodata-dirty.csv")

# drop all rows with more then one NaN as data quality would be poor otherwise
cleaned_data = data_beuth.dropna(axis=0, thresh=1)
# fullname is same information as first_name and last_name so for normalized dataframe fullname is dropped
cleaned_data = cleaned_data.drop(['id', 'full_name'], axis=1)
# drop all duplicates
cleaned_data = cleaned_data.drop_duplicates()

# replace 'old' with max age in columns
cleaned_data['age'] = cleaned_data['age'].replace('old', pd.to_numeric(cleaned_data['age'], errors='coerce').max())
# we consider each age value should be positive integer values
cleaned_data['age'] = pd.to_numeric(cleaned_data['age'], errors='coerce', downcast='integer').abs()

# replace NaN with empty string
cleaned_data = cleaned_data.fillna('')
print(cleaned_data)
