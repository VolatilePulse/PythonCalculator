import wx

from ui import CalcUI

app = wx.App()
frm = CalcUI(None, title='Hello World 2')
frm.Show()
app.MainLoop()