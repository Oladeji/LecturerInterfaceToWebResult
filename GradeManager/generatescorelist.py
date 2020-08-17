import json
from django.conf  import settings
import openpyxl
from . DetailResult import DetailResult
import datetime

def generatescorelist(excel_file):
            wb = openpyxl.Workbook()        
            wb = openpyxl.load_workbook(excel_file)
            ws = wb["SCORESSHEET"]
            ws.protection.sheet = True
            row_start=7
            
            Secretkey =ws.cell(1, 1).value
            print(Secretkey)
            Secretkeyobj= json.loads(Secretkey)
            print(Secretkeyobj['CCODE'])
            total =int(Secretkeyobj['TOTAL'])
            scorelist = []  
  
            for i in range(row_start,total+ row_start):
                  DetailResultId ='123'
                  StudentId = ws.cell(i, 2).value
                  AsessionId ='2018/2020'
                  SemesterId =1
                  CourseId =ws.cell(i, 4).value
                  AsetId ='2018'
                  LevelToDo='400'
                  CourseState='E'
                  CourseUnit =2
                  CourseNature='E'
                  Score=ws.cell(i, 6).value 
                  AUserId =1
                  donedate= str(datetime.datetime.today())
                  ReadOnly= True
                
                  d1 = DetailResult(DetailResultId , StudentId , AsessionId, SemesterId, CourseId,  AsetId,  LevelToDo,  CourseState,  CourseUnit, 
                  CourseNature,  Score,  AUserId,  donedate,  ReadOnly  ) 
                  scorelist.append(d1) 
                
            return scorelist