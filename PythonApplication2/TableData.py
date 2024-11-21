class TableData:
    def __init__(
        self,
        x: list[str],
        y: list[list[int]],
        name: str,
        isLinear: bool,
        legend: list[str] = None,
    ) -> None:
        self.x: list[str] = x
        self.y: list[list[int]] = y
        self.name: str = name
        self.legend: list[str] = legend
        self.isLinear: bool = isLinear
