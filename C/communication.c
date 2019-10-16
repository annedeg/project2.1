#define UBBRVAL 51
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
	loop_until_bit_is_set(UCSR0A, UDRE0);
	// send the data
	UDR0 = data;
}
/* receive data */
uint8_t receive() {
	UDR0 = 0;
	loop_until_bit_is_set(UCSR0A, RXC0);
	return UDR0;
}

// void receive_and_transmit() {
// 	volatile uint8_t data = 0;
// 	while (data == 0) {
// 		data = receive();
// 		transmit(data);
// 	}
// }
