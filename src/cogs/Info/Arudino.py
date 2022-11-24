import discord
from discord.ext import commands
from discord.ext.commands import Bot, BucketType, cooldown
import time 
import serial

try:
    arduino = serial.Serial() # create serial port object called arduinoSerialData
    try:
        arduino.baudrate = 9600   # set Baud rate to 9600
        arduino.port = 'COM4' # COMxx   format on Windows 
                              # ttyUSB0 format on Linux
        arduino.bytesize = 8      # Number of data bits = 8
        arduino.parity = 'N'      # No parity
        arduino.stopbits = 1      # Number of Stop bits = 1
        print(arduino)
        time.sleep(1.5)
    except Exception as e:
        print(e)
except Exception as e:
    print('An Exception Occured')
    print('Exception Details-> ', e)


class arduino(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_application_command_error(self, ctx, error):
        # sourcery skip: instance-method-first-arg-name
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.respond(error)    
        else:
            raise error    
        
    @commands.slash_command(name="led", description="Turn on/off led")
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def led(self, ctx):
        arduino.write(b'3')
        print("LED ON")
        time.sleep(0.2)
        arduino.write(b'2') # send 2

    @commands.slash_command(name="buzzer", description="Turn on/off buzzer")
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def buzzer(self, ctx):
        arduino.write(b'1')
        print("BUZZER ON")
        time.sleep(0.2)
        arduino.write(b'0')
        
def setup(bot):  # sourcery skip: instance-method-first-arg-name
    bot.add_cog(arduino(bot))