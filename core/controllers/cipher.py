class Cipher:

    def __init__(self, rot_index, mode, rough_text):
        self._frequency_rough = {}
        self._rot_index = int(rot_index)
        self._mode = mode
        self._rough_text = rough_text
        self._modes = {
            'encrypt': self._decrypt(-self._rot_index),
            'decrypt': self._decrypt(self._rot_index)
        }

    def get_result(self):
        return {'result': self._modes[self._mode],
                'frequency_rough': self._frequency_rough}

    def _decrypt(self, rot):
        result = ""
        for i in range(len(self._rough_text)):
            char = self._rough_text[i]

            # Skip non-alphabetic symbol
            if not char.isalpha():
                result = result + char
            # Encrypt uppercase characters
            elif char.isupper():
                result += chr((ord(char) + rot - 65) % 26 + 65)
                self._add_to_frequency(char.lower())
            # Encrypt lowercase characters
            else:
                result += chr((ord(char) + rot - 97) % 26 + 97)
                self._add_to_frequency(char)
        return result

    def _add_to_frequency(self, char):
        if char in self._frequency_rough:
            self._frequency_rough[char] += 1
        else:
            self._frequency_rough[char] = 1
