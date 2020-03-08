from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import csv

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a spreadsheet.
SPREADSHEET_ID = '1s8-9pxkwPvWaOeYIqnnntlkEuhreZWr8LBmV-0jL_5s'
RANGE_NAME = 'Sheet1!A:G'

def get_value():
    values = main()
    return values[0][0]

def main():
    """Shows basic usage of the Sheets API.
    Puts values from a spreadsheet into a csv.
    """
    creds = None ####FIGURE OUT HOW TO GET THESE PICKLED THINGS WORKING####
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    # if os.path.exists('token.pickle'):
    #     with open('token.pickle', 'rb') as token:
    #         creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token, protocol=2)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range=RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print('Creating csv')
        with open('kyr_data.csv', 'w',) as file: #removed newline='' bc erroring out in python 2.7
            for row in values:
            # Print columns A through G, which correspond to indices 0 through 6.
                print(row[0])
                writer = csv.writer(file)
                writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6]])
        print('Finished csv')
        return values

if __name__ == '__main__':
    main()