# Form implementation generated from reading ui file 'c:\Users\lenovo\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\Plugin-upload-Palapa\ui\UploadPalapa_main.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_StylePalapaDialogBase(object):
    def setupUi(self, StylePalapaDialogBase):
        StylePalapaDialogBase.setObjectName("StylePalapaDialogBase")
        StylePalapaDialogBase.setEnabled(True)
        StylePalapaDialogBase.resize(700, 761)
        StylePalapaDialogBase.setMinimumSize(QtCore.QSize(700, 660))
        StylePalapaDialogBase.setStyleSheet("#StylePalapaDialogBase {\n"
" background: rgb(244, 244, 244);\n"
"}")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(StylePalapaDialogBase)
        self.verticalLayout_3.setContentsMargins(20, 10, 20, 20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(StylePalapaDialogBase)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setMinimumSize(QtCore.QSize(42, 48))
        self.label_2.setMaximumSize(QtCore.QSize(42, 48))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("c:\\Users\\lenovo\\AppData\\Roaming\\QGIS\\QGIS3\\profiles\\default\\python\\plugins\\Plugin-upload-Palapa\\ui\\../img/420px-Badan_Informasi_Geospasial_logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_userdesc = QtWidgets.QLabel(self.frame)
        self.label_userdesc.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_userdesc.setObjectName("label_userdesc")
        self.verticalLayout.addWidget(self.label_userdesc)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButton_logout = QtWidgets.QPushButton(self.frame)
        self.pushButton_logout.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_logout.setStyleSheet("QPushButton{\n"
"text-align:right;\n"
"width:50px;\n"
"background:transparent;\n"
"border:0px;\n"
"}\n"
"QPushButton:disabled {\n"
"color:#cccccc;\n"
"\n"
"}\n"
"QPushButton:enabled {\n"
"color:rgb(1, 125, 197);\n"
"}\n"
"\n"
"")
        self.pushButton_logout.setObjectName("pushButton_logout")
        self.horizontalLayout_2.addWidget(self.pushButton_logout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addWidget(self.frame)
        self._main_tab = QtWidgets.QTabWidget(StylePalapaDialogBase)
        self._main_tab.setEnabled(True)
        self._main_tab.setObjectName("_main_tab")
        self.upload_tab = QtWidgets.QWidget()
        self.upload_tab.setObjectName("upload_tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.upload_tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.upload_tab)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 320))
        self.frame_4.setStyleSheet("margin:0px")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_layer = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_layer.setFont(font)
        self.label_layer.setObjectName("label_layer")
        self.verticalLayout_4.addWidget(self.label_layer)
        self.select_layer = QgsMapLayerComboBox(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_layer.sizePolicy().hasHeightForWidth())
        self.select_layer.setSizePolicy(sizePolicy)
        self.select_layer.setMinimumSize(QtCore.QSize(0, 24))
        self.select_layer.setStyleSheet("padding:5px")
        self.select_layer.setObjectName("select_layer")
        self.verticalLayout_4.addWidget(self.select_layer)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setContentsMargins(-1, -1, -1, 15)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_layertitle = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_layertitle.setFont(font)
        self.label_layertitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_layertitle.setObjectName("label_layertitle")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_layertitle)
        self.lineEdit_layertitle = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_layertitle.setEnabled(True)
        self.lineEdit_layertitle.setMinimumSize(QtCore.QSize(0, 24))
        self.lineEdit_layertitle.setStyleSheet("padding-left:\"5px\"")
        self.lineEdit_layertitle.setPlaceholderText("")
        self.lineEdit_layertitle.setObjectName("lineEdit_layertitle")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_layertitle)
        self.label_layerabstract = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_layerabstract.setFont(font)
        self.label_layerabstract.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_layerabstract.setObjectName("label_layerabstract")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_layerabstract)
        self.textEdit_layerabstract = QtWidgets.QTextEdit(self.frame_4)
        self.textEdit_layerabstract.setStyleSheet("padding-left:\"5px\"")
        self.textEdit_layerabstract.setObjectName("textEdit_layerabstract")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textEdit_layerabstract)
        self.verticalLayout_4.addLayout(self.formLayout_2)
        self.line = QtWidgets.QFrame(self.frame_4)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.label_style = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_style.setFont(font)
        self.label_style.setObjectName("label_style")
        self.verticalLayout_4.addWidget(self.label_style)
        self.groupBox_style = QtWidgets.QGroupBox(self.frame_4)
        self.groupBox_style.setStyleSheet("groupBox_style{\n"
"margin:0px}")
        self.groupBox_style.setTitle("")
        self.groupBox_style.setObjectName("groupBox_style")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_style)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.radioButton_StyleQgis = QtWidgets.QRadioButton(self.groupBox_style)
        self.radioButton_StyleQgis.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.radioButton_StyleQgis.setChecked(True)
        self.radioButton_StyleQgis.setObjectName("radioButton_StyleQgis")
        self.verticalLayout_7.addWidget(self.radioButton_StyleQgis)
        self.radioButton_StyleBrowse = QtWidgets.QRadioButton(self.groupBox_style)
        self.radioButton_StyleBrowse.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.radioButton_StyleBrowse.setStyleSheet("padding:0px")
        self.radioButton_StyleBrowse.setObjectName("radioButton_StyleBrowse")
        self.verticalLayout_7.addWidget(self.radioButton_StyleBrowse)
        self.verticalLayout_4.addWidget(self.groupBox_style)
        self.layout_browseSLD = QtWidgets.QHBoxLayout()
        self.layout_browseSLD.setContentsMargins(-1, -1, -1, 15)
        self.layout_browseSLD.setSpacing(5)
        self.layout_browseSLD.setObjectName("layout_browseSLD")
        self.lineEdit_style = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_style.setEnabled(False)
        self.lineEdit_style.setMinimumSize(QtCore.QSize(0, 24))
        self.lineEdit_style.setPlaceholderText("")
        self.lineEdit_style.setObjectName("lineEdit_style")
        self.layout_browseSLD.addWidget(self.lineEdit_style)
        self.pushButton_clearStyle = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_clearStyle.setMaximumSize(QtCore.QSize(26, 16777215))
        self.pushButton_clearStyle.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\lenovo\\AppData\\Roaming\\QGIS\\QGIS3\\profiles\\default\\python\\plugins\\Plugin-upload-Palapa\\ui\\../img/cancel.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_clearStyle.setIcon(icon)
        self.pushButton_clearStyle.setObjectName("pushButton_clearStyle")
        self.layout_browseSLD.addWidget(self.pushButton_clearStyle)
        self.browse_style = QtWidgets.QPushButton(self.frame_4)
        self.browse_style.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browse_style.sizePolicy().hasHeightForWidth())
        self.browse_style.setSizePolicy(sizePolicy)
        self.browse_style.setMaximumSize(QtCore.QSize(80, 16777215))
        self.browse_style.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.browse_style.setStyleSheet("padding:5px 20px")
        self.browse_style.setObjectName("browse_style")
        self.layout_browseSLD.addWidget(self.browse_style)
        self.verticalLayout_4.addLayout(self.layout_browseSLD)
        self.line_3 = QtWidgets.QFrame(self.frame_4)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_4.addWidget(self.line_3)
        self.label_metadata = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_metadata.setFont(font)
        self.label_metadata.setObjectName("label_metadata")
        self.verticalLayout_4.addWidget(self.label_metadata)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame_4)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.radioButton_meta_min = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_meta_min.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.radioButton_meta_min.setChecked(True)
        self.radioButton_meta_min.setObjectName("radioButton_meta_min")
        self.horizontalLayout_7.addWidget(self.radioButton_meta_min)
        self.radioButton_meta_xml = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_meta_xml.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.radioButton_meta_xml.setObjectName("radioButton_meta_xml")
        self.horizontalLayout_7.addWidget(self.radioButton_meta_xml)
        self.radioButton_meta_lengkap = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_meta_lengkap.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.radioButton_meta_lengkap.setChecked(False)
        self.radioButton_meta_lengkap.setObjectName("radioButton_meta_lengkap")
        self.horizontalLayout_7.addWidget(self.radioButton_meta_lengkap)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.mDateTimeEdit = QgsDateTimeEdit(self.frame_4)
        self.mDateTimeEdit.setMinimumSize(QtCore.QSize(0, 22))
        self.mDateTimeEdit.setCalendarPopup(True)
        self.mDateTimeEdit.setObjectName("mDateTimeEdit")
        self.verticalLayout_4.addWidget(self.mDateTimeEdit)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setContentsMargins(-1, -1, -1, 15)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_layertitle_2 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_layertitle_2.setFont(font)
        self.label_layertitle_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_layertitle_2.setObjectName("label_layertitle_2")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_layertitle_2)
        self.comboBox_keyword = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_keyword.setMinimumSize(QtCore.QSize(0, 22))
        self.comboBox_keyword.setStyleSheet("padding:5px")
        self.comboBox_keyword.setEditable(False)
        self.comboBox_keyword.setObjectName("comboBox_keyword")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.comboBox_keyword)
        self.label_layerabstract_2 = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_layerabstract_2.sizePolicy().hasHeightForWidth())
        self.label_layerabstract_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_layerabstract_2.setFont(font)
        self.label_layerabstract_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_layerabstract_2.setObjectName("label_layerabstract_2")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_layerabstract_2)
        self.comboBox_constraint = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_constraint.setMinimumSize(QtCore.QSize(0, 22))
        self.comboBox_constraint.setStyleSheet("padding:5px")
        self.comboBox_constraint.setObjectName("comboBox_constraint")
        self.comboBox_constraint.addItem("")
        self.comboBox_constraint.addItem("")
        self.comboBox_constraint.addItem("")
        self.comboBox_constraint.addItem("")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.comboBox_constraint)
        self.verticalLayout_4.addLayout(self.formLayout_3)
        self.meta_lengkap = QtWidgets.QPushButton(self.frame_4)
        self.meta_lengkap.setEnabled(True)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.meta_lengkap.setFont(font)
        self.meta_lengkap.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.meta_lengkap.setStyleSheet("padding:5px")
        self.meta_lengkap.setCheckable(False)
        self.meta_lengkap.setAutoDefault(True)
        self.meta_lengkap.setObjectName("meta_lengkap")
        self.verticalLayout_4.addWidget(self.meta_lengkap)
        self.meta_browser = QtWidgets.QHBoxLayout()
        self.meta_browser.setSpacing(6)
        self.meta_browser.setObjectName("meta_browser")
        self.lineEdit_metadata = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_metadata.setEnabled(True)
        self.lineEdit_metadata.setMinimumSize(QtCore.QSize(0, 24))
        self.lineEdit_metadata.setObjectName("lineEdit_metadata")
        self.meta_browser.addWidget(self.lineEdit_metadata)
        self.pushButton_clearMetadata = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_clearMetadata.setMaximumSize(QtCore.QSize(26, 16777215))
        self.pushButton_clearMetadata.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_clearMetadata.setText("")
        self.pushButton_clearMetadata.setIcon(icon)
        self.pushButton_clearMetadata.setObjectName("pushButton_clearMetadata")
        self.meta_browser.addWidget(self.pushButton_clearMetadata)
        self.browse_metadata = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browse_metadata.sizePolicy().hasHeightForWidth())
        self.browse_metadata.setSizePolicy(sizePolicy)
        self.browse_metadata.setMaximumSize(QtCore.QSize(80, 16777215))
        self.browse_metadata.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.browse_metadata.setStyleSheet("padding:5px 20px")
        self.browse_metadata.setObjectName("browse_metadata")
        self.meta_browser.addWidget(self.browse_metadata)
        self.verticalLayout_4.addLayout(self.meta_browser)
        self.line_2 = QtWidgets.QFrame(self.frame_4)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_4.addWidget(self.line_2)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setContentsMargins(-1, 10, -1, 0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.upload = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upload.sizePolicy().hasHeightForWidth())
        self.upload.setSizePolicy(sizePolicy)
        self.upload.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.upload.setFont(font)
        self.upload.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.upload.setStyleSheet("QPushButton {\n"
"border:0px;\n"
"border-radius: 4px;\n"
"padding: 4px;\n"
"font-size: 14px;\n"
"height:25px;\n"
"width:140px;\n"
"}\n"
"QPushButton:disabled {\n"
"background-color:#cccccc;\n"
"color:#969696;\n"
"}\n"
"QPushButton:enabled {\n"
"color:white;\n"
"background-color:rgb(1, 125, 197);\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(21, 50, 92);\n"
"color:white;\n"
"}")
        self.upload.setObjectName("upload")
        self.horizontalLayout_16.addWidget(self.upload)
        self.verticalLayout_4.addLayout(self.horizontalLayout_16)
        self.label_statusbase = QtWidgets.QLabel(self.frame_4)
        self.label_statusbase.setMinimumSize(QtCore.QSize(0, 25))
        self.label_statusbase.setStyleSheet("border-radius: 4px;")
        self.label_statusbase.setText("")
        self.label_statusbase.setWordWrap(True)
        self.label_statusbase.setIndent(5)
        self.label_statusbase.setObjectName("label_statusbase")
        self.verticalLayout_4.addWidget(self.label_statusbase)
        self.verticalLayout_2.addWidget(self.frame_4)
        self._main_tab.addTab(self.upload_tab, "")
        self.verticalLayout_3.addWidget(self._main_tab)

        self.retranslateUi(StylePalapaDialogBase)
        self._main_tab.setCurrentIndex(0)
        self.comboBox_keyword.setCurrentIndex(-1)
        self.comboBox_constraint.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(StylePalapaDialogBase)

    def retranslateUi(self, StylePalapaDialogBase):
        _translate = QtCore.QCoreApplication.translate
        StylePalapaDialogBase.setWindowTitle(_translate("StylePalapaDialogBase", "UploadToPalapa"))
        self.label.setText(_translate("StylePalapaDialogBase", "Upload to Palapa"))
        self.label_userdesc.setText(_translate("StylePalapaDialogBase", "Anda masuk sebagai \'\' pada \'\'"))
        self.pushButton_logout.setText(_translate("StylePalapaDialogBase", "Log out"))
        self.label_layer.setText(_translate("StylePalapaDialogBase", "Pilih Layer :"))
        self.label_layertitle.setText(_translate("StylePalapaDialogBase", "Layer Title"))
        self.label_layerabstract.setText(_translate("StylePalapaDialogBase", "Layer Abstract"))
        self.label_style.setText(_translate("StylePalapaDialogBase", "Pilih Style :"))
        self.radioButton_StyleQgis.setText(_translate("StylePalapaDialogBase", "Gunakan Style dari Layer di QGIS"))
        self.radioButton_StyleBrowse.setText(_translate("StylePalapaDialogBase", "Unggah Style Kustom (SLD)"))
        self.browse_style.setText(_translate("StylePalapaDialogBase", "Browse"))
        self.label_metadata.setText(_translate("StylePalapaDialogBase", "Informasi Metadata :"))
        self.radioButton_meta_min.setText(_translate("StylePalapaDialogBase", "Metadata Minimal"))
        self.radioButton_meta_xml.setText(_translate("StylePalapaDialogBase", "Upload Metadata (XML)"))
        self.radioButton_meta_lengkap.setText(_translate("StylePalapaDialogBase", "Metadata Lengkap"))
        self.mDateTimeEdit.setDisplayFormat(_translate("StylePalapaDialogBase", "M/d/yyyy h:mm AP"))
        self.label_layertitle_2.setText(_translate("StylePalapaDialogBase", "Keyword"))
        self.label_layerabstract_2.setText(_translate("StylePalapaDialogBase", "Informasi Data Constraints"))
        self.comboBox_constraint.setItemText(0, _translate("StylePalapaDialogBase", "PUBLIC"))
        self.comboBox_constraint.setItemText(1, _translate("StylePalapaDialogBase", "GOVERNMENT"))
        self.comboBox_constraint.setItemText(2, _translate("StylePalapaDialogBase", "PRIVATE"))
        self.comboBox_constraint.setItemText(3, _translate("StylePalapaDialogBase", "IG STRATEGIS"))
        self.meta_lengkap.setText(_translate("StylePalapaDialogBase", "Isi Metadata"))
        self.lineEdit_metadata.setPlaceholderText(_translate("StylePalapaDialogBase", "[optional]"))
        self.browse_metadata.setText(_translate("StylePalapaDialogBase", "Browse"))
        self.upload.setText(_translate("StylePalapaDialogBase", "Unggah"))
        self._main_tab.setTabText(self._main_tab.indexOf(self.upload_tab), _translate("StylePalapaDialogBase", "Upload"))
from qgsdatetimeedit import QgsDateTimeEdit
from qgsmaplayercombobox import QgsMapLayerComboBox
