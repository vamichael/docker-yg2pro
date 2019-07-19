#include "esphome.h"
#include "HX711.h"

#define DOUT  D2
#define CLK  D3

class CustomHX711 : public PollingComponent, public Sensor {
 public:

  CustomHX711(int poll=5000) : PollingComponent(poll){}
  CustomHX711(int poll=5000, float offset = -7050) : PollingComponent(poll)
  {
     calibration = offset;
  }

  float calibration; // = -7050; //-11000
  HX711 scale;
  int polltime;

  void setup(int poll, float offset){
    calibration = offset;
  }

  void setup() override {
    scale.begin(DOUT, CLK);
    scale.set_scale(calibration);
    scale.tare();
  }

  void update() override {

     //Serial.println(scale.read());                 // print a raw reading from the ADC
     //Serial.println(scale.read_average(20));       // print the average of 20 readings from the ADC
     //Serial.println(scale.get_value(5));		// print the average of 5 readings from the ADC minus the tare weight, set with tare()
     //Serial.println(scale.get_units(5), 1);        // print the average of 5 readings from the ADC minus tare weight, divided

     float w = scale.get_units(20);


     //w = roundf(w * 100) / 100;
     publish_state(w);
  }
};

