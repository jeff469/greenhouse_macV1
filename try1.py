
def close_door():
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



 def open_door():
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


