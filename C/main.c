
/* 
 * main.c
 *
 * Created: 10/15/2019 4:38:32 PMs
 * Author : Anne de Graaff
 */ 

//Set CPU speed.
#define F_CPU 16E6

//Include all the libraries.
#include <avr/io.h>
#include <util/delay.h>
#include <stdlib.h>
#include <avr/sfr_defs.h>

//Setting to toggle between every second some data and every 60 seconds with 40/30 seconds refreshrate.
int langzaam = 0;

//Include our files
#include "AVR_TTC_scheduler.c"
#include "display.c"
#include "led.c"
#include "distance.c"
#include "temperatuur.c"
#include "licht.c"
#include "config.c"
#include "gemiddelde.c"s
#include "communication.c"

 
//Initialize all the needed init functions.
void init_all() {
	init_ports();
	uart_init();
	reset_display();
	check_lights(1);
	init_timer();
}

//Set ports on the arduinos
void init_ports() {
	DDRB = 0xFF;
	DDRD = 0x5C;
} 

//Main loop on the arduino
int main(void)
{	
	//Setup scheduler
	SCH_Init_T1(); 
	//Start scheduler
	SCH_Start();
	//Run the init_all function once and immediately
	SCH_Add_Task(init_all, 0, 0);
	//Check every 10 ticks if the GUI has send data 
	SCH_Add_Task(receive_if_send, 0, 10);
	
	//Check variable and choose correct
	if(langzaam == 0) { 
		//Send every 100 ticks all the sensor data
		SCH_Add_Task(send_all, 0, 100);
	} else {
		//calculate averages every 4000/6000/8000 ticks.
		SCH_Add_Task(bereken_afstand_gemiddelde, 0, 4000);
		SCH_Add_Task(bereken_licht_gemiddelde, 0, 6000);
		SCH_Add_Task(bereken_temp_gemiddelde, 0, 8000);
		//send the data to GUI every 12000 ticks.
		SCH_Add_Task(send_all, 0, 12000);
	}
	//This will run until the Arduino receives data from GUI. Until then this will make the arduino work without GUI.
	SCH_Add_Task(run_config, 0, 400);
	/* Replace with your application code */
	while (1) {
		//Run all the added tasks.
		SCH_Dispatch_Tasks();
	}
	return 0;
}