#include "esp_lcd_types.h"
#include "ulgl.h"
#include "oled_esp_lcd.h"
#include <stdint.h>

uint8_t screen[1024];

void app_main(void) {
    esp_lcd_panel_handle_t panel = initialise_oled();
    draw_text("Radio Control Club", 3, screen);
    display_bitmap(panel, screen);
}

