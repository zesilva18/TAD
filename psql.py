import psycopg2
import pandas as pd
import numpy as np

# Definindo os parâmetros de conexão
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    host="localhost",  # Ou outro host, se necessário
    port="5432"  # A porta padrão do PostgreSQL
)

#Employee_ID,Age,Gender,Job_Role,Industry,Years_of_Experience,Work_Location,Hours_Worked_Per_Week,Number_of_Virtual_Meetings,Work_Life_Balance_Rating
#Stress_Level,Mental_Health_Condition,Access_to_Mental_Health_Resources,Productivity_Change,Social_Isolation_Rating,Satisfaction_with_Remote_Work,Company_Support_for_Remote_Work,Physical_Activity,Sleep_Quality,Region


df = pd.read_csv('Impact_of_Remote_Work_on_Mental_Health.csv')

cursor = conn.cursor()

unique_jobs = {}
id_counter = 0

job_ids = np.zeros(len(df), dtype=int)


for index, row in df.iterrows():
    job_key = (row['Job_Role'], row['Industry'], row['Work_Location'])
    if job_key not in unique_jobs:
        unique_jobs[job_key] = id_counter
        id_counter += 1
    
    # Armazenar o job_id correspondente para cada linha do dataset
    job_ids[index] = unique_jobs[job_key]

id = 0
    

for index, row in df.iterrows():
    
    regiao = ""
    
    if row['Region'] == "Europe":
        
        regiao = "Europa"
    
    elif row['Region'] == "Asia":

        regiao = "Ásia"
    
    elif row['Region'] == "Africa":
        
        regiao = "África"
    
    elif row['Region'] == "North America":
        
        regiao = "América do Norte"
    
    elif row['Region'] == "South America":
        
        regiao = "América do Sul"
    
    elif row['Region'] == "Oceania":
        
        regiao = "Oceania"
        
    
    cursor.execute("""
        INSERT INTO fact_mental_health  (mental_id, mental_health_condition, stress_level, productivity_change, satisfaction_with_remote_work, job_job_id, continent_region, person_employee_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (id, row['Mental_Health_Condition'], row['Stress_Level'], row['Productivity_Change'], row['Satisfaction_with_Remote_Work'], int(job_ids[index]), regiao, row['Employee_ID']))
    
    print(id)

    id = id + 1

conn.commit()  # Adicione esta linha

query = "SELECT * FROM fact_mental_health"


df = pd.read_sql(query, conn)


# Fechando a conexão
conn.close()
