#include <asf.h>
#include <avr/io.h>

int main (void)
{
	void init_adc()
	{
		// ref=Vcc, left adjust the result (8 bit resolution),
		// select channel 1 (PC1 = input)
		DDRB = 0xff;
		ADMUX = MUX1|(1<<REFS0)|(1<<ADLAR);
		// enable the ADC & prescale = 128
		ADCSRA = (1<<ADEN)|(1<<ADPS2)|(1<<ADPS1)|(1<<ADPS0);
	}
	uint8_t get_adc_value()
	{
		ADCSRA |= (1<<ADSC); // start conversion
		loop_until_bit_is_clear(ADCSRA, ADSC);
		return ADCH; // 8-bit resolution, left adjusted
	}
	void loop()
	{
		uint8_t lightvalue = get_adc_value(); //put value in variable
		if(lightvalue <= 0x32)				//this if/else statement is for testing
		{
			PORTB = 0x01;					//if it is darker, the light connected to PB0 will light up.
		}
		else
		{
			PORTB = 0x02;					//if it is lighter, the light connected to PB1 will light up.
		}
	}
	init_adc();								//these statements let the program run.
	while(1){
		loop();
	}
}
