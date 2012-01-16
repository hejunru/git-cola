from cola.widgets import completion
        if event.button() == Qt.LeftButton:
        if (event.button() == Qt.LeftButton and
        painter.drawText(option.rect, Qt.AlignLeft, self.title())
class GitRefDialog(QtGui.QDialog):
    def __init__(self, title, button_text, parent):
        super(GitRefDialog, self).__init__(parent)
        self.setWindowTitle(title)
        self.label = QtGui.QLabel()
        self.label.setText(title)
        self.lineedit = completion.GitRefLineEdit(self)
        self.setFocusProxy(self.lineedit)
        self.ok_button = QtGui.QPushButton()
        self.ok_button.setText(self.tr(button_text))
        self.ok_button.setIcon(qtutils.apply_icon())
        self.close_button = QtGui.QPushButton()
        self.close_button.setText(self.tr('Close'))

        self.button_layout = QtGui.QHBoxLayout()
        self.button_layout.setMargin(0)
        self.button_layout.setSpacing(defs.button_spacing)
        self.button_layout.addStretch()
        self.button_layout.addWidget(self.ok_button)
        self.button_layout.addWidget(self.close_button)

        self.main_layout = QtGui.QVBoxLayout()
        self.main_layout.setMargin(defs.margin)
        self.main_layout.setSpacing(defs.spacing)

        self.main_layout.addWidget(self.label)
        self.main_layout.addWidget(self.lineedit)
        self.main_layout.addLayout(self.button_layout)
        self.setLayout(self.main_layout)

        qtutils.connect_button(self.ok_button, self.accept)
        qtutils.connect_button(self.close_button, self.reject)

        self.connect(self.lineedit, SIGNAL('textChanged(QString)'),
                     self.text_changed)

        self.setWindowModality(Qt.WindowModal)
        self.ok_button.setEnabled(False)

    def text(self):
        return unicode(self.lineedit.text())

    def text_changed(self, txt):
        self.ok_button.setEnabled(bool(self.text()))

    def set_text(self, ref):
        self.lineedit.setText(ref)

    @staticmethod
    def ref(title, button_text, parent, default=None):
        dlg = GitRefDialog(title, button_text, parent)
        if default:
            dlg.set_text(default)
        dlg.show()
        dlg.raise_()
        dlg.setFocus()
        if dlg.exec_() == GitRefDialog.Accepted:
            return dlg.text()
            return None
        diff_old_rgx = TERMINAL(r'^--- ')
        diff_new_rgx = TERMINAL(r'^\+\+\+ ')
        diff_hd4_rgx = TERMINAL(r'^deleted file mode')
                          diff_hd4_rgx,     diff_head,