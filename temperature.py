print("car engine status🚔")
print("__________________")

engine_temp=float(input(" enter the temperature:\n"))
oil_level=int(input("enter the oil level:\n"))
battery_voltage=int(input("enter the battery voltage:\n"))
if engine_temp <70:
    print("the temperature is too LOW_ please wait for it to warm up:")
elif engine_temp>=70 and engine_temp<= 100:
    print("the temperature is NORMAL")
    print("proceed with your journey")
    print("safe journey!")
elif engine_temp >100:
    print("the car engine temperature is too high🙆‍♂️🙆‍♂️")
    print("check the engine immediately:")
    print("use a coolant on the engine or wait for it to cool")
else:
    print("⚠️ mechanical check up")    
if oil_level< 2:
    print("the oil_level is too low🪫")
    print("- add the oil")
    print("-to avoid emergency drive stop")
elif oil_level >=2 and oil_level<4:
    print("the oil_level is normal ")    
    print("safe journey")   
elif oil_level  >4:
    print("the oil_level is too HIGH🙆‍♂️🙆‍♂️")  
    print("lower the level to required level") 
else:
    print("⚠️ take caution")
if battery_voltage <12:
    print("the voltage is too low🪫🪫")
    print("please recharge ") 
elif 12<= battery_voltage<=14.5:
    print("the battery level is GOOD")
    print("drive safe👌👌") 
else:
    print("⚡⚡⚠️⚠️ too HIGH🙆‍♂️🙆‍♂️" ) 
    print("battery issues")


print("check the vehicle status:🚔🚔-drive safe")    