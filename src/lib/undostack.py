from PyQt4.QtCore import *
from PyQt4.QtGui import *
import lib.helper as helper


@helper.singleton
class QGlobalUndoStack(QUndoGroup):
  pass


globalUndoStack = QGlobalUndoStack()
