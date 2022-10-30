import insertUtil as ut
import psycopg2


#Tạo kết nối với RDS PostgreSQL và thêm dữ liệu vào
conn = psycopg2.connect(database='dbcovid19Postgre', user='postgres', password='abc123456', host='database-postgresql.cgeb5ecbsirb.us-east-1.rds.amazonaws.com', port='5432')
print('Open DB successfully')
ut.insert(conn)
ut.select(conn)
conn.close()
print('Successfully')