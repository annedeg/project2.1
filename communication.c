#define UBBRVAL 51
#include <stdint.h>
#include <math.h>
volatile extern uint8_t current_distance;

/*
* Communication.c is one of the most essential pieces in our C code.
* It gets all the input and it transmit every data.
*/

void uart_init()
{
	// set the baud rate
	UBRR0H = 0;
	UBRR0L = UBBRVAL;
	// disable U2X mode
	UCSR0A = 0;
	// enable transmitter
	UCSR0B = _BV(TXEN0) | _BV(RXEN0);
	// set frame format : asynchronous, 8 data bits, 1 stop bit, no parity
	UCSR0C = _BV(UCSZ01) | _BV(UCSZ00);
}
/* Transmit data */
void transmit(uint8_t data)
{
	loop_until_bit_is_set(UCSR0A, UDRE0);
	UDR0=data;
}
/* receive data */
uint8_t receive() {
	loop_until_bit_is_set(UCSR0A, 7);
	return UDR0;
}

/* Check if data was send. If so save it and set the lights accordingly. */
void receive_if_send() {
	if(UCSR0A & (1 << 7)) {
		uint8_t data = receive();
		data = (int) data;
		check_lights(data);
		handmatig = 0;
	} else {
		check_lights(rol_luik_status);
	}
} 

// Send all the data in a specific way. This design can be found in our technical design what you can find here: https://drive.google.com/file/d/1I5dLaODou5_8nIarDF2WDtAQAurOe5Mj/view?usp=sharing
void send_all() {
	int counter = 0;
	
	//Set the amount of bits every value can have.
	int light_bit = 2;
	int ult_bit = 8;
	int temp_bit = 10;
	int light_bit2 = 7;
	int cont_bit = 5;
	
	uint8_t temp = 0;
	uint8_t light2 = 0;
	uint8_t dist = 0;
	
	if(langzaam == 0) {
		temp =(uint8_t) getTemperature();
		light2=(uint8_t) get_adc_value();
		dist = (uint8_t) get_distance();
	} else {
		get_gemiddelde();
		temp =(uint8_t) get_temp();
		light2=(uint8_t) get_licht();
		dist = (uint8_t) get_afstand();

	}
	uint8_t light = (uint8_t) get_light_status();
	int totaal = 0;
	uint8_t binary[32];
	uint8_t byte[4][8];
	uint8_t getal[4];
	
/*
 * test.c
 *
 * Created: 10/29/2019 12:18:45 PM
 * Author : adgra
 */ 

	//Build binary string.
	for(int i = 0; i<light_bit;i++) {
		if(light%2==1) {
			binary[counter] = 1;
			totaal+=1;
			light = (light-1)/2;
			} else {
			binary[counter] = 0;
			light = (light)/2;
		}
		counter+=1;
	}
	for(int i = 0; i<ult_bit;i++) {
		if(dist%2==1) {
			binary[counter] = 1;
			totaal+=1;
			dist = (dist-1)/2;
			} else {
			binary[counter] = 0;
			dist = (dist)/2;
		}
		counter+=1;
	}
	for(int i = 0; i<temp_bit;i++) {
		if(temp%2==1) {
			binary[counter] = 1;
			totaal+=1;
			temp = (temp-1)/2;
			} else {
			binary[counter] = 0;
			temp = (temp)/2;
		}
		counter+=1;
	}
	for(int i = 0; i<light_bit2;i++) {
		if(light2%2==1) {
			binary[counter] = 1;
			totaal+=1;
			light2 = (light2-1)/2;
			} else {
			binary[counter] = 0;
			light2 = (light2)/2;
		}
		counter+=1;
	}
	uint8_t totaal2 = (uint8_t) totaal;
	for(int i = 0; i<cont_bit;i++) {
		if(totaal2%2==1) {
			binary[counter] = 1;
			totaal2 = (totaal2-1)/2;
			} else {
			binary[counter] = 0;
			totaal2 = (totaal2)/2;
		}
		counter+=1;
	}

	//Set data in an array.
	volatile int ding[4];
	int aantal = 0;
	for(int i=0; i<4; i++) {
		ding[i]=0;
		for(int a=0; a<8;a++) {
			if(binary[aantal] == 1) {
				ding[i]+= (int)(pow(2, (7-a))+0.5);
			}
			aantal++;
		}
	}
	//First byte is to be sure data was send.
	transmit(0xff);
	
	//Then we transfer 4 bytes of data.
	transmit(ding[0]);
	transmit(ding[1]);
	transmit(ding[2]);
	transmit(ding[3]);

}