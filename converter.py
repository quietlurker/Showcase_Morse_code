from morse_code import morse_code


class Converter:

    def to_morsecode(self, input_text):
        '''converts input text to morse code
        includes polish letters
        returns ? for unknown string'''
        output = ""
        for i in input_text:
            if i in morse_code:
                output += morse_code[i]
            else:
                output += "?"
            output += " "
        return output
