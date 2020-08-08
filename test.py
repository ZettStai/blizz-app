import requests
import sched, time
import sys

API_SERVER = "http://35.223.105.4"

uri = API_SERVER 

def callApi():
    # Open a file with access mode 'a'
    with open("timeapi.log", "a") as file_object:
    # Append request response code and whether it was a success or failture
        response = requests.get(uri)
        file_object.write("\nResponse code: " + str(response.status_code) + "\n")
        print("\nResponse code: " + str(response.status_code))
        if response.status_code == 200:
            print("Success")
            file_object.write("Success\n")
            print(response.text)
            file_object.write(str(response.text))
        else:
            print('Failure')
            file_object.write("Failure\n")

scheduler = sched.scheduler(time.time, time.sleep)

def new_timed_call(calls_per_second, callback, *args, **kw):
    period = 1.0 / calls_per_second
    def reload():
        callback(*args, **kw)
        scheduler.enter(period, 0, reload, ())
    scheduler.enter(period, 0, reload, ())


new_timed_call(int(sys.argv[1]), callApi)  # takes the first argument after script name for calls per second (3, 3 calls/sec)

scheduler.run()
