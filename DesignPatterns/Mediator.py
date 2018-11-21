# https://py.checkio.org/blog/design-patterns-part-2/


class WindowBase(object):
    def show(self):
        raise NotImplementedError()

    def hide(self):
        raise NotImplementedError()


class MainWindow(WindowBase):
    def show(self):
        print('Show MainWindow')

    def hide(self):
        print('Hide MainWindow')


class SettingsWindow(WindowBase):
    def show(self):
        print('Show SettingsWindow')

    def hide(self):
        print('Hide SettingsWindow')


class HelpWindow(WindowBase):
    def show(self):
        print('Show HelpWindow')

    def hide(self):
        print('Hide HelpWindow')


class WindowMediator(object):
    def __init__(self):
        self.windows = dict.fromkeys(['main', 'settings', 'help'])

    def show(self, win):
        for window in self.windows.values():
            if not window is win:
                window.hide()
        win.show()

    def set_main(self, win):
        self.windows['main'] = win

    def set_settings(self, win):
        self.windows['settings'] = win

    def set_help(self, win):
        self.windows['help'] = win


main_win = MainWindow()
settings_win = SettingsWindow()
help_win = HelpWindow()

mediator = WindowMediator()
mediator.set_main(main_win)
mediator.set_settings(settings_win)
mediator.set_help(help_win)

mediator.show(settings_win)
mediator.show(help_win)
