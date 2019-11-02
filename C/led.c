
/*
 * Rol luik status is de huidige stand van het rolluik.
 * 1 = Opgerold
 * 2 = Uitgerold
 * 3 = Bezig met oprollen/uitrollen
 */
volatile int rol_luik_status = 1;
volatile int oude_status = 0;
volatile int aantal_aan = 0;
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

int get_light_status () {
	return rol_luik_status;
}

void check_lights(void) {
	if(rol_luik_status == 1) {
		if(CHECK_BIT(PORTD, GREEN)) {
			turn_led_off(GREEN);
			oude_status = 2;
		}
		if(CHECK_BIT(PORTD, YELLOW)) {
			turn_led_off(YELLOW);
		}
		
		if(!CHECK_BIT(PORTD, RED)) {
			turn_led_on(RED);
		}
	}
	if(rol_luik_status == 2) {
		if(CHECK_BIT(PORTD, RED)) {
			turn_led_off(RED);
			oude_status = 1;
		}
		if(CHECK_BIT(PORTD, YELLOW)) {
			turn_led_off(YELLOW);
		}
		
		if(!CHECK_BIT(PORTD, GREEN)) {
			turn_led_on(GREEN);
		}
	}
	if(rol_luik_status == 3) {
		if(CHECK_BIT(PORTD, GREEN)) {
			turn_led_off(GREEN);
		}
		if(CHECK_BIT(PORTD, RED)) {
			turn_led_off(RED);
		}
		
		if(oude_status == 1) {
			turn_led_on(RED)
		}
		
		if(oude_status == 2) {
			turn_led_on(RED)
		}
				
		aantal_aan++;
		if(aantal_aan < 5) {
			if(!CHECK_BIT(PORTD, YELLOW)) {
				turn_led_on(YELLOW);
			}
		} else {
			if(CHECK_BIT(PORTD, YELLOW)) {
				turn_led_off(YELLOW);
			}
			if(aantal_aan >= 10) {
				aantal_aan = 0;
			}
		}
	}
}