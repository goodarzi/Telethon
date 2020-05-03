#!/usr/bin/env python3
# Import modules to access environment, sleep, write to stderr
import time
import logging
import glob

# Import the client
from telethon.sync import TelegramClient, errors, functions, types

# Define some variables so the code reads easier
session = '<session file>'
api_id = 12345 #Replace with api id
api_hash = '<api hash>'

logging.basicConfig(level=logging.ERROR)

#from telethon.sync import connection #MTproxy
client = TelegramClient(
    session, api_id, api_hash,
#    connection=connection.ConnectionTcpMTProxyRandomizedIntermediate,
#    proxy=('<IP>', 443, '<secret>')
)
#client.session.flood_sleep_threshold = 

client.start()

#Download all profile photos of contacts
contact_result = client(functions.contacts.GetContactsRequest(
    hash=0
))
downloadcount=0
for user in contact_result.users:
    #if user.photo and user.mutual: #only mutual contacts
    if user.photo:
        #print(user.stringify())
        photo_result = client(functions.photos.GetUserPhotosRequest(
            user_id=user.id,
            offset=0,
            max_id=0,
            limit=100
        ))
        print('Download ', len(photo_result.photos), 'photos')
        for photo in photo_result.photos:            
            filename='./profile_photos/'+str(user.id)+'_'+photo.date.strftime('%Y-%m-%d_%H-%M-%S_%Z')+'_'+str(photo.id)
            if glob.glob(filename+'.*'):
                print ("File exist ",filename)
            else:
                downloadcount += 1
                if downloadcount > 99:
                    #wait 60 second to avoid flood error
                    print('sleep for 60 seconds.')
                    time.sleep(60)
                    downloadcount = 0
                # Printing download progress
                def callback(current, total):
                    print(filename,' Downloaded', current, 'out of', total,
                        'bytes: {:.2%}'.format(current / total))
                client.download_media(photo, file=filename, progress_callback=callback)
