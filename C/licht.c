#include <asf.h>
#include <avr/io.h>

volatile uint8_t lightvalue;

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
		lightvalue = get_adc_value(); //put value in variable
		if(lightvalue > 0x7f)				//this if statement will limit it to 7 bits
		{
			lightvalue = 0x7f;					//if the value is more than 7 bits can handle it will make in maximum of 7 bits
		}
	}
	init_adc();								//these statements let the program run.
	while(1){
		loop();
	}
}
