import string, itertools, random, os, sys, time, signal
print("NOTE: This Password Cracking will take longer. If you put strong password, You will recieve longer time to crack")
userPwd=input("Enter Password to begin Cracking your Password: ")
pwd=list(string.ascii_letters+string.digits+'@#$%&*:;')
pw=''
print("Cracking Password.....")
start_cpu,c=time.process_time(),0
def handler(signum, frame):
    print("Signal handler called with signal", signum)
    exit(0)
signal.signal(signal.SIGINT, handler)
while pw!=userPwd:
   pw=''
   for _ in range(len(userPwd)):
      gues=pwd[random.randint(0,len(pwd)-1)]
      pw+=str(gues)
      print(pw,flush=True)
      '''if len(pw)==len(userPwd):
        print(pw)'''                #Get only n ways
      c+=1
      time.sleep(0.2)
end_cpu=time.process_time()
print("Your Password is ",pw)
cpu_time=end_cpu-start_cpu
print(f"Password cracked in {cpu_time:.2f} seconds.")
print("Number of inputs used:",c)
