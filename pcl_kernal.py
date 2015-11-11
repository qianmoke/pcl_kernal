#!/usr/bin/env python
#coding=gbk
import sys
import frame
import datetime
import xlwt
import xlrd

#the time collect of pcl in server.log
class cal_pcltime_kernal:
  def __init__(self,f1):
    self.start_time_col=5
    self.stop_time_col=6
    self.period_col=7
    self.dic_time={}
    self.seq=[]
    self.workbook=xlrd.open_workbook(f1)
    self.seq_final=[]
  def begin(self):
    pass
  def choose_first(self):
    for sheet in self.workbook.sheets():
      for row in xrange(sheet.nrows):
        if row != 0:
          start_time=sheet.cell(row,self.start_time_col).value
          stop_time=sheet.cell(row,self.stop_time_col).value
          time=sheet.cell(row,self.period_col).value
          if self.dic_time.has_key(start_time):
            if time >=self.dic_time[start_time][0]:
              self.dic_time[start_time][0]=time
          else:
            self.dic_time[start_time]=[]
            self.dic_time[start_time].append(time)
            self.seq.append(start_time)

  def choose_second(self):
    i=0
    for now in self.seq:
      if i>0:
        time_now=datetime.datetime.strptime(now,"%H:%M:%S")
        time_fre=datetime.datetime.strptime(self.seq_final[i-1],"%H:%M:%S")
        delta=(time_now-time_fre).seconds
        period=delta + self.dic_time[now][0]
        #print now,sequence_today_final[i-1],delta,yesterday_result[now][0],period
        if period >= self.dic_time[self.seq_final[i-1]][0]:
          self.seq_final.append(now)
          i +=1
      else:
        self.seq_final.append(now)
        i +=1

  def end(self):
    pass
  def description(self):
    return "Collection Data of PCL Running Time in Kernal"
  def result(self):
    s=""
    for time in self.seq_final:
      s += time
      s += " "
      s += str(self.dic_time[time])
      s += "\n"
    return s

kernal = frame.controller()
today=cal_pcltime_kernal('2015-10-09.xlsx')
yesterday=cal_pcltime_kernal('2015-11-06.xlsx')
kernal.subscribe(today)
kernal.subscribe(yesterday)
kernal.run()
kernal.print_results()
