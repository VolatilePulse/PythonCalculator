import wx

class CalcUI(wx.Frame):
    def __init__(self, *args, **kw):
        # Call parent constructor first
        super().__init__(*args, **kw)

        # Prevent controls from getting too small
        self.SetMinSize((300, 400))

        # Generate buttons and layout
        self.CreateLayout()

        # create a menu bar
        self.makeMenuBar()

        # and a status bar
        self.CreateStatusBar()
        self.SetStatusText("Welcome to wxPython!")


    def makeMenuBar(self):
        """
        A menu bar is composed of menus, which are composed of menu items.
        This method builds a set of menus and binds handlers to be called
        when the menu item is selected.
        """

        # Make a file menu with Hello and Exit items
        fileMenu = wx.Menu()
        # The "\t..." syntax defines an accelerator key that also triggers
        # the same event
        helloItem = fileMenu.Append(-1, "&Hello...\tCtrl-H",
                "Help string shown in status bar for this menu item")
        fileMenu.AppendSeparator()
        # When using a stock ID we don't need to specify the menu item's
        # label
        exitItem = fileMenu.Append(wx.ID_EXIT)

        # Now a help menu for the about item
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        # Make the menu bar and add the two menus to it. The '&' defines
        # that the next letter is the "mnemonic" for the menu item. On the
        # platforms that support it those letters are underlined and can be
        # triggered from the keyboard.
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")

        # Give the menu bar to the frame
        self.SetMenuBar(menuBar)

        # Finally, associate a handler function with the EVT_MENU event for
        # each of the menu items. That means that when that menu item is
        # activated then the associated handler function will be called.
        self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
        self.Bind(wx.EVT_MENU, self.OnExit,  exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)


    def OnExit(self, event):
        """Close the frame, terminating the application."""
        self.Close(True)


    def OnHello(self, event):
        """Say hello to the user."""
        wx.MessageBox("Hello again from wxPython")


    def OnAbout(self, event):
        """Display an About Dialog"""
        wx.MessageBox("This is a wxPython Hello World sample",
                      "About Hello World 2",
                      wx.OK|wx.ICON_INFORMATION)

    def CreateLayout(self):
        # Define "screen"
        display = wx.TextCtrl(self, value="50", style=wx.TE_READONLY|wx.TE_RIGHT, name="display")

        # Define calculator buttons
        calc_7 = wx.Button(self, label="7", size=(60, 40), name="calc_7")
        calc_8 = wx.Button(self, label="8", size=(60, 40), name="calc_8")
        calc_9 = wx.Button(self, label="9", size=(60, 40), name="calc_9")

        calc_4 = wx.Button(self, label="4", size=(60, 40), name="calc_4")
        calc_5 = wx.Button(self, label="5", size=(60, 40), name="calc_5")
        calc_6 = wx.Button(self, label="6", size=(60, 40), name="calc_6")

        calc_1 = wx.Button(self, label="1", size=(60, 40), name="calc_1")
        calc_2 = wx.Button(self, label="2", size=(60, 40), name="calc_2")
        calc_3 = wx.Button(self, label="3", size=(60, 40), name="calc_3")

        calc_sign = wx.Button(self, label="+/-", size=(60, 40), name="calc_sign")
        calc_0 = wx.Button(self, label="0", size=(60, 40), name="calc_0")
        calc_decimal = wx.Button(self, label=".", size=(60, 40), name="calc_decimal")

        calc_div = wx.Button(self, label="/", size=(60, 40), name="calc_div")
        calc_mul = wx.Button(self, label="x", size=(60, 40), name="calc_mul")
        calc_add = wx.Button(self, label="+", size=(60, 40), name="calc_add")
        calc_sub = wx.Button(self, label="-", size=(60, 40), name="calc_sub")
        calc_eq = wx.Button(self, label="=", size=(60, 40), name="calc_eq")

        # and create a sizer to manage the layout of child widgets
        sizer_col_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_col_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_col_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_col_4 = wx.BoxSizer(wx.VERTICAL)

        sizer_col_1.Add(calc_7, 1, wx.EXPAND)
        sizer_col_1.Add(calc_4, 1, wx.EXPAND)
        sizer_col_1.Add(calc_1, 1, wx.EXPAND)
        sizer_col_1.Add(calc_sign, 1, wx.EXPAND)

        sizer_col_2.Add(calc_8, 1, wx.EXPAND)
        sizer_col_2.Add(calc_5, 1, wx.EXPAND)
        sizer_col_2.Add(calc_2, 1, wx.EXPAND)
        sizer_col_2.Add(calc_0, 1, wx.EXPAND)

        sizer_col_3.Add(calc_9, 1, wx.EXPAND)
        sizer_col_3.Add(calc_6, 1, wx.EXPAND)
        sizer_col_3.Add(calc_3, 1, wx.EXPAND)
        sizer_col_3.Add(calc_decimal, 1, wx.EXPAND)

        sizer_col_4.Add(calc_div, 1, wx.EXPAND)
        sizer_col_4.Add(calc_mul, 1, wx.EXPAND)
        sizer_col_4.Add(calc_add, 1, wx.EXPAND)
        sizer_col_4.Add(calc_sub, 1, wx.EXPAND)
        sizer_col_4.Add(calc_eq, 1, wx.EXPAND)

        # Number sizer
        sizer_numbers = wx.BoxSizer(wx.HORIZONTAL)

        sizer_numbers.Add(sizer_col_1, 1, wx.EXPAND)
        sizer_numbers.Add(sizer_col_2, 1, wx.EXPAND)
        sizer_numbers.Add(sizer_col_3, 1, wx.EXPAND)
        sizer_numbers.Add(sizer_col_4, 1, wx.EXPAND)

        calc_sizer = wx.BoxSizer(wx.VERTICAL)
        calc_sizer.Add(display, 1, wx.EXPAND)
        calc_sizer.Add(sizer_numbers, 6, wx.EXPAND)

        self.SetSizer(calc_sizer)