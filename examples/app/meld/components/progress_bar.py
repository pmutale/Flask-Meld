
from flask_meld import Component, listen


class ProgressBar(Component):
    progress = 50

    @listen("progress")
    def set_progress(self, progress):
        self.progress = progress
