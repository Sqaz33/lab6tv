import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from utils.paths import resolve_path
from widgets import TaskView
from tasks import labs, lab_names


class LabsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._last_lab_num = None
        uic.loadUi(resolve_path('ui/window.ui'), self)
        self.taskSelect.currentIndexChanged.connect(self.on_task_selected)
        self.on_lab_selected()
    
    def on_lab_selected(self):
        lab_num = 6
        if self._last_lab_num is not None:
            for view in labs[self._last_lab_num]:
                self.taskView.removeWidget(view)
        for i in range(len(labs[lab_num])):
            if not isinstance(labs[lab_num][i], TaskView):
                labs[lab_num][i] = labs[lab_num][i](self)
            self.taskView.addWidget(labs[lab_num][i])
        self.taskSelect.clear()
        self.taskSelect.addItems(list(map(lambda x: x.task_name(), labs[lab_num])))
        self._last_lab_num = lab_num
    
    def on_task_selected(self, index):
        self.taskView.setCurrentIndex(index)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LabsWindow()
    window.show()
    sys.exit(app.exec_())
