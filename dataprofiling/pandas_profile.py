# get the latest version of pandas_profiling
from pathlib import Path
import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport

if __name__ == "__main__":
# data set location http://eforexcel.com/wp/downloads-18-sample-csv-files-data-sets-for-testing-sales/
    df=pd.read_csv("/home/prasad/Downloads/sales_records.csv")

    # Prepare missing values
    df = df.replace("\\?", np.nan, regex=True)

    # changing date fields from categorical to date
    df['Order Date'] = pd.to_datetime(df['Order Date'],infer_datetime_format=True )
    df['Ship Date'] = pd.to_datetime(df['Ship Date'],infer_datetime_format=True )

# using custom cofig yaml file to speed up the process , ignoring Correlations and Interactions
    profile = ProfileReport(
        df,
        config_file="/home/prasad/Downloads/sales_config.yaml",
        explorative=True,
        minimal=False)
    profile.to_file(Path("sales_report.html"))