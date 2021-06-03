import light_levels0
import checktemp0


class Greenhouse_conditions:
        def __init__ (self, opti_temp, act_temp, act_light, opti_light):
            self.opti_temp = opti_temp
            self.act_temp = act_temp
            self.actual_light = act_light
            self.opti_light = opti_light
            #self.door = door

G0= Greenhouse_conditions(27,checktemp0.temperature, light_levels0.act_light,0.12,)
#print (G0.opti_temp)
#print (G0.act_temp)
#print (G0.actual_light)
#print(G0.opti_light)

#Light_level.relay_on.write(1)