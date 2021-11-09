import pandas as pd
sirenaExport = pd.read_fwf('data/Sirena-export-fixed.tab')
sirenaExport.to_csv(r'data/Sirena-export-fixed.csv', index_label='id')