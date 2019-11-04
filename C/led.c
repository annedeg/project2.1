
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
	rol_luik_input = status;
}

void turn_led_on(int led) {
	PORTD |= (1 << led);
}

void turn_led_off(int led) {
	PORTD &= ~(1 << led);
}

int get_light_status () {
	return rol_luik_status;
}

// FUNCTION BLINK, EVERY "Aantal_keer" is 5 ms.
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
		_delay_ms(5);
		klaar++;
	}
	turn_led_off(YELLOW);

}

void turn_motor_on() {
	if(CHECK_BIT(PORTD, RED)) {
		turn_led_off(RED);
		int klaar = 0;
		int aantal_aan = 1;
		blink(10);
	}
	if(!CHECK_BIT(PORTD, GREEN)) {
		turn_led_on(GREEN);
		rol_luik_status = 2;
	}
}

void turn_motor_off() {
	if(CHECK_BIT(PORTD, GREEN)) {
		turn_led_off(GREEN);
		int klaar = 0;
		int aantal_aan = 1;
		blink(10);
	}
	if(!CHECK_BIT(PORTD, RED)) {
		turn_led_on(RED);
		rol_luik_status = 1;
	}
}

void check_lights(int input) {
	if(input == 1) {
		turn_motor_off();
	}
	if (input == 2) {
		turn_motor_on();
	}
}
