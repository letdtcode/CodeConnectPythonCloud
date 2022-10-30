import insertUtil as ut
import psycopg2


#Tạo kết nối với RDS PostgreSQL và thêm dữ liệu vào
conn = psycopg2.connect(database='dbcovid19Postgre', user='postgres', password='abc123456', host='database-postgresql.cigivp9jsmup.us-east-1.rds.amazonaws.com', port='3306')
print('Open DB successfully')
ut.insert(conn)
ut.select(conn)
conn.close()
print('Successfully')