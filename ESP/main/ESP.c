#include "freertos/idf_additions.h"
#include "freertos/projdefs.h"
#include "portmacro.h"
#include "vvm_interface.h"
#include <stdint.h>
// #include "ULGL.h"
// #include "ssd1306_oled.h"

uint8_t screen[1024];

void print_values(void* uart_queue) {
    uint8_t *data = (uint8_t *)malloc(1024);
    while(1){
        if (xQueueReceive(*(QueueHandle_t *)uart_queue, data, (TickType_t) 0)){
            printf("%s\n", (char *) data);
        }
    }
}

void app_main(void) {
    // esp_lcd_panel_handle_t panel = initialise_oled();
    // draw_text("Radio Control Club", 3, screen);
    // display_bitmap(panel, screen);
    //
    QueueHandle_t uart_queue = xQueueCreate(25, 1024);  // 1024 is the buffer_size in read_uart_data anyways
    xTaskCreate(read_uart_data, "vvm_uart_read_task", 3076, &uart_queue, 0, NULL);
    xTaskCreate(print_values, "print_task", 3076, &uart_queue, 10, NULL);
}

