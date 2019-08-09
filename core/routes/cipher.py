from flask import render_template, json, request
from core.controllers.cipher import Cipher


class CipherRoute:

    def __init__(self):
        self.main_page_legend = 'Cesar cipher site. Please choose rotate and case: encrypt or decrypt <br>' \
                                'After that enter text in the left field'

    def main_page(self):
        return render_template("index.html", legend=self.main_page_legend)

    def cipher(self):
        rot_index = request.form['rot-index']
        mode = request.form['mode']
        rough_text = request.form['rough-text']
        cipher = Cipher(rot_index=rot_index, mode=mode, rough_text=rough_text)
        return json.dumps(cipher.get_result())
