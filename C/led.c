
/*
 * Rol luik status is de huidige stand van het rolluik.
 * 1 = Opgerold
 * 2 = Uitgerold
 * 3 = Bezig met oprollen/uitrollen
 */
volatile uint8_t rol_luik_status = 2;

/*
 * PIND2 = Green LED
 * PIND3 = Yellow LED
 * PIND4 = Red LED
 */
#define GREEN 2
#define YELLOW 3
#define RED 4

void turn_led_on(int led) {
	PORTD = (PORTD | (1 << led));
}

void turn_led_off(int led) {
	PORTD = PORTD ^ (1 << led);
}

void knipperen(int led) {
	turn_led_on(led);
	_delay_ms(50);
	turn_led_off(led);
	_delay_ms(50);
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
		knipperen(YELLOW);
	}
}