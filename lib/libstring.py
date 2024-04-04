import re


class LibString:
    @staticmethod
    def extractstringname(stringnames):
        matches = re.findall(r"\((S\.\$)\.(\w+)\)", stringnames)
        return [match[1] for match in matches]