#define UBBRVAL 51
#include <stdint.h>
#include <math.h>
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
	// wait for an empty transmit buffer
	// UDRE is set when the transmit buffer is empty
	_delay_ms(10);
	if(UCSR0A << UDRE0) {
	// send the data
		UDR0 = data;
	}
}
/* receive data */
uint8_t receive() {
	loop_until_bit_is_set(UCSR0A, 7);
	return UDR0;
}


void receive_and_transmit() {
	volatile uint8_t data = 0;
	while (data == 0) {
		data = receive();
		transmit(data);
	}
}

void send_status() {
	transmit(rol_luik_status);
}

void check_status() {
	uint8_t data = 0x00;
	data = receive();
	if(data == 0x1) {
		set_rol_luik_status(1);
	}
	if(data == 0x2) {
		set_rol_luik_status(2);
	}
	if(data == 0x3) {
		set_rol_luik_status(3);
	}
	
}

void send_all() {
	int light_bit = 2;
	int ult_bit = 8;
	int temp_bit = 10;
	int light_bit2 = 7;
	int cont_bit = 5;
	
	uint8_t temp =(uint8_t) 30;
	uint8_t light2=(uint8_t) 50;
	uint8_t distance =(uint8_t) 212;
	uint8_t light =(uint8_t) 3;
	
	uint8_t binary[32];
	int counter = 0;
	for(int i = 0; i<=light_bit;i++) {
		if(light%2==1) {
			binary[counter] = 1;
			light = (light-1)/2
		} else {
			binary[counter] = 0;
			light = (light)/2
		}
		counter++;
	}
	for(int i = 0; i<=distance;i++) {
		if(distance%2==1) {
			binary[counter] = 1;
			distance = (distance-1)/2
			} else {
			binary[counter] = 0;
			distance = (distance)/2
		}
		counter++;
	}
	for(int i = 0; i<=temp_bit;i++) {
		if(temp%2==1) {
			binary[counter] = 1;
			temp = (temp-1)/2
			} else {
			binary[counter] = 0;
			temp = (temp)/2
		}
		counter++;
	}
	for(int i = 0; i<=light_bit2;i++) {
		if(light2%2==1) {
			binary[counter] = 1;
			light2 = (light2-1)/2
			} else {
			binary[counter] = 0;
			light2 = (light2)/2
		}
		counter++;
	}
	

}

void receive_all() {
	uint8_t byte_1 = receive();
	uint8_t byte_2 = receive();
	uint8_t byte_3 = receive();
	uint8_t byte_4 = receive();
	int byteArray[32];
	uint8_t byteArray2[4]={byte_1,byte_2,byte_3,byte_4};

	int al = 0;
	for(int a=0; a<4; a++){
		for(int i=7; i>=0; i--){
			byteArray[al] = (int)(byteArray2[a] >> i) & 1;
			al++;
		}
	}
	uint8_t byte[4];
	al = 0;
	for(int a=0; a<4; a++){
		int extra = 0;
		for(int i=7; i>=0; i--){
			if(byteArray[al] & 1) {
				extra += (int)1<<i;
			}
			al++;
		}
		byte[a] = extra;
		
	}
	
	for(int a=0; a<4; a++){
		transmit(byte[a]);
	}
}