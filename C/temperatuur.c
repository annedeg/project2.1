volatile int temp_off = 0;
//This function is designed to be able to ignore all the data from the temprature if this function is called.
void turn_temp_off() {
	temp_off = 1;
}
  
void setupVolt() {
	ADCSRA |= ((1<<ADPS2)|(1<<ADPS1)|(1<<ADPS0));    //Prescaler at 128 so we have an 125Khz clock source
	ADMUX = 0x00;
	ADMUX |= (1<<REFS0);
	ADMUX &= ~(1<<REFS1);           //Avcc(+5v) as voltage reference
	ADCSRB &= ~((1<<ADTS2)|(1<<ADTS1)|(1<<ADTS0));    //ADC in free-running mode
	ADCSRA |= (1<<ADATE);                //Signal source, in this case is the free-running
	ADCSRA |= (1<<ADEN);                //Power up the ADC
	ADCSRA |= (1<<ADSC);                //Start converting
}

int getTemperature() {
	if(temp_off != 1) {
		setupVolt();
		_delay_ms(5);
		double result;
		int end_result;
		int volt = ADCW;                //get amount of volts
		if(ADCW != 0) {
		double mv = volt / 0.2;         //convert it into microvolts
		result = ((mv - 500)/10);       //change volts to temperature in degrees celsius
		result = result * 10;
		end_result = (int)result;
		//return temperature
		return end_result;
		}
	}
	return 0;
	
}