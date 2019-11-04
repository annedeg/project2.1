#include <avr/io.h>
volatile int light_off = 0;
void turn_light_off() {
	light_off = 1;
}

void init_adc()
{
	// ref=Vcc, left adjust the result (8 bit resolution),
	// select channel 1 (PC1 = input)
	ADMUX = 0x00;
	ADMUX = MUX1|(1<<REFS0)|(1<<ADLAR);
	// enable the ADC & prescale = 128
	ADCSRA = (1<<ADEN)|(1<<ADPS2)|(1<<ADPS1)|(1<<ADPS0);
}

int get_adc_value()
{
	if(light_off != 1) {
		init_adc();
		ADCSRA |= (1<<ADSC); // start conversion
		loop_until_bit_is_clear(ADCSRA, ADSC);
		int light_value = (int) ADCH;
		show_distance(light_value);
		return light_value; // 8-bit resolution, left adjusted
	}
	return 0;
}

