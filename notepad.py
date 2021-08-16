from pywinauto.application import Application
import time
from pywinauto import mouse

app = Application(backend='win32').start('notepad.exe')
mainwin = app['无标题 - 记事本']
time.sleep(1)
mainwin.Edit.type_keys("自动化输入第一行", with_spaces = True)
time.sleep(1)
mainwin.child_window(class_name="Edit").type_keys("{ENTER}自动化输入第二行", with_spaces = True)
time.sleep(1)
mainwin.menu_select('文件 -> 保存')
app['另存为']['文件名 Edit'].set_text(r'11.txt')
time.sleep(1)
mouse.click(coords=(1690,860))
