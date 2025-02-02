import logging

import dearpygui.dearpygui as dpg
from dearpygui import demo

import Core 
import GUI

logger = logging.getLogger("Core.Main")
def main():
    dpg.create_context()
    dpg.create_viewport(title="SkyGauge")
    core_logger = logging.getLogger("Core")
    gui_logger = logging.getLogger("GUI")
    core_logger.setLevel(logging.DEBUG)
    gui_logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "[{threadName}][{asctime}] [{levelname:<8}] {name}: {message}",
        "%H:%M:%S",
        style="{",
    )

    with dpg.window(tag="Primary Window"):
        with dpg.menu_bar():
            with dpg.menu(label="Tools"):
                dpg.add_menu_item(
                    label="Show Performance Metrics", callback=dpg.show_metrics
                )
                dpg.add_menu_item(
                    label="Logger Stress Test", callback=GUI.logger_stress_test
                )
                dpg.add_menu_item(
                    label="Show GUI demo", callback=demo.show_demo
                )
            dpg.add_button(
                label="Music",
                callback=lambda: GUI.MusicVisualiser(
                    "./Data/Audio/clodman.mp3"
                ).start(),
            )
            dpg.add_button(
                label="Log Serial",
                callback=GUI.serial_monitor
            )

    log = GUI.Logger()
    log.setFormatter(formatter)
    core_logger.addHandler(log)
    gui_logger.addHandler(log)

    dpg.setup_dearpygui()
    dpg.set_primary_window("Primary Window", True)
    dpg.set_viewport_vsync(False)
    dpg.show_viewport(maximized=True)
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == "__main__":
    main()
