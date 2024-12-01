from abc import abstractmethod
from typing import Any
from pandas import DataFrame
from data.BaseData import BaseData
from data.TableData import TableData
from utils.ItemName import ItemName
import matplotlib.pyplot as plt
import numpy as np


class BaseDataService:

    def __init__(self, df: DataFrame, style: str = "fivethirtyeight") -> None:
        self.style = style
        self.base_data_map: dict[str, BaseData] = self.map_df_to_base_data(df)

    def __get_linear_regression_values(
        self, xValues: list[int], yValues: list[int]
    ) -> np.poly1d:
        coef = np.polyfit(xValues, yValues, 1)
        return np.poly1d(coef)

    def __map_columns_to_dummy_values(self, column_names: list[str]) -> list[int]:
        new_index: int = 0
        column_values: dict[str, int] = dict()
        for name in column_names:
            if name not in column_values:
                column_values[name] = new_index
                new_index += 1
        return list(column_values.values())

    @abstractmethod
    def map_df_to_base_data(self, df: DataFrame) -> dict[str, BaseData]:
        pass

    @abstractmethod
    def map_base_data_to_table(self, filters: dict[ItemName, Any]):
        pass

    def show_plot(self, table_data: TableData) -> None:
        plt.figure(table_data.name.capitalize())
        plt.title(table_data.name.capitalize())
        plt.tight_layout()
        plt.ylabel(table_data.value_label)
        plt.style.use(self.style)
        for label, yValues in table_data.value_data.items():
            plt.plot(table_data.x, yValues, label=label)
            if table_data.isLinear:
                dummyX: list[int] = self.__map_columns_to_dummy_values(table_data.x)
                poly: np.poly1d = self.__get_linear_regression_values(dummyX, yValues)
                plt.plot(dummyX, poly(dummyX))

        plt.legend()
        plt.show()
