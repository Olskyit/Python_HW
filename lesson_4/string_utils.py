class StringUtils:
    def capitalize(self, string: str) -> str:
        return string.capitalize()

    def trim(self, string: str) -> str:
        whitespace = " "
        while string.startswith(whitespace):
            string = string.removeprefix(whitespace)
        return string

    def contains(self, string: str, symbol: str) -> bool:
        try:
            return string.index(symbol) > -1
        except ValueError:
            return False

    def delete_symbol(self, string: str, symbol: str) -> str:
        if self.contains(string, symbol):
            return string.replace(symbol, "")
        return string
