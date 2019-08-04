from flask import render_template


class Cipher:

    def __init__(self):
        self.main_page_legend = 'Cesar cipher site. Please choose rotate and case: code or decode <br>' \
                                'After that enter text in the left field'

    def main_page(self):
        return render_template("index.html", legend=self.main_page_legend)
