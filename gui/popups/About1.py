
import wx
from wx.lib.wordwrap import wordwrap

#----------------------------------------------------------------------

licenseText = "Put license info here"

#----------------------------------------------------------------------

class AboutPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1)

        button1 = wx.Button(self, -1, "Show a wx.AboutBox", (50,50))
        self.Bind(wx.EVT_BUTTON, self.OnButton, button1)


    def OnButton(self, evt):
        # First we create and fill the info object
        info = wx.AboutDialogInfo()
        info.Name = "PypeLine"
        info.Version = "1.0"
        info.Copyright = "(C) 2015 ASRAD"
        info.Description = wordwrap(
            "Description of ASRAD goes here",
            350, wx.ClientDC(self))
        info.WebSite = ("http://www.asrad.com.tr/")
        info.Developers = ["Oguz Yilmaz and Friends"]

        info.License = wordwrap(licenseText, 500, wx.ClientDC(self))

        # Then we call wx.AboutBox giving it that info object
        wx.AboutBox(info)

#----------------------------------------------------------------------


class Frame(wx.Frame):
    def __init__(self):
        super(Frame, self).__init__(None)
        self.SetTitle('About ASRAD')
        self.SetClientSize((500, 500))
        self.Center()
        self.view = AboutPanel(self)

def main():
    app = wx.App(False)
    frame = Frame()
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
