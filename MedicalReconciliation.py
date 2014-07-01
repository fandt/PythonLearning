def test_sums():
  import csv
  import Tkinter, tkFileDialog
  import os
  file = "path/filetocreate"
  krecon = open(file,"w+")
  root = Tkinter.Tk()
  marker = 0
  deductotal = 0
  invoicetotal = 0
  InvoiceType = "Kaiser"
  deductSS = 0
  name = "blank"
  global found
  oddeven = 0
  missing = "blank"
  currentfile = tkFileDialog.askopenfilename(parent=root,initialdir="C:originpath",title='Choose the current deduction report')
  deductionfile = csv.reader(open(currentfile))
  for drow in deductionfile:
    if marker > 0:
        
        try:
          deductEE = float(drow[3])
          deductER = float(drow[4])
          name = drow[2]
          deductotal = round((deductotal + deductEE + deductER),2)
          deductSS = drow[6]
        except:
          pass
        #2 semi-monthly deductions = 1 monthly invoice, adding both deductions (if exist) to match against invoice
        if marker%2 == 0 :
          with open("C:filethatwascreated", 'a') as krecon:
            krecon.write(str(invoicetotal)+"\t"+InvoiceType+"\n")
          #print
          out = str(deductSS)+"\t"+str(name)+"\t"+str(deductotal)+"\t"
          with open("C:filethatwascreated", 'a') as krecon:
            krecon.write(out)
          
          found = 0
          #get invioce amount from downloaded files
          with open("C:invoice.csv") as csvfile:
            medent = csv.reader(csvfile)
            InvoiceType = "DHMO Union"

  #def test_download(medent,deductotal): DHMO Union
            for mrow in medent:
              try:
                invoiceSS = mrow[4]
                if invoiceSS == deductSS:
                  invoicetotal = float(mrow[9])
                  if abs(invoicetotal - deductotal) >= 1:
                    print name + " deduction amount= " + str(deductotal) + " DHMO Union invoice amount= " + str(mrow[9])
                    deductotal = 0
                  found = 1
                  break
              except:
                continue 

          deductotal = 0
          if found == 0:
            print name + " NOT FOUND IN INVOICES."
            InvoiceType = "--"
            invoicetotal = 0
    marker = marker + 1


#BACK - looking from invoice to deductions 
  with open("C:filethatwascreated", 'a') as krecon:
      krecon.write("\nNOT FOUND IN DEDUCTIONS")
      SumInvoice = 0
      
#deduction file 0 DHMO UNION
  deductionfile = csv.reader(open(currentfile))
  with open("C:invoice.csv") as csvfile:
    invoicefile = csv.reader(csvfile)
    file = "DHMO Union"
    for irow in invoicefile:
      deductionfile = csv.reader(open(currentfile))
      found = 0
      try:
          invoiceSS = irow[4]
      except:
          continue
      for drow in deductionfile:
        deductSS = drow[6]
        if invoiceSS == deductSS:
          found = 1
          break
      if found == 0 and irow[2] != "" and irow[9] != "" and irow[9] != "Total dues":
        print irow[2] + " Not found in deductions " + file + "\t\t" + str(irow[9])
        with open("C:/Users/rmorganstern/Documents/Medent Reconcile/Kaiser/krecon", 'a') as krecon:
            krecon.write("\n"+str(irow[4])+"\t" + str(irow[2])+"\t\t" +str(irow[9]))
        deductionfile = csv.reader(open(currentfile))

  
  with open("C:filethatwascreated", 'a') as krecon:
    krecon.write("\n\n" +"Total\t\t"+ str(SumInvoice))      
    
  raw_input("press enter to exit")





test_sums()
