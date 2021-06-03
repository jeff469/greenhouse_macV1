
door_closed = True
on= True


while on:

    import logging
    import time
    from datetime import date
    from datetime import datetime

    import Greenhouseconditions0
    import light_levels0
    import checktemp0
    from Greenhouseconditions0 import G0



    actual_temperature = G0.act_temp

    optimal_temperature = G0.opti_temp
    act_light= G0.actual_light
    opti_light=G0.opti_light
    print("temperature is:  " + str(checktemp0.temperature))

    if act_light < 0.8:
        is_day = True
    else:
        is_day = False

    if is_day:
        optimal_temperature = G0.opti_temp
        print("Time: is day")

    else:
        optimal_temperature = G0.opti_temp - 5
        print("Time: is night, optimal temp lowered")

    print("-optimal temperature-")
    print(optimal_temperature)


    #close door
    if (actual_temperature) < optimal_temperature and not door_closed:
        print("closing door..")
        light_levels0.rev_neg.write(1)
        light_levels0.rev_pos.write(1)
        light_levels0.forw_neg.write(0)
        light_levels0.forw_pos.write(0)

        light_levels0.time.sleep(25)

        light_levels0.forw_neg.write(1)
        light_levels0.forw_pos.write(1)

        door_closed = True
        print("door closed")
        print("waiting for next cycle")

    if (actual_temperature) < optimal_temperature and door_closed:
        print("temp too low but door closed already")
        time.sleep(20)

    if (actual_temperature) > optimal_temperature and door_closed:
        print("opening door..")
        light_levels0.rev_neg.write(0)
        light_levels0.rev_pos.write(0)
        light_levels0.forw_neg.write(1)
        light_levels0.forw_pos.write(1)

        light_levels0.time.sleep(25)

        light_levels0.rev_neg.write(0)
        light_levels0.rev_pos.write(0)
        door_closed = False
        print("door opened")
        print("waiting for next cycle")
        time.sleep(20)

    if (actual_temperature) > optimal_temperature and not door_closed:
        print("temp hot but already open")
        time.sleep(20)

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")

    today = date.today()
    print("today is " + str(today))

    file = "log " + str(today)

    logging.basicConfig(filename=(file), level=logging.DEBUG,
                        format='%(message)s')

    logging.debug("time:  " + str(current_time))
    logging.debug("light:  " + str(Greenhouseconditions0.G0.actual_light))
    logging.debug("temperature:   " + str(checktemp0.temperature))