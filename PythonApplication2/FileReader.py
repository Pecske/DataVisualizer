import pandas as pd

pd.set_option("display.max_rows",100)
pd.set_option("display.max_columns",100)

class FileReader:
    delimeter : str = ";"
    encoding : str = "ISO-8859-1"

    def __init__(self,path) -> None:
        self.path : str = path
    
    def read_from_csv(self) -> pd.DataFrame:
        df: pd.DataFrame = pd.read_csv(self.path,delimiter=self.delimeter,skiprows=1,encoding=self.encoding)
        return df.dropna()