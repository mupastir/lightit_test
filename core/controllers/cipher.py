import csv
import os

from core.constants import CSV_FILEPATH


class Cipher:

    def __init__(self, rot_index, mode, rough_text):
        self._frequency_rough = {}
        self._rot_index = int(rot_index)
        self._mode = mode
        self._rough_text = rough_text

    def get_result(self):
        result = self._encrypt() if self._mode == 'encrypt' \
            else self._decrypt()
        return {'result': result,
                'frequency_rough': self._frequency_rough}

    def _decrypt(self):
        self._rot_index = -self._rot_index
        return self._encrypt()

    def _encrypt(self):
        result = ""
        for i in range(len(self._rough_text)):
            char = self._rough_text[i]

            # Skip non-alphabetic symbol
            if not char.isalpha():
                result = result + char
            # Encrypt uppercase characters
            elif char.isupper():
                result += chr((ord(char) + self._rot_index - 65) % 26 + 65)
                self._add_to_frequency(char.lower())
            # Encrypt lowercase characters
            else:
                result += chr((ord(char) + self._rot_index - 97) % 26 + 97)
                self._add_to_frequency(char)
        self._write_to_csv(result)
        return result

    def _write_to_csv(self, result_text):
        if os.path.isfile(CSV_FILEPATH):
            csv_writer = csv.writer(open(CSV_FILEPATH, 'a'),
                                    lineterminator='\n')

        else:
            csv_writer = csv.writer(open(CSV_FILEPATH, 'w'),
                                    lineterminator='\n')
            csv_writer.writerow(["MODE",
                                 "ROTATION",
                                 "ROUGH TEXT",
                                 "RESULT TEXT"])
        csv_writer.writerow([self._mode,
                             self._rot_index,
                             self._rough_text,
                             result_text])

    def _add_to_frequency(self, char):
        if char in self._frequency_rough:
            self._frequency_rough[char] += 1
        else:
            self._frequency_rough[char] = 1
