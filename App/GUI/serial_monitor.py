import dearpygui.dearpygui as dpg
import threading
from Core import get_serial

# everything here is crap, make it better
data_y = []
data_x = []

def update_plot():
    sample = 1
    while True:
        data_x.append(sample)
        data_y.append(get_serial())
        dpg.set_value('line', [list(data_x[-100:]), list(data_y[-100:])])
        sample += 1
        dpg.fit_axis_data('xaxis')
        dpg.fit_axis_data('yaxis')


def serial_monitor():
    # dog shit
    with dpg.window(pos=(10,10)):
        with dpg.plot(label="Dog Shit Serial Monitor", height=400, width=500):
            dpg.add_plot_axis(dpg.mvXAxis, label="x", tag="xaxis")
            dpg.add_plot_axis(dpg.mvYAxis, label="y", tag="yaxis")
            dpg.add_line_series(data_x, data_y, tag='line', parent="yaxis")
        dpg.add_checkbox(label="Auto-fit axis limits", tag="auto_fit_checkbox", default_value=False)
    thread = threading.Thread(target=update_plot)
    thread.start()
