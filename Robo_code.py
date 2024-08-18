import threading
import time

'''FUNCTIONS FOR ROBOT, DO NOT CHANGE'''

def set_speed(speed: int):
    '''Is used to change the speed of the robot, only one integer is expected | set_speed(speed=100)'''
    if speed > 100 or speed <= 0:
        raise ValueError( "\033[1mSpeed must be in between 1 and 100" )
    chassis_ctrl.set_wheel_speed( speed, speed, speed, speed )

def move( distance: float, direction: str ):
    '''Is used to move the robot, currently can only move forward, one float is expected as distance in range 0, 5 (meters) and one direction is expected 'S','B','R','L' '''
    if direction == 'S':
        chassis_ctrl.move_with_distance( 0, distance )
    elif direction == 'B':
        chassis_ctrl.move_with_distance( distance, 0 )  # NEEDS TESTING
    elif direction == 'R':
        chassis_ctrl.move_with_distance( 0, 0, distance )  # NEEDS TESTING
    elif direction == 'L':
        chassis_ctrl.move_with_distance( 0, 0, -distance )  # NEEDS TESTING

def rotate( direction: int, degrees: int ):
    '''Is used to rotate the robot, not currently working, one integer is expected as direction, 0 for clockwise, 1 for anticlockwise and another integer is expected as degrees with in range 0 to 360'''
    if direction == 1:
        chassis_ctrl.rotate_with_degree(degrees, rm_define.anticlockwise)
    else:
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, degrees)

def IR_distance( ):
    '''Returns how far away the IR scanner detects a wall'''
    return ir_distance_sensor_ctrl.get_distance_info(1)

def stop_everything( ):
    '''Stops everything to do with the chassis (movement)'''
    chassis_ctrl.stop( )

def led_set_color( *RGB: int ):
    '''Is used to set the LED colour of the robot, expects 3 integer variables as RGB'''
    led_ctrl.set_bottom_led( rm_define.armor_bottom_all, RGB[ 0 ], RGB[ 1 ], RGB[ 2 ], rm_define.effect_always_on )

def led_flash( time: int ):
    '''Is used to flash the led, expects 1 float variable as time'''
    led_ctrl.set_flash( rm_define.armor_all, time )

def led_off( ):
    '''Is used to turn all led's off'''
    led_ctrl.turn_off( rm_define.armor_all )

def armor_sensitivity( sensitivity: int ):
    '''Is used to change armor hit sensitivity, expects 1 int variable as sensitivity'''
    armor_ctrl.set_hit_sensitivity( sensitivity )

def thread( target: str, *args ):
    '''Used to thread expects 1 required variable and many unrequired| thread(FUNCTION_NAME, ARG1,CAN GO TO INFINITY)'''
    if args:
        threading.Thread(target=target, args=args).start()
    else:
        threading.Thread(target=target).start()

def get_arm_pos( ):
    '''Returns robotic arms position'''
    return robotic_arm_ctrl.get_position( )

def arm_ctrl_abs( x: int, y: int, wait: bool ):
    '''Sets robots arm to an absoloute position, expects 2 intiger variables, 1 as a x variable the other as a y variable and 1 boolean variable as wait'''
    robotic_arm_ctrl.moveto( x, y, wait )

def arm_ctrl_rltv( x, y, wait ):
    '''Sets robots arm to an realitive position, expects 2 intiger variables, 1 as a x variable the other as a y variable and 1 boolean variable as wait'''
    robotic_arm_ctrl.move( x, y, wait )

def grip_open( ):
    '''Opens the gripper'''
    for i in range( 1, 10 ):
        gripper_ctrl.open( )

def grip_close( ):
    '''Closes the gripper'''
    for i in range( 1, 10 ):
        gripper_ctrl.close( )

def grip_power( power: int ):
    '''Sets the grippers power, must be an integer in range 1 to 4'''
    gripper_ctrl.update_power_level( power )

def grip_stop( ):
    '''Stops the gripper from doing anything'''
    gripper_ctrl.stop( )

def grip_is_closed( ):
    '''Returns True if gripper is closed otherwise, returns False'''
    return gripper_ctrl.is_closed( )

def grip_is_open( ):
    '''Returns True if gripper is open otherwise, returns False'''
    return gripper_ctrl.is_open( )


'''RAN BEFORE CODE'''

ir_distance_sensor_ctrl.enable_measure
robotic_arm_ctrl.recenter( )

'''SYNTAX OF CODE'''

rotate( direction = 0, degrees = 180 )
time.sleep( 2 )
set_speed( speed = 80 )
move( direction = 'S', distance = 0.2 )
if IR_distance( ) >= 10:
    move( direction = 'S', distance = 2 )
else:
    move( direction = 'B', distance = 1 )
move( direction = 'S', distance = 1 )
thread( led_set_color, 20, 20, 20 )
time.sleep( 2 )
led_set_color( 100, 100, 100 )
thread( led_flash, 1 )
time.sleep( 5 )
thread( led_off, None )
armor_sensitivity( sensitivity = 5 )
print( get_arm_pos( ) )
arm_ctrl_abs( x = 200, y = 800, wait = True )
time.sleep( 2 )
arm_ctrl_rltv( x = 200, y = -300, wait = False )
grip_power( 4 )
grip_open( )
time.sleep( 2 )
grip_close( )
grip_power( 1 )
grip_stop( )
