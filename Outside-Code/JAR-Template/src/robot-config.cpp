#include "vex.h"

using namespace vex;
using signature = vision::signature;
using code = vision::code;

// A global instance of brain used for printing to the V5 Brain screen
brain  Brain;

// VEXcode device constructors
motor Motor1 = motor(PORT1, ratio6_1, false);
motor Motor11 = motor(PORT11, ratio6_1, false);
motor Motor10 = motor(PORT10, ratio6_1, true);
motor Motor20 = motor(PORT20, ratio6_1, true);
inertial Inertial17 = inertial(PORT17);

// VEXcode generated functions



/**
 * Used to initialize code/tasks/devices added using tools in VEXcode Pro.
 * 
 * This should be called at the start of your int main function.
 */
void vexcodeInit( void ) {
  // nothing to initialize
}