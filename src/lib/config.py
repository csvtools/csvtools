from lib.helpers.iniconfig import IniConfig
from PyQt4.QtGui import *
from PyQt4.QtCore import *


class Config(IniConfig):

    # File section
    file_recent = IniConfig.iniproperty('file', 'recent', [])
    file_session = IniConfig.iniproperty('file', 'session', [])

    # Recent Files section
    recentfiles_check = IniConfig.iniproperty('recentfiles', 'checkRecentFiles', False)
    recentfiles_maxEntries = IniConfig.iniproperty('recentfiles', 'maxEntries', 20)

    # Tab Bar section
    tabbar_showclosebutton = IniConfig.iniproperty('tabbar', 'showCloseButton', True)
    tabbar_doubleclicktoclose  = IniConfig.iniproperty('tabbar', 'doubleClickToClose', False)
    tabbar_lock  = IniConfig.iniproperty('tabbar', 'lock', False)

    # Tools section
    tools_searches = IniConfig.iniproperty('tools', 'searches', [])
    tools_filterFiles = IniConfig.iniproperty('tools', 'filterFiles', [])
    tools_favFolders = IniConfig.iniproperty('tools', 'favFolders', [])
    tools_matchMode = IniConfig.iniproperty('tools', 'matchMode', 0)
    tools_matchCase = IniConfig.iniproperty('tools', 'matchCase', False)
    tools_findAllDocuments = IniConfig.iniproperty('tools', 'findAllDocuments', False)
    tools_showUnmatchedDisabled = IniConfig.iniproperty('tools', 'showUnmatchedDisabled', False)
    tools_showColumnSize = IniConfig.iniproperty('tools', 'showColumnSize', True)
    tools_showColumnDateModified = IniConfig.iniproperty('tools', 'showColumnDateModified', True)

    # Config section
    config_restore = IniConfig.iniproperty('config', 'restore', True)

    # View section
    view_headerrow = IniConfig.iniproperty('view', 'headerRow', True)
    view_showColumnNumberHeaderRow = IniConfig.iniproperty('view', 'showColumnNumberHeaderRow', True)
    view_showtools = IniConfig.iniproperty('view', 'showTools', True)
    view_positiontools = IniConfig.iniproperty('view', 'positionTools', 0)
    view_showTitleTools = IniConfig.iniproperty('view', 'showTitleTools', True)
    view_showborderdata = IniConfig.iniproperty('view', 'showBorderData', True)
    view_colorborderdata = IniConfig.iniproperty('view', 'colorBorderData', QColor(Qt.red).rgb())
    view_widthborderdata = IniConfig.iniproperty('view', 'widthBorderData', 1)
    view_showHighlightSections = IniConfig.iniproperty('view', 'showHighlightSections', True)
    view_colorHighlightSections = IniConfig.iniproperty('view', 'colorHighlightSections', QColor(Qt.white).rgb())
    view_backgroundColorHighlightSections = IniConfig.iniproperty('view', 'backgroundColorHighlightSections', QColor(Qt.black).rgb())

    # Format wizard section
    wizard_showToOpenFile = IniConfig.iniproperty('wizard', 'showToOpenFile', True)
    wizard_showToSaveFile = IniConfig.iniproperty('wizard', 'showToSaveFile', True)
    wizard_showSaveNewFile = IniConfig.iniproperty('wizard', 'showSaveNewFile', True)
    wizard_showToReloadFile = IniConfig.iniproperty('wizard', 'showToReloadFile', True)
    wizard_showToDropFile = IniConfig.iniproperty('wizard', 'showToDropFile', True)
    wizard_loadAllLines = IniConfig.iniproperty('wizard', 'loadAllLines', False)
    wizard_linesToLoad = IniConfig.iniproperty('wizard', 'linesToLoad', 20)

#
# global
#

config = Config('csvtools.cfg')
