class TableData:
    def __init__(
        self,
        x: list[str],
        value_data: dict[str, list[int]],
        name: str,
        value_label: str,
        isLinear: bool,
    ) -> None:
        self.x: list[str] = x
        self.value_data: dict[str, list[int]] = value_data
        self.name: str = name
        self.isLinear: bool = isLinear
        self.value_label = value_label
