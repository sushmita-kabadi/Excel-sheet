import xlsxwriter
from xlwt import *
import time , xlwt
wb = xlsxwriter.Workbook('sushmita.xlsx')
ws = wb.add_worksheet('Sushmita')
cell_format = wb.add_format({'bold':True , 'italic':True})
cell_format.set_bg_color('yellow')
ws.write('A1','User Name',cell_format)
cnt = 2
for i in range(0,65544):
    ws.write('A'+str(cnt),'Sushmita')
    cnt = cnt+1
wb.close()
    
