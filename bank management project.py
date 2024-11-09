import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt

df = pd.DataFrame()
csv_file = "/Users/ritvijakatare/Downloads/1000 BT Records.csv"

def introduction():
    msg = '-'

    for x in msg:
        print('Python is a case sensitive language,so type exact column name wherever required')
        print(x, end= '')
        time.sleep(0.002)
        wait = input("Press any key to continue - ")

def read_csv_file():
    df = pd.read_csv(csv_file)
    print(df)

def clear():
    for x in range(65):
        print()

def data_analysis_menu():
    df = pd.read_csv(csv_file)
    while True:
        clear()
        print("\n\n Data Analysis Menu \n")
        print('_' *100)
        print('1. Show Whole DataFrame \n')
        print('2. Show Columns \n')
        print('3. Show Top Rows \n')
        print('4. Show Bottom Rows \n')
        print('5. Show Specific Columns\n')
        print('6. Add a new record \n')
        print('7. Add a New Column \n')
        print('8. Delete a Column \n')
        print('9. Delete a Record\n')
        print('10. Update a Record\n')
        print('11. Rating Wise Report \n')
        print('12. Data Summary\n')
        print('13. Exit (Move to main menu)\n')

        ch = int(input('Enter Your Choice:'))

        if ch == 1:
            print('The Whole Dataframe is:-')
            print(df)
            wait = input()
        if ch == 2:
            print('The columns of the DataFrame are:')
            print(df.columns)
            wait = input()
        if ch == 3:
            n = int(input('Enter Total rows you want to show :'))
            print(df.head(n))
            wait = input()
        if ch == 4:
            n = int(input('Enter Total rows you want to display: '))
            print(df.tail(n))
            wait = input()
        if ch == 5:
            print(df.columns)
            col_name = input('Enter Column Name that You want to print : ')
            print(df[col_name])
            wait = input()
        if ch == 6 :
            a = input('Enter date: ')
            b = input('Enter description: ')
            c = input('Enter deposits: ')
            d = input('Enter withdrawals: ')
            e = input('Enter balance: ')
            
            data={'Date':a,'Description':b,"Deposits":c,'Withdrawls':d,'Balance':e}
            df = df.append(data, ignore_index =True)
            print(df)
            wait = input()
        if ch==7:
            col_name = input('Enter new column name :')
            col_value = int(input('Enter default column value :'))
            df[col_name]=col_value
            print(df)
            print('The command has been executed.')
            print('\n\n\n Press any key to continue....')
            wait=input()

        if ch == 8:
            col_name = input('Enter Column Name to delete')
            del df[col_name]
            print(df)
            print('The column has been deleted.')
            print('\n\n\n Press any key to continue....')
            wait=input()
        if ch ==9:
            index_no = int(input('Enter the Index Number that You want to delete :'))
            df = df.drop(df.index[index_no])
            print(df)
            print('The record has been deleted.')
            print('\n\n\n Press any key to continue....')
            wait = input()
        #update a record - this is to be cover
        if ch == 10:
            index_no = int(input('Enter the index number you want to update: '))
            df = df.drop(df.index[index_no])
            print(df)
            print('\n\n\n Press Any Key to Continue:')
            wait =input()
        if ch == 11:
            g = df.sort_values(by=['Deposits','Balance'],ascending = False)
            clear()
            print('Top 5 mode of transactions are: ')
            print('-'*120)
            print(g.head())
            print('\n\n\n Press any key to continue')
            wait = input()
        if ch == 12:
            print(df.describe())
            print('\n\n\n Press any key to continue')
            wait = input()
        if ch == 13:
            break

def graph():
    df = pd.read_csv(csv_file)
    while True:
        clear()
        print('\n GRAPH MENU')
        print('-'*100)
        print('1. Whole data Line Graph\n')
        print('2. Whole Data Bar Graph\n')
        print('3. Whole Data Bar Graph Horizontal\n ')
        print('4. Whole Data Scatter Graph\n')
        print('5. Exit(Move to Main Menu)\n')
        ch = int(input('Enter your choice:'))

        if ch == 1:
            g = df.groupby(by ='Description')
            x = df['Description'].unique()
            y = g['Description'].count()
            plt.xticks(rotation='vertical')
            plt.ylabel('No. Of Transactions')
            plt.title('Mode of Transaction')
            plt.title('Transaction wise records')
            plt.grid(True)
            plt.plot(x,y)
            plt.show()
        if ch == 2:
            g = df.groupby('Description')
            x = df['Description'].unique()
            y = g['Description'].count() #plt.xticks(rotation='vertical') plt.xlabel('Language')
            plt.ylabel('No. Of Transactions')
            plt.title('Mode of Transaction')
            plt.bar(x, y)
            plt.grid(True)
            plt.show()
        
        if ch == 3:
            g = df.groupby('Description')
            x = df['Description'].unique()
            y = g['Description'].count() #plt.xticks(rotation='vertical') plt.xlabel('Language')
            plt.ylabel('No. Of Transactions')
            plt.title('Mode of Transaction')
            plt.barh(x, y)
            plt.grid(True)
            plt.show()
        
        if ch == 4:
            g = df.groupby('Description')
            x = df['Description'].unique()
            y = g['Description'].count()  #plt.xticks(rotation='vertical') plt.xlabel('Language')
            plt.ylabel('No. Of Transactions')
            plt.title('Mode of Transaction')
            plt.grid(True)
            plt.scatter(x, y)
            plt.show()
            wait = input()
        
        if ch == 5:
            break

def export_menu():
    
    df = pd.read_csv(csv_file)
    
    while True:
        
        clear()
        print('\n\nEXPORT MENU ')
        print('_'*100)
        print()
        print('1. CSV File\n')
        print('2. Excel File\n')
        print('3. Exit (Move to main menu)')
        ch = int(input('Enter your Choice : '))
        
        if ch == 1:
            
            x = df.to_csv('/Users/ritvijakatare/Downloads/bank.csv')
            print('\n\n /Users/ritvijakatare/Downloads/bank.csv')
            print(df)
            
            wait = input()
        if ch == 2:
            df.to_excel('/Users/ritvijakatare/Desktop/1000 BT Records 2.xlsx')
            print('\n\n /Users/ritvijakatare/Desktop/1000 BT Records 2.xlsx')
            wait = input()
        if ch == 3:
            break
            
  
        
       
def main_menu():
    clear()
    introduction()
    while True:
        clear()
        print('MAIN MENU ')
        print('_'*100)
        print()
        print('1.Read CSV File\n')
        print('2.Data Analysis Menu\n')
        print('3.Graph Menu\n')
        print('4.Export Data\n')
        print('5.Exit\n')
        choice = int(input('Enter your choice :'))


        if choice == 1:
            read_csv_file()
            wait = input()
        if choice == 2:
            data_analysis_menu()
            wait = input()
        if choice == 3:
            graph()
            wait = input()
        if choice == 4:
            export_menu()
            wait = input()
        if choice == 5:
            break
    clear()
main_menu()

# call main menu main_menu()

        

    
            
            
            
            
        
        
        
























