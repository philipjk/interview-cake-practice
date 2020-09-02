class WordCloudData(object):

    def __init__(self, input_string):

        # Count the frequency of each word

        self.words_to_counts = {}

    def string_to_list(self, input_string):
        outl = []
        word = []
        for char in input_string:
            if char != ' ':
                word += char
            else:
                outl.append()
                word = []
        for word in outl:
