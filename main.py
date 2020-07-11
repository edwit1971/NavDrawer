#############################################################
# File Name : main.py
#
# KivyMD - NAVIGATION DRAWER
#
# Created :   July 2020 
#############################################################


from kivy.graphics.context_instructions import Color

from kivy.core.window import Window
from kivy.properties  import StringProperty

from kivy.uix.widget       import Widget
from kivy.uix.boxlayout    import BoxLayout
from kivy.uix.scrollview   import ScrollView
from kivy.uix.anchorlayout import AnchorLayout

from kivymd.app import MDApp

from kivymd.theming              import ThemableBehavior
from kivymd.theming              import ThemeManager
from kivymd.uix.list             import MDList
from kivymd.uix.list             import OneLineIconListItem
from kivymd.uix.list             import IconLeftWidget
from kivymd.uix.label            import MDLabel
from kivymd.uix.button           import MDFloatingActionButton
from kivymd.uix.toolbar          import MDToolbar
from kivymd.uix.floatlayout      import MDFloatLayout
from kivymd.uix.navigationdrawer import NavigationLayout
from kivymd.uix.navigationdrawer import MDNavigationDrawer


##############################################################
##############################################################

class ItemDrawer(OneLineIconListItem):

    icon = StringProperty()

    ###################################
    def __init__(self, **kwargs):
        super(ItemDrawer, self).__init__(**kwargs)
        self.theme_text_color = 'Custom'
        self.icon = IconLeftWidget(icon='info.png', \
                                   theme_text_color = 'Custom', \
                                   text_color = (1, 0, 0, 1))
        self.bind(on_release = self.Press_ItemDrawer)
        if(self.icon.parent == None):
            self.add_widget(self.icon)
        return

    ###################################
    def Press_ItemDrawer(self, instance):
        self.parent.set_color_item(self)
        return

##############################################################
##############################################################

class DrawerList(ThemableBehavior, MDList):
    
    ###################################
    def __init__(self, **kwargs):
        super(DrawerList, self).__init__(**kwargs)
        return

    ###################################
    def set_color_item(self, pIT):
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
        pIT.text_color = self.theme_cls.primary_color
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
        self.LSpace  = MDLabel()
        self.Label2  = MDLabel()
        self.Label3  = MDLabel()
        self.Label4  = MDLabel()
        self.Label5  = MDLabel()
        self.Label6  = MDLabel()
        self.Scrll   = ScrollView()
        ###############################
        self.List1 = DrawerList()
        self.Pic1  = MDFloatingActionButton(icon = 'info.png')
        ###############################
        return

    ###################################
    def Initialize(self):
        LHeight = int(Window.height / 15)
        ###############################
        self.Anchor1.anchor_x    = 'left'
        self.Anchor1.size_hint_y = None
        self.Anchor1.height      = int(LHeight * 1.25)
        if(self.Anchor1.parent == None):
            self.add_widget(self.Anchor1)
        ###
        self.Label1.text        = 'WeightLoss App'
        self.Label1.font_style  = 'H5'
        self.Label1.size_hint_y = None
        self.Label1.height      = int(LHeight * 0.9)
        if(self.Label1.parent == None):
            self.add_widget(self.Label1)
        ###
        self.Label2.text        = 'Current User = Cheecha'
        self.Label2.font_style  = 'Subtitle2'
        self.Label2.size_hint_y = None
        self.Label2.height      = int(LHeight * 0.5)
        self.Label2.text_color  = (0, 1, 1, 1)
        if(self.Label2.parent == None):
            self.add_widget(self.Label2)
        ###
        self.LSpace.text        = ''
        self.LSpace.font_style  = 'Button'
        self.LSpace.size_hint_y = None
        self.LSpace.height      = int(LHeight * 0.75)
        if(self.LSpace.parent == None):
            self.add_widget(self.LSpace)
        ###
        self.Label3.text        = 'Users'
        self.Label3.font_style  = 'Caption'
        self.Label3.size_hint_y = None
        self.Label3.height      = LHeight
        if(self.Label3.parent == None):
            self.add_widget(self.Label3)
        ###
        self.Label4.text        = 'Database Import'
        self.Label4.font_style  = 'Caption'
        self.Label4.size_hint_y = None
        self.Label4.height      = LHeight
        if(self.Label4.parent == None):
            self.add_widget(self.Label4)
        ###
        self.Label5.text        = 'Database Export'
        self.Label5.font_style  = 'Caption'
        self.Label5.size_hint_y = None
        self.Label5.height      = LHeight
        if(self.Label5.parent == None):
            self.add_widget(self.Label5)
        ###
        self.Label6.text        = 'About'
        self.Label6.font_style  = 'Caption'
        self.Label6.size_hint_y = None
        self.Label6.height      = LHeight
        if(self.Label6.parent == None):
            self.add_widget(self.Label6)
        ###############################
        self.Pic1.size_hint = (None, None)
        self.Pic1.size.x = '56dp'
        self.Pic1.size.y = '56dp'
        if(self.Pic1.parent == None):
            self.Anchor1.add_widget(self.Pic1)
        ###############################
        if(self.List1.parent == None):
            self.Scrll.add_widget(self.List1)
        if(self.Scrll.parent == None):
            self.add_widget(self.Scrll)
        ###############################
        return

##############################################################
##############################################################


class LayoutsApp(MDApp):
    
    ###################################
    def __init__(self, **kwargs):
        LayoutsApp.theme_cls = ThemeManager()
        LayoutsApp.theme_cls.theme_style = 'Light'
        super(LayoutsApp, self).__init__(**kwargs)
        self.nav_drawer = MDNavigationDrawer()
        self.Screen1 = MDFloatLayout()
        self.BLay    = BoxLayout()
        self.MDTool  = MDToolbar()
        self.Widgy   = Widget()
        self.NLayout = NavigationLayout()
        self.content_drawer = ContentNavigationDrawer()
        return

    ###################################
    def My_Callback(self, instance):
        self.nav_drawer.set_state('toggle')
        return

    ###################################
    def build(self):
        ###############################
        self.Screen1.size = Window.size
        self.NLayout.size = self.Screen1.size
        self.NLayout._scrim_color = Color(rgba=[0, 0, 0, 0]) # Necessary to avoid Exception
        self.BLay.size    = self.Screen1.size
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
        if(self.content_drawer.parent == None):
            self.nav_drawer.add_widget(self.content_drawer)
        if(self.nav_drawer.parent == None):
            self.NLayout.add_widget(self.nav_drawer)
        if(self.NLayout.parent == None):
            self.Screen1.add_widget(self.NLayout)
        ###############################
        LayoutsApp.title = 'Navigation Drawer'
        self.content_drawer.Initialize()
        return self.Screen1

##############################################################
##############################################################

if __name__ == "__main__":
    LayoutsApp().run()

