void setupVolt() {
    DDRD = 0xFF;

    ADCSRA |= ((1<<ADPS2)|(1<<ADPS1)|(1<<ADPS0));    //Prescaler at 128 so we have an 125Khz clock source
    ADMUX |= (1<<REFS0);
    ADMUX &= ~(1<<REFS1);                //Avcc(+5v) as voltage reference
    ADCSRB &= ~((1<<ADTS2)|(1<<ADTS1)|(1<<ADTS0));    //ADC in free-running mode
    ADCSRA |= (1<<ADATE);                //Signal source, in this case is the free-running
    ADCSRA |= (1<<ADEN);                //Power up the ADC
    ADCSRA |= (1<<ADSC);                //Start converting
    //https://hekilledmywire.wordpress.com/2011/03/16/using-the-adc-tutorial-part-5/
}

double getTemperature() {
    double result;
    int end_result;
    int volt = ADCW;                //get amount of volts
    double mv = volt / 0.2;         //convert it into microvolts
    result = ((mv - 500)/10);       //change volts to temperature in degrees celsius
    result = result * 10;
    end_result = (int)result;
    return end_result;              //return temperature
}

int main(void)
{
    init_ports();
    reset_display();
    int temperature;
    setupVolt();
    while(1) {
        temperature = getTemperature();
    }
    return temperature;
}
