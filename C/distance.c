#include <stdlib.h>
volatile uint64_t gv_counter= 0; // 16 bit counter value
volatile uint8_t current_distance = 0;

int get_current_distance(void);

void init_timer (void){
	TCCR0A |= (1 << WGM01);

	// Set the value that you want to count to
	OCR0A = 0x0;

	TIMSK0 |= (1 << OCIE0A);    //Set the ISR COMPA vect

	sei();         //enable interrupts



	// set prescaler to 256 and start the timer

}

void calculate_distance() {
	PORTD = 0x00;
	_delay_us(10);
	PORTD = (1<<6);
	TCCR0B |= (1 << CS00);
	gv_counter = 0;
	while(PIND & (1 << 7)){}
	current_distance = (uint8_t) (gv_counter*8)/58;
	show_distance((uint16_t) current_distance);
}

int get_current_distance(){
	current_distance = (int) current_distance;
	return current_distance;
}

ISR (TIMER0_COMPA_vect)
{
	gv_counter++;
}