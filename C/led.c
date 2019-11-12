
/*
 * Rol luik status is de huidige stand van het rolluik.
 * 1 = Opgerold
 * 2 = Uitgerold
 * 3 = Bezig met oprollen/uitrollen
 */
volatile int rol_luik_input = 1;
volatile int rol_luik_status = 1;
#define CHECK_BIT(var,pos) ((var) & (1<<(pos)))
/*
 * PIND2 = Green LED
 * PIND3 = Yellow LED
 * PIND4 = Red LED
 */
#define GREEN 2
#define YELLOW 3
#define RED 4

void set_rol_luik_status(int status) {
	rol_luik_status = status;
}

void turn_led_on(int led) {
	PORTD |= (1 << led);
}

void turn_led_off(int led) {
	PORTD &= ~(1 << led);
}

//Get the current light status.
int get_light_status () {
	return rol_luik_status;
}

// FUNCTION BLINK, EVERY "Aantal_keer" is 5 ms. This will blink the yellow light.
void blink(int aantal_keer) {
	int klaar = 0;
	while (klaar < aantal_keer)
	{
		if(klaar % 2 == 0) {
			if(CHECK_BIT(PORTD, YELLOW)) {
				turn_led_off(YELLOW);
			}
			} else {
			if(!CHECK_BIT(PORTD, YELLOW)) {
				turn_led_on(YELLOW);
			}
		}
		_delay_ms(3);
		klaar++;
	}
	turn_led_off(YELLOW);

}

//Turn motor on (this controls the light)
void turn_motor_on() {
	if(CHECK_BIT(PORTD, RED)){
		turn_led_off(RED);
	}
	if(!CHECK_BIT(PORTD, GREEN)) {
		turn_led_on(GREEN);
		rol_luik_status = 2;
	}
}

//Turn motor off (this controls the light)
void turn_motor_off() {
	if(CHECK_BIT(PORTD, GREEN)) {
		turn_led_off(GREEN);
	}
	if(!CHECK_BIT(PORTD, RED)) {
		turn_led_on(RED);
		rol_luik_status = 1;
	}
}

//Check_lights gets the input and decides what should happen.
void check_lights(int input) {
	if(input == 1) {
		rol_luik_status = 1;
		turn_motor_off();
	}
	if (input == 2) {
		rol_luik_status = 2;
		turn_motor_on();
	}
	if(input == 3) {
		rol_luik_status = 3;
		blink(6);
	}
}
