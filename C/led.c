
/*
 * Rol luik status is de huidige stand van het rolluik.
 * 1 = Opgerold
 * 2 = Uitgerold
 * 3 = Bezig met oprollen/uitrollen
 */
volatile int rol_luik_status = 1;
volatile int aantal_aan = 0;
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
	PORTD = (1 << led);
}

void turn_led_off(int led) {
	PORTD = PORTD ^ (1 << led);
}

int get_light_status () {
	return rol_luik_status;
}

void check_lights(void) {
	PORTD = 0x00;
	if(rol_luik_status == 1) {
		turn_led_on(RED);
	}
	if(rol_luik_status == 2) {
		turn_led_on(GREEN);
	}
	if(rol_luik_status == 3) {
// 		if(aantal_aan > 10) {
// 			turn_led_on(YELLOW);	
// 			if (aantal_aan > 20) {
// 				aantal_aan = 0;
// 			}
// 		}
// 		aantal_aan++;
		turn_led_on(YELLOW);
	}
}