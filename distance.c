#include <stdlib.h>
volatile uint64_t gv_counter= 0; // 16 bit counter value


void init_timer (void){
	TCCR0A |= (1 << WGM01);

	// Set the value that you want to count to
	OCR0A = 0x0;

	TIMSK0 |= (1 << OCIE0A);    //Set the ISR COMPA vect

	sei();         //enable interrupts
	// set prescaler to 256 and start the timer}

int get_distance() {
	//enable trigger bit
	PORTD &= ~(1<<6);
	_delay_us(10);
	//dissable trigger bit
	PORTD |= (1<<6);
	//Set timer
	TCCR0B |= (1 << CS00);
	
	//set counter
	gv_counter = 0;
	
	//Wait until echo bit is done
	while(PIND & (1 << 7)){}
		
	//get counter value. and calculate distance
	uint8_t current_distance = (gv_counter*8)/58;
	int distance = (int) current_distance;
	//Show distance on display
	show_distance(distance);
	//return distance
	return distance;
}


//This is an interupt that increases the counter.
ISR (TIMER0_COMPA_vect)
{
	gv_counter++;
}