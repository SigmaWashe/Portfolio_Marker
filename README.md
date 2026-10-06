![Portfolio Marker](project_images/logo.png)


<details>
  <summary style="font-size: 18px; font-weight: bold;">Table of Contents</summary>
  <ol>
    <li> <a href="#overview">Overview</a> </li>
    <li> <a href="#usage">Usage</a> </li>
    <li> <a href="#installation">Installation</a> </li>
    <li>
      <a href="#how-to-use-it">How To Use It</a>
      <ul>
        <li>
          <details>
            <summary><a href="#students">Students</a></summary>
            <ul>
              <li><a href="#student-signup">Student Signup</a></li>
            </ul>
          </details>
        </li>
        <li>
          <details>
            <summary><a href="#teachers">Teachers</a></summary>
            <ul>
              <li><a href="#teacher-signup">Teacher Signup</a></li>
            </ul>
          </details>
        </li>
      </ul>
    </li>
  </ol>
</details>


## Overview
*** 
>Portfolio Marker is an app that allows the user to input their marks and automatically perform the necessary calculations for their assessments and exams. 
> Once when all the necessary assessments and exams have been input the user is able to download their SBA coversheet.


## Usage
***
Make sure that you have at least python 3.12 installed
    
**windows**
```bash
winget install Python.Python.3.12
```

**mac**
```bash
brew install python
```

## Installation
***
Below are the steps that you need to take in order to use the project.

1. Clone the GitHub repository
   ```bash
   git clone https://github.com/SigmaWashe/Portfolio_Marker.git
   ```
2. Install the required pips
   ```bash
   pip install -r requirements.txt
   ```
3. Run the necessary migrations to create the database
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ``` 
4. A default admin user is created during migration
   ```bash
    username = 'admin'
    password = 'admin123'
    email    = 'admin@example.com'
   ```

## How To Use It

### Students
***
#### Student Signup
1. The student has to create an account by using their exam number, name and surname.
2. The student also has to use a secure password and once their account has been created they will be redirected to a page 
where they will be prompted to select their subjects.
3. After the student has completed creating their account they will be redirected to the dashboard.


### Teachers
***
#### Teacher Signup
1. The teacher has to create an account by using their name, surname, email, subject and the school they teach at.
2. The teacher also has to use a secure password and once their account has been created they will be redirected their dashboard.
3. Once the teacher is done creating their account they will be able to add students to their roster and manage their marks as well.

