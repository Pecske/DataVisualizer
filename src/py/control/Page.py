from control.Section import Section


class Page:

    def __init__(self) -> None:
        self.sections: list[Section] = list()

    def add_section(self, section: Section) -> None:
        self.sections.append(section)
