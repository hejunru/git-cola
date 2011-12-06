def create_button(text='', layout=None, tooltip=None, icon=None):
    if text:
        button.setText(tr(text))
        self.label = label = QtGui.QLabel()
        self.corner_layout = QtGui.QHBoxLayout()
        self.corner_layout.setMargin(0)
        self.corner_layout.setSpacing(defs.spacing)

        layout.addLayout(self.corner_layout)
    def set_title(self, title):
        self.label.setText(title)

    def add_corner_widget(self, widget):
        self.corner_layout.addWidget(widget)

    'color_text':           rgba(0x00, 0x00, 0x00),
        diff_head = self.mkformat(fg=self.color_header)
        diff_head_bold = self.mkformat(fg=self.color_header, bold=True)
        diff_add = self.mkformat(fg=self.color_text, bg=self.color_add)
        diff_remove = self.mkformat(fg=self.color_text, bg=self.color_remove)
            bad_ws = self.mkformat(fg=Qt.black, bg=Qt.red)