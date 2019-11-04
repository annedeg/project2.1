#define F_CPU 16E6

#include <avr/io.h>
#include <util/delay.h>
#include <stdlib.h>
#include <avr/sfr_defs.h>

#include "display.c"
#include "led.c"
#include "communication.c"
#include "AVR_TTC_scheduler.c"
#include "distance.c"
#include "temperatuur.c"
#include "licht.c"


/* 
 * Algemene software.c
 *
 * Created: 10/15/2019 4:38:32 PMs
 * Author : adgra
 */ 


void init_ports() {
	DDRB = 0xFF;
	DDRD = 0x5C;

}
 

void init_all() {
	init_ports();
	uart_init();
	reset_display();
	check_lights(1);
	init_timer();
	turn_temp_off();
}
 

int main(void)
{	
	SCH_Init_T1();
 	SCH_Start();
 	SCH_Add_Task(init_all, 0, 0);
	SCH_Add_Task(receive_and_transmit, 0, 0);
	SCH_Add_Task(receive_if_send, 0, 10); 
	SCH_Add_Task(send_all, 0, 10);
    /* Replace with your application code */
    while (1) {
	    SCH_Dispatch_Tasks();
    }
	return 0;
}