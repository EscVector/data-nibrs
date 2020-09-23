import wget

s3_key1 = "http://s3-us-gov-west-1.amazonaws.com/cg-d3f0433b-a53e-4934-8b94-c678aa2cbaf3/"
s3_key2 = "http://s3-us-gov-west-1.amazonaws.com/cg-d4b776d0-d898-4153-90c8-8336f86bdfec/"

states = {}

with open("nibr-state-data.txt") as file:
   for line in file:
      line = line.replace("\n","")
      (key,value) = line.split("\t")
      states[key] = value

def download(url,filename):
   try:
      wget.download(url,filename)
   except Exception as e:
      print(str(e))
   
for key,value in states.items():
   loopcount = 2019-int(value)
   for x in range(0,loopcount):
      year = (int(value)+ x)
      filename = str(key+"-"+str(year)+".zip")
      if year <=2016:
         url = s3_key1+str(year)+"/"+filename
         print("\nDownloading:", url,filename)
         download(url,filename)
      else:
         url = s3_key2+str(year)+"/"+filename
         print("\nDownloading:", url,filename)
         download(url,filename)