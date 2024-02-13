<h1 align="center">Hello, this is a project about Python</h1>
<h3 align="center">
  <h1>Description</h1>
  This project consists of a CRUD (Create, Read, Update, Delete) system that interacts with a MySQL database using input files to perform operations on a table called mae_empleados. <br>

  <h1>Functionalities</h1>
  • Create: The application creates records in the mae_empleados table from an input file, generating separate files for successful and failed inserts.<br>
  • Read: Allows querying and dumping all data from the mae_empleados table into an output file.<br>
  • Update: Updates records in the mae_empleados table based on the data provided in an input file, generating separate files for successful and failed updates.<br>
  • Delete: Deletes records from the mae_empleados table based on employee codes provided in an input file, generating separate files for successful and failed deletions.<br>
  
  <h1>Implementation Details</h1>
  • A program is implemented for each CRUD operation: altas_empleados_mysql.py, bajas_empleados_mysql.py, modificaciones_empleados_mysql.py, consulta_empleados_mysql.py.<br>
  • Input and output files follow a specific naming convention to distinguish between inserts, deletes, updates, and queries, as well as between successful and failed operations.<br>
  • Proper error handling is ensured, such as handling duplicate records in inserts, non-existent employee codes in deletes, and non-existent employee codes for updates.<br>
  • Connection and communication with the MySQL database are performed using the API provided by MySQL.<br>
  • Performance and effectiveness of each program in interacting with MySQL are evaluated, assigning scores based on their performance.<br>
  
  <h1>File Structure</h1>


- altas_empleados_mysql.py
- bajas_empleados_mysql.py
- modificaciones_empleados_mysql.py
- consulta_empleados_mysql.py
- altas_mysql.txt
- modificaciones_mysql.txt
- bajas_mysql.txt
- altas_correctas_mysql.txt
- modificaciones_correctas_mysql.txt
- bajas_correctas_mysql.txt
- altas_erroneas_mysql.txt
- modificaciones_erroneas_mysql.txt
- bajas_erroneas_mysql.txt
- consulta_mysql.txt

<h1>Evaluation and Conclusion</h1>
Comprehensive testing is conducted to evaluate the performance and efficiency of each CRUD operation against MySQL. Maximum scores are assigned based on established evaluation criteria. This project provides a robust and effective solution for data management in a MySQL database through CRUD operations using input files.


</h3>

<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> <a href="https://www.mysql.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>
