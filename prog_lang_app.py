from flask import Flask

app = Flask(__name__)

in_memory_datastore = {
        "1":  {"empid": 1, "Firstname": "Dhamodaran", "Lastname": " V T", "D.O.B": "31/08/1999", "Salary": "13,000"},
        "2": {"empid": 2, "Firstname": "Mani", "Lastname": "P", "D.O.B": "05/12/1998", "Salary": "15,000"},
        "3": {"empid": 3, "First name": "Praveen", "Last name":"V", "D.O.B": "28/09/1998", "Salary": "10,000"},
        "4": { "empid": 4, "Firstname": "Radha Krishnan","Lastname":"", "D.O.B": "27/6/1998", "Salary": "8,000"},
        "5": {"empid": 5, "Firstname": "Dilli Vignesh","Lastname":"V", "D.O.B": "22/03/1998", "Salary": "9,000"},
        "6": {"empid": 6, "Firstname": "Karthick Raja","Lastname":"R", "D.O.B": "24/11/1999", "Salary": "9,000"},
        "7": {"empid": 7, "Firstname": "Mani Bharathi","Lastname":"R", "D.O.B": "29/10/1998", "Salary": "7,000"},
        "8": {"empid": 8, "Firstname": "Vijay kumar","Lastname":"V S", "D.O.B": "20/09/2000", "Salary": "17,000"},
        "9": {"empid": 9, "Firstname": "Mohan","Lastname":"A D", "D.O.B": "24/04/2000", "Salary": "10,000"},
        "10": {"empid": 10, "Firstname": "Naveen","Lastname":"G", "D.O.B": "23/08/1999", "Salary": "20,000"}
   }

@app.get('/employee')
def list_employee_lists():
   return {"employee_lists":list(in_memory_datastore.values())}

@app.route('/employee/empid=<employee_list_empid>')
def  get_employee_list(employee_list_empid):
   return in_memory_datastore[employee_list_empid]

if __name__=='__main__':
    app.run(debug=True)
