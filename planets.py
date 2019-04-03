def weight_on_planets():
   Weight = input('What do you weigh on earth? ')
   
   #Using cast to change str -> float
   EarthWeight = float(Weight)
   
   #Generate weights on other planets using given values
   MarsWeight = (EarthWeight * 0.38)
   JupiterWeight = (EarthWeight * 2.34)
   
   #Create blank line before the first sentence
   #Specify next string is on a different line
   MarsString = ("\nOn Mars you would weigh %.2f pounds.\n" %MarsWeight)
   
   #Format the dloating point to 2 digits after the decimal
   JupiterString = ("On Jupiter you would weigh %.2f pounds." %JupiterWeight)
   
   #Concatenate the 2 strings for the final string
   FinalString = MarsString + JupiterString
   
   print(FinalString, end='')
   
if __name__ == '__main__':
   weight_on_planets()