#include "esphome.h"

class Foobar : public PollingComponent, public Sensor
{
 public:

  Foobar(int poll=5000) : PollingComponent(poll){}

  int fubar=0;
  int multiplier=0;

  void bar(int x)
  {
     multiplier=x;
     ESP_LOGD("custom", "multiplier changed to: %i",  multiplier);
  }

  void setup() override {
     bar(1);
//     subscribe("the/topic", &Foobar::on_message);


    // also supports JSON messages
   // subscribe_json("the/json/topic", &MyCustomComponent::on_json_message);
  }

  void on_message(const std::string &payload) {
     ESP_LOGD("MQTT!!!", "xxx");
  }

  void update() override {
     if (((rand() % 5) + 1) == 5)   //1 out of 5 times throw a random number into things
     {
	    int x;
        do {
           x=(rand() % 5) + 1;
        } while (multiplier==x);
		ESP_LOGD("TRICKERY!!!", "multiplier changed!!");
        bar(x);
		// hey, multiplier isn't the same value that was passed in.
		// we should somehow report this new value back to Home Assistant
     }

     fubar += (1*multiplier);
     publish_state(fubar);
     ESP_LOGD("custom", "fubar: %i", fubar);
  }
};


