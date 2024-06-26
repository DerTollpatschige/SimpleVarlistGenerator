import re


class LibVar:
    @staticmethod
    def extractvarname(varnames):
        matches = re.findall(r"\((S\.L|L\.L)\.(\w+)\)", varnames)
        return [match[1].lower()for match in matches]
