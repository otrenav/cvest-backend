
class TextProcessor:

    @staticmethod
    def floatify(string, default=0):
        try:
            return float(string)
        except:
            return default
