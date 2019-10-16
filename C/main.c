#define F_CPU 16E6

#include <avr/io.h>
#include <util/delay.h>
#include <stdlib.h>
#include <avr/sfr_defs.h>

#include "led.c"
#include "communication.c"
#include "AVR_TTC_scheduler.c"
/*
 * Algemene software.c
 *
 * Created: 10/15/2019 4:38:32 PM
 * Author : adgra
 */ 


void init_ports() {
	DDRD = 0x1C;
}


void init_all() {
	init_ports();
	uart_init();
}

void send_status() {
	transmit(rol_luik_status);
}

void check_status() {
	uint8_t data = receive();
	if(data & 0x1 || data & 0x2 || data & 0x3) {
		rol_luik_status = data;
		
	}
}

int main(void)
{
	SCH_Init_T1();
	SCH_Start();
	SCH_Add_Task(init_all, 0, 0);
	SCH_Add_Task(check_lights, 10, 1);
/*	SCH_Add_Task(send_status, 100, 1);*/
	SCH_Add_Task(check_status, 100, 1);
    /* Replace with your application code */
    while (1) 
    {
		SCH_Dispatch_Tasks();

    }
}