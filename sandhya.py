from twilio.rest import Client 
import keys
 
account_sid = 'ACa692427848369035b409b363b2f8d938' 
auth_token = '[AuthToken]' 
client = Client(keys.account_sid,keys.auth_token) 
 
message = client.messages.create(  
                              
                              body='Hi, how are you ',      
                              from=keys.from_num
                              to=keys.to_num
                          ) 
 
print(message.body)