/*
* gemiddelde.c
* This is only used if the slow (langzaam) is enabled.
* This calculates the averages of the sensors.
*/


int get_afstand();
int get_licht();
int get_temp();

int gemiddelde_temp = 0;
int gemiddelde_licht = 0;
int gemiddelde_afstand = 0;

int gemiddelde_temp_terug = 0;
int gemiddelde_licht_terug = 0;
int gemiddelde_afstand_terug = 0;

int aantal_temp = 0;
int aantal_licht = 0;
int aantal_afstand = 0;

//Calc temperature average
void bereken_temp_gemiddelde() {
	int temp =(int) getTemperature();
	gemiddelde_temp+=temp;
	aantal_temp++;
}

//Calc light average
void bereken_licht_gemiddelde() {
	int licht =(int) get_adc_value();
	gemiddelde_licht+=licht;
	aantal_licht++;
}

//Calc distance average
void bereken_afstand_gemiddelde() {
	int afstand =(int) get_distance();
	gemiddelde_afstand+=afstand;
	aantal_afstand++;
}

//Set all the averages in gemiddelde_temp_terug/gemiddelde_licht_terug/gemiddelde_afstand_terug
void get_gemiddelde() {
	gemiddelde_temp_terug = gemiddelde_temp/aantal_temp;
	gemiddelde_licht_terug = gemiddelde_licht/aantal_licht;
	gemiddelde_afstand_terug = gemiddelde_afstand/aantal_afstand;
	gemiddelde_temp = 0;
	gemiddelde_afstand = 0;
	gemiddelde_licht = 0;
	aantal_licht = 0;
	aantal_temp = 0;
	aantal_afstand = 0;
}

//Get average temperature
int get_temp() {
	return gemiddelde_temp_terug;
}

//Get average light
int get_licht() {
	return gemiddelde_licht_terug;
}

//Get average distance
int get_afstand() {
	return gemiddelde_afstand_terug;
}