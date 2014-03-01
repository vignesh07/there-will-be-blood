from gcm import GCM
import access_gcm
#gcm = GCM('AIzaSyCbEFJvsCgSgGulvJMcdnkqnFFuygFvPJE')
data = {'message': 'nigger yo'}

gcmm = access_gcm.gcm
reg_ids = access_gcm.reg_ids

# Plaintext request
#reg_id = 'APA91bEOiJCDqtRCxPmUXyWAQZJkn5VU1mnfSkx81Py5bQY7MDO424_xCBJ_3B8jXLUoKu5m4n9kWjPb9KUN28E3tefa-j2szrJc9ekIRc_p-Cqb7FyQC41iZe9MARpcq8ciCBHOkGePdSWEGEMYMNcrxZPBuP9-1Q'

#gcm.plaintext_request(registration_id=reg_id, data=data)

# JSON request
#reg_ids = ['APA91bEOiJCDqtRCxPmUXyWAQZJkn5VU1mnfSkx81Py5bQY7MDO424_xCBJ_3B8jXLUoKu5m4n9kWjPb9KUN28E3tefa-j2szrJc9ekIRc_p-Cqb7FyQC41iZe9MARpcq8ciCBHOkGePdSWEGEMYMNcrxZPBuP9-1Q','APA91bEv9_z85UdoFmB0_9xUpGhB1E2yPLvUcRHoz52uGzfNj1IZKUTUmxznwYuIzS1IHt_Tp0h5OhYrwSJH6xaCuPJB-Qu_cjxXwPWuTx7B4Y9BdBceeeZlGJ8nPbSq4GUvqcnnLise8_yCWdS3VpfHXxBdRvI31w']
response = gcmm.json_request(registration_ids=reg_ids, data=data)

# Extra arguments
#res = gcm.json_request(
#    registration_ids=reg_ids, data=data,
#    collapse_key='uptoyou', delay_while_idle=True, time_to_live=3600
#)
