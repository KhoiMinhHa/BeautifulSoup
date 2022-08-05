#import beautifulsoup and request here


#function to get job list from url f'https://www.talent.com/jobs?k={role}&l={location}'

def getJobList(role,location):
    url = f'https://www.talent.com/jobs?k={role}&l={location}'
    # Complete the missing part of this function here
    response = requests.get(url)
    print(response.status_code)
    soup = BeautifulSoup(response.content, 'html.parser')
    JobDetails = soup.find_all('div', class_='card card__job')
    #create an array here
    my_array = []
    for job in JobDetails:
       jobTitle = job.find('h2', class_='card__job-title').text.strip()
       company = job.find('div', class_='card__job-empname-label').text.strip()
       description = job.find('p', class_='card__job-snippet').text.replace('\n', '').replace("'", "").strip()
       jobDetailsjson = {
           "Title": jobTitle,
           "Company": company,
           "Description": description
       }
       #Add jobDetailsjson to that array
       my_array = [jobDetailsjson]
    return my_array

#save data in JSON file
def saveDataInJSON(jobDetails):
    #Complete the missing part of this function here
    print("Saving data to JSON")

#main function
def main():
    # Write a code here to get job location and role from user e.g. role = input()
    print("Enter role you want to search")
    role = input()
    print("Enter the location you want to searching for")
    location = input()
    # Complete the missing part of this function here
    print('\n')
    print(role)
    print(location)
    getJobList(role, location)
    saveDataInJSON(getJobList(role, location))
    
if __name__ == '__main__':
    main()
