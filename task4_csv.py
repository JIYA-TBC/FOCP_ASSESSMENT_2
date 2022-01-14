# importing csv module
import csv

#opens the csv file named result.csv in writing mode
with open('result.csv','w',newline='') as csv1:
    theresult = csv.writer(csv1)
    theresult.writerow(['Italy','10','France','50'])
    theresult.writerow(['England','6','Scotland','11'])
    theresult.writerow(['Wales','21','Ireland','16'])
    theresult.writerow(['England','41','Italy','18'])
    theresult.writerow(['Scotland','24','Wales','25'])
    theresult.writerow(['Ireland','13','France','15'])
    theresult.writerow(['Italy','10','Ireland','48'])
    theresult.writerow(['Wales','40','England','24'])
    theresult.writerow(['Italy','7','Wales','48'])
    theresult.writerow(['England','23','France','20'])
    theresult.writerow(['Scotland','24','Ireland','27'])
    theresult.writerow(['Scotland','52','Italy','10'])
    theresult.writerow(['Ireland','32','England','18'])
    theresult.writerow(['France','32','Wales','30'])
    theresult.writerow(['France','23','Scotland','27'])