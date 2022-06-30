import pandas
df = pandas.read_csv('testCSV2.csv',
            index_col='Employee',
            header=0,
            names=['Employee', 'Department'])
df.to_csv('testCSV2write.csv')
