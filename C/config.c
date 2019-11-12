volatile int handmatig = 1;

void run_config(void);
int config_temp = 15;
int config_light2 = 100;

//Set default config
void run_config()
{
	//Handmatig is set to zero if it makes contact with GUI and then it follow the configuration that the GUI provides.
	if(handmatig == 1) {
		int distance = get_distance();
		if(distance < 40) {
			turn_motor_off();
		} else if(distance > 180) {
			turn_motor_on();
		} else {
			blink(6);
		}
	} 
}