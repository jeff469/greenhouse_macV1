import pyfirmata
import time


light_int_list=[0,0,0,0]

board = pyfirmata.Arduino('/dev/cu.wchusbserialfa130')
it = pyfirmata.util.Iterator(board)
it.start()

#Light sensor A Arduino-serail setup
light_s_A = board.get_pin('a:0:i')
#Light sensor B Arduino setup
light_s_B = board.get_pin('a:1:i')
#Light sensor B Arduino setup
light_s_C = board.get_pin('a:2:i')
#Light sensor B Arduino setup
light_s_D = board.get_pin('a:3:i')

# forw = (0), rev = (1) off = (1)
forw_neg = board.get_pin('d:7:o')
#forw = rev = off =1
rev_neg = board.get_pin('d:8:o')
#forw = rev = off =1
forw_pos = board.get_pin('d:5:o')

rev_pos = board.get_pin('d:6:o')
#temperature
#temperature = board.get_pin('a:2:i')
#Test LED arduino-serial setup

def assign_light_vals():
    while True:
        light_intensity_A = light_s_A.read()
        light_intensity_B = light_s_B.read()
        light_intensity_C = light_s_C.read()
        light_intensity_D = light_s_D.read()
        if light_intensity_A is not None and light_intensity_B is not None:
            #set time to
            time.sleep(1)
            light_int_list[0] = light_intensity_A
            light_int_list[1] = light_intensity_B
            light_int_list[2] = light_intensity_C
            light_int_list[3] = light_intensity_D
            act_light = (light_int_list[0] + light_int_list[1] + light_int_list[2] + light_int_list[3])/4
            #return(act_light)
            return (act_light)
            time.sleep(10)

        #return act_light
        else:
            time.sleep(1)
            print("looping assign vals again due to LS value being none")

no_terminate = True
while no_terminate:
    #fetch new actlight values every 15 min/(900 sec)
    time.sleep(5)
    assign_light_vals
    act_light = assign_light_vals()
    print(act_light)
    #print(light_int_list)
    no_terminate= False