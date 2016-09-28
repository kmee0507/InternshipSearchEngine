#Average Joes
#CS 21
#Internship search


import os

def main():
    #exception handling to ensure program wont break
    try:
    
        #welcome the user and prompt for username
        print('Welcome to E-interns\n')
        user_name = input('Username: ')
        print('')

        #if user name exists continue
        if os.path.exists(user_name+'.txt') and not user_name == '':
            file=open(user_name+'.txt','r')
            #display account info and open the menu
            print('Hello', user_name, 'your account information is: \n')
            
            for line in file:
                print(line)
            print('')
            menu(user_name)
               
            
            
            
        #if user name does not exist ask user if they want to create an account
        else:
            
            keep_going = input('Account does not exist, \
Would you like to create an account(y/n): ')
            while not(keep_going == 'y' or keep_going == 'n'):
                print('Invalid Selection')
                keep_going = input('Would you like to create an account\
(y/n): ')
            
            #if you decide to keep going prompt for desired username                 
            if keep_going == 'y':
                print('')
                user_name = input('Enter your desired Username: ')

                #open two files and prompt for name, major, graduation, and interests
                
                my_file = open(user_name +'.txt','w')
                favorites_file = open(user_name +'_favorites.txt','w')
                print('')
                name = input('What is your name? ')
                print('')
            
                major  = input('What is your major? ')
                print('')

                year = input('What is your expected year of graduation? ' )
                print('')

                interests = input('What are you interests? ')
                
                #write it all to a file
                my_file.write('Name: '+name+'\n')
                my_file.write('Major: '+major+'\n')
                my_file.write('Year of graduation: '+year+'\n')
                my_file.write('Interests: '+interests+'\n')
                my_file.close()
                
                my_file1 = open(user_name +'.txt','r')
                print('')
                print('')
                print('')
                print('')
                print('------------------------------------------------')
                print('')
                print('')
                print('')
                print('')
                #welcome the user and display the results and then open the menu
                print('Hello', user_name, 'your account information is: \n')
                for line in my_file1:
                    print(line)
                print('')
                menu(user_name)
            else:
                exit_program()
    except ValueError:
        print('invalid value')
    except:
        print('Error')
   
# this function displays the menu with 4 options, Search, View Favorites,
#internship resources, and quit
def menu(name1):
    try:
        keep_going = 'y'
        while keep_going == 'y':
            print('MAIN MENU')
            print('---------\n')
            print('1. Search\n')
            print('2. View Favorites\n')
            print('3. Internship Resources\n')
            print('4. Exit program\n')
            #prompt user for there choice
            selection = input('What would you like to do \
(choose corresponding number): ')
            print('')
            #depending on choice do what is necessary
            if selection == '1':
                search(name1)
                keep_going = input('Would you like to keep going(y/n): ')
                print('')
                while not(keep_going =='y' or keep_going == 'n'):
                    print('invalid choice\n')
                    keep_going = input('Would you like to keep going(y/n): ')
                    print('')
            elif selection == '2':
                favorites(name1)
                keep_going = input('Would you like to keep going(y/n): ')
                print('')
                while not(keep_going =='y' or keep_going == 'n'):
                    print('invalid choice\n')
                    keep_going = input('Would you like to keep going(y/n): ')
                    print('')
            elif selection == '3':
                internship_resources()
                keep_going = input('Would you like to keep going(y/n): ')
                print('')
                while not(keep_going =='y' or keep_going == 'n'):
                    print('invalid choice\n')
                    keep_going = input('Would you like to keep going(y/n): ')
                    print('')
            elif selection == '4':
                exit_program()
                break
         
            #if choice does not exist tell user and see if they would like to keep going
            else:
                print('That was not one of the choices\n')
                keep_going = input('Would you like to keep going(y/n): ')
                print('')
                while not(keep_going =='y' or keep_going == 'n'):
                    print('invalid choice\n')
                    keep_going = input('Would you like to keep going(y/n): ')
                    print('')
        #if keep going is a no end the program
        if keep_going == 'n':
            print('See ya later')
    except:
        print('Error')
    
#this function exists the program
def exit_program():
    return

#this function allows the user to search the file for internships
def search(name):
    try:
        #open the files
        jobs=[]
        infile=open("internships_average_joes.txt","r")
        file = open(name+'_favorites.txt','a')
        d={}
        index = 0
        i=0
        #read each line in the file add to the dictionary 
        for line in infile:
            i=i+1
     
            readline = line.rstrip().split(":")
            s1=readline[0]
            s2=readline[1]
            s2=list(readline[1].split(','))
            
            d[s1]=s2
            #if is 5 append to jobs
            if i==5:
                       
                jobs.append(d)
                d={}
                i=0
        #prompt user to search within something
        userset=input("Search within?: ")
        userset=userset.upper()
        print('')
        #prompt user for a key word
        key=[input("Keyword: ")]
        print('')
        #make sure its validated
        if userset!= " ":
            
            for job in jobs:
                value=job[userset]
                
                #if value is the key replace things
                if value==key:
                    job=str(job)
                    job=job.replace("'","")
                    job=job.replace('{',"")
                    job=job.replace('}',"")
                    job=job.replace('[',"")
                    job=job.replace(']',"")
                    job=job.replace(',',"")

                    
                    print(job)
                    print(" ")
                    #prompt user if they want to add to favorites
                    option = input('Would you like to add this to your favorites(y/n): ')
                    print('')
                    #either yes or no
                    if option == 'y':
                        file.write(str(job)+'\n')
                    else:
                        pass
                    
                    
                else:
                    pass
        else:
            print("No results found.")
    except:
        print('Error')
        print('')

 
            

        
        
    
        
    

# this function displays the favorites if there are any and puts them into a list
def favorites(name):
    try:
        my_list=[]
        #open the favorites file for reading
        fav_file = open(name+'_favorites.txt','r')
        
        print('')
        print('FAVORITES')
        print('---------\n')
        for line in fav_file:
            line = line.rstrip('\n')
            
            print(line)
            print('')
            
            
            my_list.append(line)
        fav_file.close()
        
        #ask user if they would like to delete any of these entries
        choice = input('Do you want to delete any of these entries (y/n): ')
        print('')
        #if they want to delete an entry over write the text file
        if choice == 'y':
            fav_file1 = open(name+'_favorites.txt','w')
            
            item = input('Which job should be removed from favorites: ')
            
            if item in my_list:
                my_list.remove(item)
                print('')
                print(item+'\n','Has been removed from your favorites\n')
            else:
                print('')
                print('invalid item\n')
            for i in my_list:
                fav_file1.write(i+'\n')
        #otherwise return
        else:
            return
    except IOError:
        print('file does not exist')
    except ValueError:
        print('Incorrect Value')
    except:
        print('Error')

        
#this function gives a bunch of links to different useful internship things aroun
#the area
def internship_resources():
    try:
        #welcome the user and display the possible options which are
        #resume builder, campus resources, apartment rentals, cars, and networking
        print('Welcome to the internship resources page:')
        print('')

        print('1. Resume builder\n')
        print('2. Campus Resources\n')
        print('3. Apartment Rentals\n')
        print('4. Cars\n')
        print('5. Networking\n')
        
        #prompt user for what they would like to do
        selection = input('What do you want to look into(select corresponding number): ')
        print('')

        #depending on selection do what is necessary
        if selection == '1':
            print('Heres 2 links to get you started with your resume:\n')
            print('http://www.gotresumebuilder.com')
            print('')
            print('http://www.resumebuilder.org')
            print('')
        elif selection == '2':
            print('Heres 2 links to the uvm catamount job site:\n')
            print('http://www.uvm.edu/~career/?Page=cjl.html')
            print('')
            print('http://www.uvm.edu/~career/?Page=hub.html')
            print('')
        elif selection == '3':
            print('Heres 2 links to get you started with your apartment search\n')
            print('http://www.burlingtonrent.com')
            print('')
            print('http://802apartments.com')
            print('')
        elif selection == '4':
            print('Heres a 2 links to get you started with finding a vehicle:\n')
            print('http://www.cars.com')
            print('')
            print('http://www.autotrader.com')
            print('')
        elif selection == '5':
            print('Heres 2 links to get you connected with some people in your field:\n')
            print('http://www.studentinternnetwork.com')
            print('')
            print('https://www.linkedin.com ')
            print('')
        #if none of the choices are selected display invalid choice
        else:
            print('Invalid choice')
    except ValueError:
        print('Invalid value')
    except:
        print('Error')

    
        

main()
        
        
    
