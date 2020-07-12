#############################################################
# File Name : main.py
#
# KivyMD - NAVIGATION DRAWER
#
# Created :   July 2020 
#############################################################


from kivy.graphics.context_instructions import Color

from kivy.properties  import StringProperty
from kivy.core.window import Window

from kivy.uix.image        import Image
from kivy.uix.widget       import Widget
from kivy.uix.boxlayout    import BoxLayout
from kivy.uix.scrollview   import ScrollView
from kivy.uix.anchorlayout import AnchorLayout

from kivymd.app import MDApp

from kivymd.theming              import ThemableBehavior
from kivymd.uix.list             import MDList
from kivymd.uix.list             import OneLineIconListItem
from kivymd.uix.list             import IconLeftWidget
from kivymd.uix.label            import MDLabel
from kivymd.uix.toolbar          import MDToolbar
from kivymd.uix.floatlayout      import MDFloatLayout
from kivymd.uix.navigationdrawer import NavigationLayout
from kivymd.uix.navigationdrawer import MDNavigationDrawer


##############################################################
##############################################################

class DrawerList(ThemableBehavior, MDList):

    ###################################
    def set_color_item(self, instance_item):
        ################################
        #
        # Called when tap on a menu item
        #
        # Set the color of the icon and text for the menu item.
        #
        for item in self.children:
            if(item.text_color == self.theme_cls.primary_color):
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color
        return

##############################################################
##############################################################

class ItemDrawer(OneLineIconListItem):

    icon = StringProperty()

    ###################################
    def __init__(self, pIcon, pText, **kwargs):
        super(ItemDrawer, self).__init__(**kwargs)
        self.theme_text_color = 'Custom'
        self.text = pText
        self.bind(on_release = self.Press_ItemDrawer)
        ItemDrawer.icon = IconLeftWidget(icon = pIcon, \
                                   theme_text_color = 'Custom', \
                                   text_color = self.text_color)
        if(self.icon.parent == None):
            self.add_widget(self.icon)
        return

    ###################################
    def Press_ItemDrawer(self, instance):
        self.parent.set_color_item(self)
        return

##############################################################
##############################################################

class ContentNavigationDrawer(BoxLayout):

    ###################################
    def __init__(self, **kwargs):
        super(ContentNavigationDrawer, self).__init__(**kwargs)
        ###############################
        self.orientation = 'vertical'
        self.padding     = '8dp'
        self.spacing     = '8dp'
        ###############################
        self.Anchor1 = AnchorLayout()
        self.Label1  = MDLabel()
        self.Label2  = MDLabel()
        self.Scrll   = ScrollView()
        self.DrwList = DrawerList()
        self.Pic1    = Image(source = 'icon.png')
        ###############################
        return

    ###################################
    def Initialize(self):
        LHeight = int(Window.height / 15)
        ###############################
        self.Pic1.size_hint     = (None, None)
        self.Pic1.width         = int(LHeight * 1.5)
        self.Pic1.height        = self.Pic1.width
        self.Pic1.keep_ratio    = True
        self.Pic1.allow_stretch = True
        if(self.Pic1.parent == None):
            self.Anchor1.add_widget(self.Pic1)
        ###############################
        self.Anchor1.anchor_x    = 'left'
        self.Anchor1.size_hint_y = None
        self.Anchor1.height      = int(LHeight * 2)
        if(self.Anchor1.parent == None):
            self.add_widget(self.Anchor1)
        ###
        self.Label1.text        = 'WeightLoss App'
        #self.Label1.custom_color = (1, 0, 0, 1)
        self.Label1.font_style  = 'H5'
        self.Label1.size_hint_y = None
        self.Label1.height      = int(LHeight * 0.9)
        if(self.Label1.parent == None):
            self.add_widget(self.Label1)
        ###
        self.Label2.text        = 'Current User = Monkey'
        self.Label2.font_style  = 'Subtitle2'
        self.Label2.size_hint_y = None
        self.Label2.height      = int(LHeight * 0.4)
        self.Label2.text_color  = (0, 1, 1, 1)
        if(self.Label2.parent == None):
            self.add_widget(self.Label2)
        ###
        icons_item = {'face': 'Users', \
                      'folder': 'DB Import', \
                      'folder-download': 'DB Export', \
                      'information': 'About'}
        ######################################
        #
        # Add on_release to end of ItemDrawer
        # to bind callback function
        #
        for icon_name in icons_item.keys():
            self.DrwList.add_widget(ItemDrawer(pIcon = icon_name, pText = icons_item[icon_name]))
        ###############################
        if(self.DrwList.parent == None):
            self.Scrll.add_widget(self.DrwList)
        if(self.Scrll.parent == None):
            self.add_widget(self.Scrll)
        ###############################
        return

##############################################################
##############################################################


class LayoutsApp(MDApp):
    
    ###################################
    def __init__(self, **kwargs):
        super(LayoutsApp, self).__init__(**kwargs)
        self.NDrawer  = MDNavigationDrawer()
        self.Screen1  = MDFloatLayout()
        self.BLay     = BoxLayout()
        self.MDTool   = MDToolbar()
        self.Widgy    = Widget()
        self.NLayout  = NavigationLayout()
        self.CNDrawer = ContentNavigationDrawer()
        return

    ###################################
    def My_Callback(self, instance):
        self.NDrawer.set_state('toggle')
        return

    ###################################
    def build(self):
        ###############################
        self.Screen1.size = Window.size
        self.NLayout.size = self.Screen1.size
        self.NLayout._scrim_color = Color(rgba=[0, 0, 0, 0]) # Necessary to avoid Exception
        self.BLay.size        = self.Screen1.size
        self.BLay.orientation = 'vertical'
        self.MDTool.title     = 'Navigation Drawer'
        self.MDTool.elevation = 10
        self.MDTool.left_action_items = [['menu', self.My_Callback]]
        ###############################
        if(self.MDTool.parent == None):
            self.BLay.add_widget(self.MDTool)
        if(self.Widgy.parent == None):
            self.BLay.add_widget(self.Widgy)
        if(self.BLay.parent == None):
            self.Screen1.add_widget(self.BLay)
        if(self.CNDrawer.parent == None):
            self.NDrawer.add_widget(self.CNDrawer)
        if(self.NDrawer.parent == None):
            self.NLayout.add_widget(self.NDrawer)
        if(self.NLayout.parent == None):
            self.Screen1.add_widget(self.NLayout)
        ###############################
        LayoutsApp.title = 'Navigation Drawer'
        self.CNDrawer.Initialize()
        return self.Screen1

##############################################################
##############################################################

if __name__ == "__main__":
    LayoutsApp().run()

