#!/usr/bin/env python3.11

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib
import repo_manager

class RepoSelector(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="PkgRepoSelector")
        self.set_border_width(10)
        self.set_default_size(400, 300)
        
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)
        
        title_label = Gtk.Label(label="Select Package Repository")
        vbox.pack_start(title_label, False, False, 0)

        if not repo_manager.REPOS:
            error_label = Gtk.Label(label="No repositories loaded. Please check the configuration.")
            vbox.pack_start(error_label, False, False, 0)
        else:
            for name in repo_manager.REPOS.keys():
                button = Gtk.Button(label=name)
                button.set_tooltip_text(f"Select the {name} repository")
                button.connect("clicked", self.on_repo_selected, name)
                vbox.pack_start(button, False, False, 0)

        quit_button = Gtk.Button(label="Quit")
        quit_button.set_tooltip_text("Quit the application")
        quit_button.connect("clicked", self.quit)
        vbox.pack_start(quit_button, False, False, 0)

        self.statusbar = Gtk.Statusbar()
        self.context_id = self.statusbar.get_context_id("status")
        vbox.pack_start(self.statusbar, False, False, 0)

    def on_repo_selected(self, widget, repo_name):
        dialog = Gtk.MessageDialog(
            transient_for=self,
            flags=0,
            message_type=Gtk.MessageType.QUESTION,
            buttons=Gtk.ButtonsType.YES_NO,
            text="Confirm Repository Change",
        )
        dialog.format_secondary_text(f"Do you want to change the repository to {repo_name}?")
        response = dialog.run()
        dialog.destroy()

        if response == Gtk.ResponseType.YES:
            self.show_progress("Updating repository configuration...")
            GLib.idle_add(self.update_repository, repo_name)

    def update_repository(self, repo_name):
        success, message = repo_manager.select_repo(repo_name)
        self.statusbar.push(self.context_id, message)
        self.show_message("Success" if success else "Error", message)
        return False

    def show_message(self, title, message):
        dialog = Gtk.MessageDialog(
            transient_for=self,
            flags=0,
            message_type=Gtk.MessageType.INFO if title == "Success" else Gtk.MessageType.ERROR,
            buttons=Gtk.ButtonsType.OK,
            text=title,
        )
        dialog.format_secondary_text(message)
        dialog.run()
        dialog.destroy()

    def show_progress(self, message):
        progress_dialog = Gtk.Dialog(
            transient_for=self,
            flags=0,
            title="Progress"
        )
        progress_dialog.set_modal(True)
        progress_dialog.set_decorated(False)
        label = Gtk.Label(label=message)
        progress_dialog.get_content_area().pack_start(label, True, True, 0)
        spinner = Gtk.Spinner()
        spinner.start()
        progress_dialog.get_content_area().pack_start(spinner, True, True, 0)
        progress_dialog.show_all()
        GLib.timeout_add(1000, progress_dialog.destroy)

    def quit(self, widget):
        Gtk.main_quit()

def launch_gui():
    win = RepoSelector()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()

if __name__ == "__main__":
    launch_gui()

