#############################################################
# File Name : main.py
#
# KivyMD - NAVIGATION DRAWER
#
# Created :   July 2020 
#############################################################


from kivy.core.window import Window
from kivy.properties  import StringProperty

from kivy.uix.boxlayout    import BoxLayout
from kivy.uix.scrollview   import ScrollView
from kivy.uix.anchorlayout import AnchorLayout

from kivymd.app import MDApp

from kivymd.theming              import ThemableBehavior
from kivymd.uix.list             import MDList
from kivymd.uix.list             import OneLineListItem
from kivymd.uix.list             import OneLineIconListItem
from kivymd.uix.list             import IconLeftWidget
from kivymd.uix.label            import MDLabel
from kivymd.uix.button           import MDFloatingActionButton
from kivymd.uix.floatlayout      import MDFloatLayout
from kivymd.uix.navigationdrawer import NavigationLayout
from kivymd.uix.navigationdrawer import MDNavigationDrawer


##############################################################
##############################################################

class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()

##############################################################
##############################################################

class DrawerList(ThemableBehavior, MDList):

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

    ###################################
    def on_start(self):
        icons_item = {"folder": "My files", \
                      "account-multiple": "Shared with me", \
                      "star": "Starred", \
                      "history": "Recent", \
                      "checkbox-marked": "Shared with me", \
                      "upload": "Upload",}
        for icon_name in icons_item.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(ItemDrawer(icon=icon_name, text=icons_item[icon_name]))
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
        self.Anchor1   = AnchorLayout()
        self.Label1    = MDLabel()
        self.Label2    = MDLabel()
        self.Scr1      = ScrollView()
        ###############################
        self.Pic1   = MDFloatingActionButton(icon = 'kivymd_logo.png')
        self.List1  = DrawerList()
        self.LItem1 = OneLineListItem()
        self.LItem2 = OneLineListItem()
        self.ItemDr = ItemDrawer()
        self.ico1   = IconLeftWidget()
        ###############################
        self.NavDrawer = None
        return

    ###################################
    def Initialize(self):
        ###############################
        self.Anchor1.anchor_x    = 'left'
        self.Anchor1.size_hint_y = None
        self.Anchor1.height      = '56dp'
        if(self.Anchor1.parent == None):
            self.add_widget(self.Anchor1)
        ###
        self.Label1.text        = 'KivyMD library'
        self.Label1.font_style  = 'Button'
        self.Label1.size_hint_y = None
        self.Label1.height      = self.Label1.texture_size[1]
        if(self.Label1.parent == None):
            self.add_widget(self.Label1)
        ###
        self.Label2.text        = 'kivydevelopment@gmail.com'
        self.Label2.font_style  = 'Caption'
        self.Label2.size_hint_y = None
        self.Label2.height      = self.Label2.texture_size[1]
        if(self.Label2.parent == None):
            self.add_widget(self.Label2)
        ###
        if(self.Scr1.parent == None):
            self.add_widget(self.Scr1)
        ###############################
        self.Pic1.size_hint = (None, None)
        self.Pic1.size.x = '56dp'
        self.Pic1.size.y = '56dp'
        ###############################
        self.ItemDr.theme_text_color = 'Custom'
        if(self.ItemDr.parent == None):
            self.add_widget(self.ItemDr)
        ###
        self.ico1.icon = ''
        self.ico1.theme_text_color = 'Custom'
        self.ico1.text_color = (1, 0, 0, 1)
        if(self.ico1.parent == None):
            self.ItemDr.add_widget(self.ico1)
        ###############################
        if(self.List1.parent == None):
            self.Scr1.add_widget(self.List1)
        ###############################
        self.LItem1.text = 'Screen 1'
        if(self.LItem1.parent == None):
            self.List1.add_widget(self.LItem1)
        ###
        self.LItem2.text = 'Screen 2'
        if(self.LItem2.parent == None):
            self.List1.add_widget(self.LItem2)
        ###############################
        self.ItemDr.bind(on_release = self.Press_ItemDr)
        self.LItem1.bind(on_press   = self.Press_Item1)
        self.LItem2.bind(on_press   = self.Press_Item2)
        return
    
    ###################################
    def Press_Item1(self, instance):
        self.NavDrawer.set_state("close")
        return
    
    ###################################
    def Press_Item2(self, instance):
        self.NavDrawer.set_state("close")
        return
    
    ###################################
    def Press_ItemDr(self, instance):
        self.parent.set_color_item(self)
        return

##############################################################
##############################################################
class LayoutsApp(MDApp):

    ###################################
    def __init__(self, **kwargs):
        super(LayoutsApp, self).__init__(**kwargs)
        self.Screen1   = MDFloatLayout()
        self.iMenu     = MDFloatingActionButton(icon = './iMenu.png')
        self.CND       = ContentNavigationDrawer()
        self.NLayout   = NavigationLayout()
        self.NavDrawer = MDNavigationDrawer()
        return

    ###################################
    def Press_Menu(self, instance):
        self.NavDrawer.set_state("toggle")
        self.NavDrawer.set_state("open")
        return

    ###################################
    def build(self):
        ###############################
        self.Screen1.size = Window.size
        self.NLayout.size = self.Screen1.size
        Xc = int(self.Screen1.width  * 0.5)
        Yc = int(self.Screen1.height * 0.5)
        ###
        self.iMenu.elevation_normal = 10
        self.iMenu.size_hint = (None, None)
        self.iMenu.height    = 50
        self.iMenu.width     = 50
        self.iMenu.x         = Xc - int(self.iMenu.width * 0.5)
        self.iMenu.y         = Yc - int(self.iMenu.height * 0.5)
        self.iMenu.bind(on_press = self.Press_Menu)
        ###
        if(self.iMenu.parent == None):
            self.Screen1.add_widget(self.iMenu)
        if(self.NLayout.parent == None):
            self.Screen1.add_widget(self.NLayout)
        if(self.NavDrawer.parent == None):
            self.NLayout.add_widget(self.NavDrawer)
        if(self.CND.parent == None):
            self.NavDrawer.add_widget(self.CND)
        ###############################
        LayoutsApp.title   = 'Navigation Drawer'
        self.CND.NavDrawer = self.NavDrawer
        self.CND.Initialize()
        return self.Screen1

##############################################################
##############################################################
    
if __name__ == "__main__":
    LayoutsApp().run()

