# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled2.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_help_window(object):
    def setupUi(self, help_window):
        if not help_window.objectName():
            help_window.setObjectName(u"help_window")
        help_window.setWindowModality(Qt.ApplicationModal)
        help_window.resize(758, 610)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(help_window.sizePolicy().hasHeightForWidth())
        help_window.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"img/help.png", QSize(), QIcon.Normal, QIcon.Off)
        help_window.setWindowIcon(icon)
        self.text2 = QTextBrowser(help_window)
        self.text2.setObjectName(u"text2")
        self.text2.setGeometry(QRect(30, 130, 680, 440))
        self.label1 = QLabel(help_window)
        self.label1.setObjectName(u"label1")
        self.label1.setGeometry(QRect(30, 20, 55, 16))
        self.label2 = QLabel(help_window)
        self.label2.setObjectName(u"label2")
        self.label2.setGeometry(QRect(30, 110, 81, 16))
        self.text1 = QTextBrowser(help_window)
        self.text1.setObjectName(u"text1")
        self.text1.setGeometry(QRect(30, 40, 680, 61))

        self.retranslateUi(help_window)

        QMetaObject.connectSlotsByName(help_window)
    # setupUi

    def retranslateUi(self, help_window):
        help_window.setWindowTitle(QCoreApplication.translate("help_window", u"Help", None))
        self.text2.setHtml(QCoreApplication.translate("help_window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Hra se ovl\u00e1d\u00e1 jednodu\u0161e p\u0159es jednotliv\u00e9 ovl\u00e1dac\u00ed prvky viditeln\u00e9 v otev\u0159en\u00e9m okn\u011b.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">V\u00fdb\u011br hr\u00e1\u010d\u016f</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; "
                        "margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Seznam hr\u00e1\u010d\u016f se nach\u00e1z\u00ed v lev\u00e9 \u010d\u00e1sti obrazovky. Pokud chcete n\u011bjak\u00e9ho hr\u00e1\u010de p\u0159idat do sv\u00e9ho t\u00fdmu, je pot\u0159eba ho v seznamu vybrat, pot\u00e9 vybrat pozici ve va\u0161em t\u00fdmu, na kterou ho chcete um\u00edstit a pot\u00e9 kliknout na tla\u010d\u00edtko &quot;P\u0159idat do t\u00fdmu&quot; nach\u00e1zej\u00edc\u00ed se pod seznamem hr\u00e1\u010d\u016f.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Atributy hr\u00e1\u010d\u016f</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">P\u0159i podr\u017een\u00ed"
                        " kurzoru my\u0161i nad jednotliv\u00fdmi hr\u00e1\u010di v seznamu se zobraz\u00ed hodnoty jejich atribut\u016f. Podle t\u011bchto hodnot se lze \u0159\u00eddit p\u0159i umis\u0165ov\u00e1n\u00ed hr\u00e1\u010d\u016f do sv\u00e9ho t\u00fdmu. Atributy ovliv\u0148uj\u00ed v\u00fdkon hr\u00e1\u010d\u016f v n\u00e1sleduj\u00edcm z\u00e1pasu.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Odstran\u011bn\u00ed hr\u00e1\u010de</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Hr\u00e1\u010de z t\u00fdmu lze odstranit snadno t\u00edm, \u017ee je vybr\u00e1na pozice, na kter\u00e9 je doty\u010dn\u00fd hr\u00e1\u010d um\u00edst\u011bn a p\u0159es seznam a tla\u010d"
                        "\u00edtko &quot;P\u0159idat do t\u00fdmu&quot; je na tuto pozici vybr\u00e1n jin\u00fd hr\u00e1\u010d.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Zm\u011bna jm\u00e9na vlastn\u00edho t\u00fdmu</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Lze prov\u00e9st p\u0159es textov\u00e9 pole nad soupiskou vlastn\u00edho t\u00fdmu. Po vlo\u017een\u00ed nov\u00e9ho n\u00e1zvu je pot\u0159eba kliknout na tla\u010d\u00edtko &quot;Zm\u011bnit&quot;.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p style=\""
                        " margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Vytvo\u0159en\u00ed soupe\u0159e</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Jakmile m\u00e1te vytvo\u0159en\u00fd vlastn\u00ed t\u00fdm, m\u016f\u017eete vygenrovat soupe\u0159\u016fv t\u00fdm. Ten se vytvo\u0159\u00ed ze zb\u00fdvaj\u00edc\u00edch voln\u00fdch hr\u00e1\u010d\u016f seznamu. Pro vygenerov\u00e1n\u00ed je pot\u0159eba kliknout na tla\u010d\u00edtko &quot;Vytvo\u0159it soupe\u0159e&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Uskute\u010dn\u011bn\u00ed z\u00e1pasu</sp"
                        "an></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Pokud m\u00e1te vy i soupe\u0159 vytvo\u0159en\u00fd t\u00fdm, je mo\u017en\u00e9 uskute\u010dnit z\u00e1pas. Toto lze prov\u00e9st p\u0159es tla\u010d\u00edtko &quot;Hr\u00e1t&quot;. Po dokon\u010den\u00ed simulace z\u00e1pasu je zobrazen v\u00fdsledek.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Restart hry</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Pokud chcete zvolit nov\u00fd t\u00fdm a opakovat z\u00e1pas s po\u010d\u00edta\u010dem, zvolte v horn\u00ed li\u0161t\u011b jedinou mo\u017enost &quot;Menu&quot; a "
                        "ve vyb\u00edrac\u00ed nab\u00eddce pot\u00e9 mo\u017enost &quot;Restart&quot;. Tuto volbu je pot\u00e9 je\u0161t\u011b nutn\u00e9 potvrdit.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p></body></html>", None))
        self.label1.setText(QCoreApplication.translate("help_window", u"C\u00edl hry", None))
        self.label2.setText(QCoreApplication.translate("help_window", u"Ovl\u00e1d\u00e1n\u00ed hry", None))
        self.text1.setHtml(QCoreApplication.translate("help_window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">C\u00edlem hry je sestavit co nejlep\u0161\u00ed fotbalov\u00e9 mu\u017estvo a v n\u00e1sleduj\u00edc\u00edm z\u00e1pase porazit po\u010d\u00edta\u010d. O v\u00edt\u011bzi rozhoduj\u00ed zejm\u00e9na st\u0159eleck\u00e9 schopnosti \u00fato\u010dn\u00edk\u016f, obrann\u00e9 schopnosti obr\u00e1nc\u016f, golmanova \u00farove\u0148 chyt\u00e1n\u00ed, ale svou roli hraje i n\u00e1hoda.</p></body></html>", None))
    # retranslateUi

